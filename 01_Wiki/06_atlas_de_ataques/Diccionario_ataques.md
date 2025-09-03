# 📚 Diccionario Hacker Ético (Atlas de Ataques)

Cada ataque está estructurado con:  
🎯 **Método** = técnica utilizada  
💥 **Consecuencia** = qué produce  
🎯 **Objetivo** = finalidad del atacante

---

## 1. ARP Spoofing
- 🧪 Método: Envío de mensajes ARP falsificados en una red local.
- 💥 Consecuencia: Envenenamiento de cachés ARP (ARP Poisoning).
- 🎯 Objetivo: Interceptar tráfico de red (MitM).

## 2. DNS Spoofing
- 🧪 Método: Falsificación de respuestas DNS.
- 💥 Consecuencia: Redirección a sitios falsos.
- 🎯 Objetivo: Phishing, robo de credenciales.

## 3. MITM (Man-in-the-Middle)
- 🧪 Método: Interceptar y posiblemente modificar la comunicación entre dos partes.
- 💥 Consecuencia: Pérdida de confidencialidad, integridad.
- 🎯 Objetivo: Espiar, modificar datos, robar información.

## 4. XSS (Cross Site Scripting)
- 🧪 Método: Inyección de scripts maliciosos en páginas web.
- 💥 Consecuencia: Robo de cookies, secuestro de sesiones.
- 🎯 Objetivo: Acceso no autorizado a cuentas, manipulación de contenido.

## 5. SQL Injection
- 🧪 Método: Inyección de comandos SQL en formularios web.
- 💥 Consecuencia: Acceso, modificación o eliminación de datos de bases de datos.
- 🎯 Objetivo: Control de bases de datos, escalación de privilegios.

## 6. Brute Force Attack
- 🧪 Método: Prueba masiva de combinaciones de contraseñas.
- 💥 Consecuencia: Acceso no autorizado a cuentas.
- 🎯 Objetivo: Obtener credenciales válidas.

## 7. Password Cracking (Hashcat, John)
- 🧪 Método: Ataques a hashes de contraseñas mediante diccionarios o fuerza bruta.
- 💥 Consecuencia: Descifrado de contraseñas.
- 🎯 Objetivo: Obtener acceso a sistemas protegidos.

## 8. Phishing
- 🧪 Método: Suplantación de identidad mediante correos o páginas falsas.
- 💥 Consecuencia: Robo de credenciales o datos personales.
- 🎯 Objetivo: Engañar al usuario para obtener acceso.

## 9. Keylogger
- 🧪 Método: Registro oculto de teclas presionadas por el usuario.
- 💥 Consecuencia: Robo de contraseñas, información sensible.
- 🎯 Objetivo: Vigilancia o robo de datos.

## 10. Directory Traversal
- 🧪 Método: Manipulación de rutas de archivos mediante `../`.
- 💥 Consecuencia: Acceso a archivos del sistema fuera del directorio permitido.
- 🎯 Objetivo: Explotar configuraciones inseguras.

## 11. Remote Code Execution (RCE)
- 🧪 Método: Inyección y ejecución de código remoto en el servidor.
- 💥 Consecuencia: Compromiso completo del sistema.
- 🎯 Objetivo: Toma de control, persistencia.

## 12. CSRF (Cross Site Request Forgery)
- 🧪 Método: Envío de peticiones maliciosas desde navegadores autenticados.
- 💥 Consecuencia: Acciones no autorizadas realizadas por el usuario.
- 🎯 Objetivo: Explotar la confianza de un sitio en el navegador del usuario.

## 13. Reverse Shell
- 🧪 Método: El atacante obtiene una conexión de vuelta desde la víctima.
- 💥 Consecuencia: Control remoto del sistema afectado.
- 🎯 Objetivo: Interacción directa con el sistema objetivo.

## 14. Buffer Overflow
- 🧪 Método: Desbordamiento de un buffer para sobrescribir memoria adyacente.
- 💥 Consecuencia: Ejecución de código arbitrario.
- 🎯 Objetivo: Obtener acceso o escalar privilegios.

## 15. OSINT (Open Source Intelligence)
- 🧪 Método: Recolección de información pública (Google, redes, dominios).
- 💥 Consecuencia: Reconocimiento previo a un ataque.
- 🎯 Objetivo: Construir un perfil del objetivo, encontrar debilidades.

## 16. Social Engineering
- 🧪 Método: Manipulación psicológica para obtener información.
- 💥 Consecuencia: Divulgación no autorizada de credenciales o acceso físico.
- 🎯 Objetivo: Comprometer sistemas sin técnicas técnicas.

