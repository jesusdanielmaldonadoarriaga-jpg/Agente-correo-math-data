#!/usr/bin/env python3
"""Static integrity checks only. No network, Glean calls or Outlook writes."""
from pathlib import Path
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[1]

def require(condition, message):
    if not condition:
        raise SystemExit('FAIL: ' + message)

def read(relative):
    return (ROOT / relative).read_text(encoding='utf-8')

def main():
    manifest = json.loads(read('manifest.json'))
    baseline_bytes = (ROOT / 'baseline/INSTRUCTIONS.original.md').read_bytes()
    baseline = baseline_bytes.decode('utf-8')
    require(hashlib.sha256(baseline_bytes).hexdigest() == manifest['baseline_sha256'], 'Baseline hash mismatch')
    require(len(baseline) == manifest['baseline_characters'], 'Baseline length mismatch')
    reconstructed = read(manifest['orchestration']) + ''.join(read(manifest['section_paths'][str(n)]) for n in range(2, 9))
    require(reconstructed.encode('utf-8') == baseline_bytes, 'Original text was not preserved verbatim')
    urls = re.findall(r'https://[^\s|]+', reconstructed)
    require(urls == manifest['reference_urls'], 'Original URL/order mismatch')
    candidate = read('candidate/MAIN_INSTRUCTIONS.proposed.md')
    orchestration = read(manifest['orchestration'])
    role, core = orchestration.split('## 0.', 1)
    require(candidate.startswith(role), 'Candidate role changed')
    require('## 0.' + core in candidate, 'Candidate omitted original core gates/safeguards')
    request = next(x for x in baseline.splitlines() if x.startswith('**Request parts**'))
    victor = next(x for x in baseline.splitlines() if x.startswith('- **Victor route:**'))
    require(read('skills/weldmation-joel-victor/references/victor-route.md').strip() == victor, 'Victor rule mismatch')
    for name in ['weldmation-ecr-data', 'weldmation-alejandro']:
        require(read('skills/' + name + '/references/request-parts.md').strip() == request, 'Shared request-part procedure mismatch')
    found = sorted(p.parent.name for p in (ROOT / 'skills').glob('*/SKILL.md'))
    require(found == sorted(manifest['skills']), 'Missing or unexpected skill')
    for name in found:
        folder = ROOT / 'skills' / name
        skill = (folder / 'SKILL.md').read_text(encoding='utf-8')
        parts = skill.split('---', 2)
        require(skill.startswith('---\n') and len(parts) == 3, 'Missing frontmatter: ' + name)
        front = parts[1].strip().splitlines()
        require(front[0] == 'name: ' + name, 'Skill name mismatch: ' + name)
        require(re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', name) is not None and len(name) <= 64, 'Invalid skill name')
        require(front[1].startswith('description: '), 'Description missing: ' + name)
        description = json.loads(front[1].split(': ', 1)[1])
        require(isinstance(description, str) and 0 < len(description) <= 1024, 'Description invalid: ' + name)
        references = re.findall(r'`(references/[^`]+\.md)`', skill)
        require(bool(references), 'No declared references: ' + name)
        for rel in references:
            require((folder / rel).is_file(), 'Missing bundled file: ' + name + '/' + rel)
        files = [p for p in folder.rglob('*') if p.is_file()]
        require(len(files) <= 100, 'Skill exceeds file-count limit')
        require(all(len(p.relative_to(folder).parts) <= 6 for p in files), 'Skill nesting too deep')
        require(sum(p.stat().st_size for p in files) < 16 * 1024 * 1024, 'Skill exceeds unpacked-size limit')
        require(not any(p.is_symlink() for p in folder.rglob('*')), 'Symlinks not allowed')
    for rel, expected in manifest['file_sha256'].items():
        path = ROOT / rel
        require(path.is_file(), 'Missing file: ' + rel)
        require(hashlib.sha256(path.read_bytes()).hexdigest() == expected, 'File hash mismatch: ' + rel)
    print('PASS: baseline preserved byte-for-byte (' + str(len(baseline)) + ' characters).')
    print('PASS: original sections 0-8 reconstructed without omissions; ' + str(len(urls)) + ' original URLs retained.')
    print('PASS: four SKILL.md headers, local reference paths, shared extracts and package sizes checked.')
    print('PASS: proposed parent preserves original safety, routing and interaction gates.')
    print('PASS: repository file hashes verified.')
    print('NOT TESTED: GitHub/Glean import, runtime skill loading, document permissions, manager detection or Outlook drafts.')

if __name__ == '__main__':
    main()
