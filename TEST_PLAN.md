# Plan de pruebas — pendiente de ejecución en Glean

## Separación de estados
- Validación estática del paquete: ver `STATIC_VALIDATION.txt` si está presente.
- Importación/ejecución modular real: **NO ejecutadas**.
- Las pruebas anteriores del agente monolítico no certifican estas Skills.
- Usar copia de prueba aislada. Para probar Victor sin un usuario real de ese equipo, etiquetar el caso como simulación; no falsear el manager del solicitante ni afirmar validación real del directorio.

## Fase A: sin escrituras
Pedir explícitamente una evaluación de reglas sin generar borradores, sin llamadas de escritura Outlook. Comprobar en el registro qué Skill/referencia se leyó. Esta fase no demuestra funcionamiento real de Outlook.

| Caso | Resultado esperado | Estado |
|---|---|---|
| Solo número ECR | Pide Summary y PAT; espera antes de plantilla/imagen | Pendiente |
| Un adjunto | Solo pide el faltante | Pendiente |
| Archivo ilegible/ECR diferente | Pide reemplazo o aclaración; no mezcla ECR | Pendiente |
| Manager Joel | Menú de seis, SUP original donde exista | Pendiente |
| Manager Victor | Mismas seis/reglas Joel; SUP Victor y correo verificado o vacío; nunca correo Jose Maria | Pendiente |
| Manager Alejandro | Tres variantes; opción 3 = Math Data Request; sin checklist y DLT sin confirmar vacío | Pendiente |
| Manager ambiguo/distinto | Pregunta área; no defecto Joel | Pendiente |
| Plantilla ya elegida | No repite menú | Pendiente |
| Rechazo de imagen | No re-pregunta, recordatorio, espera o marco vacío en seguimientos | Pendiente |
| Imagen sí sin archivo | Espera carga/cancelación explícita | Pendiente |
| ADD/CHANGE con repetidos | Una categoría por acción, números solos, deduplicación solo dentro de acción/columna, ceros iniciales conservados | Pendiente |
| Otra acción/acción desconocida | No fuerza ADD/CHANGE ni inventa; informa desconocidos | Pendiente |
| Solicitud de Math | Solo partes seleccionadas; Alejandro usa mismo conjunto en intro y PART NUMBER/S | Pendiente |
| Workflow Execute 10.1/ausente | Suposición limitada Joel/Victor; jamás Alejandro; checklist vacío | Pendiente |
| Falta un dato ordinario | Campo vacío/nota externa, no nueva pregunta | Pendiente |
| Skill/referencia inaccesible | Reporta bloqueo; no otra área ni datos inventados | Pendiente |

## Fase B: ejecución controlada de borradores
Solo con autorización del usuario de prueba y adjuntos reales permitidos. Seleccionar una plantilla, resolver la imagen y permitir las acciones de borrador en su buzón. No repetir creación si existe un ID exitoso o hay fallo ambiguo.
Probar las seis variantes de Joel, las seis de Victor y las tres de Alejandro, en solicitudes separadas y sin duplicar innecesariamente borradores. Cubrir rechazo/carga de captura y reanudación de autorización.

Comprobaciones:
- Summary/PAT de la misma ECR, todos los programas/partes aplicables, sin datos de ejemplo.
- Joel/Victor: checklist correcto de 19/12/25/14/8/9 ítems según variante, respuestas vacías, colores y contactos originales salvo SUP Victor.
- Alejandro: ausencia completa de checklist, firma DE actual debajo de Best Regards, DLT vacío hasta confirmación; párrafos de proveedor exactos y fondo verde completo.
- El modelo lee referencias EML/Word seleccionadas; las URLs no son evidencia actual.
- Solo borrador en buzón del solicitante, To/Cc/Bcc vacío, sin envío ni adjuntos no aprobados.
- Imagen aceptada: bytes reales, tamaño inferior a 3 MB, CID coincidente, aspecto completo; comprobar readback y lista de adjuntos.
- Registrar diferencias de HTML; revisión visual manual en Outlook cuando se necesite, sin confundir HTML con equivalencia visual exacta.

## Criterios de aceptación y migración posterior
Registrar por caso: ruta/plantilla, evidencia utilizada, Skills/referencias consultadas, resultado esperado/real y defectos. Guardar evidencia sensible fuera del repositorio o en una ubicación autorizada.
No aceptar si faltan reglas, hay mezcla de áreas, se inventa correo, se pregunta de nuevo por imagen rechazada, se envía correo o se duplican borradores por recuperación automática.
La migración de producción requiere aprobación expresa posterior; este paquete no la ejecuta. Conservar `baseline/INSTRUCTIONS.original.md` para comparar/restaurar instrucciones si se modifica una copia posteriormente. No es un respaldo completo de permisos/herramientas/automatizaciones.
