# Herramientas y dependencias del agente de prueba
Mantener las mismas herramientas del agente original; importar una Skill no concede permisos ni conecta Outlook automáticamente.

- Employee Search: identidad, manager y contactos.
- Microsoft Outlook Extension Actions: Create email draft.
- Microsoft Outlook Extension Actions: Add mail attachment.
- Microsoft Outlook Extension Actions: Get email message.
- Microsoft Outlook Extension Actions: List outlook attachments.
- Glean Document Reader y Shell son capacidades de ejecución disponibles en Auto Agents; no se añaden como acciones explícitas en este paquete.

No se requieren búsqueda de documentos, herramientas de GitHub durante cada ejecución, envío de correos ni nuevas credenciales en el repositorio. Importar desde GitHub privado sí requiere autorización de acceso al repositorio y habilitación administrativa de esa función.
No cambiar modelo, disparadores, destinatarios ni permisos como parte de esta separación. No importar `baseline/` como una Skill. El paquete no incluye una definición `spec.yaml` ni modifica herramientas/configuración automáticamente.
