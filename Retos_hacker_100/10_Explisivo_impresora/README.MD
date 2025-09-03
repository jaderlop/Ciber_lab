ip_victima = 192.168.0.200
ip_atacante = 192.168.0.155

PROYECTO: Hacking Ético a Impresora **Brother MFC-L8900CDW**
OBJETIVO: Acceder al sistema de impresion para recrear archivos, obtener control y documentar el proceso.

ETAPAS DEL PENTEST:
1. Reconocimiento (pasivo)
2. Escaneo y enumeración
3. Explotacion
4. Escalada de privilegios
5. Persistencia (opcional)
6. Exfiltracion de datos
7. Limpieza de huellas (opcional)
8. Reporte tecnico

## Reconocimiento pasivo (Recon / pasivo)
- IP = 192.168.0.200
- MASCARA = 255.255.255.0
- SUBRED = 192.168.0.0/24
- MAC = E8:9E:B4:4B:31:C3
- FABRICANTE = Hon Hai Precision Ind. Co.,Ltd.

## Escaneo y enumeracion activa
- **whatweb http://192.168.0.200** = me muestra las tecnologias que usa la web
- **gobuster dir -u http://192.168.0.200 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x php,html,txt -t 30** = prueba de enumeracion de rutas web 

**no descartar los resultados que te dan 403,301 o 302 que son directorios que igual tienen acceso restrigido**

ruta encontrada / defecto = http://192.168.0.200/general/status.html

el formulario del loggin esta presente, lo que sugiere que tenemnos una vista como invital y el sistema no protege algunas rutas internas buscaremos hacer un reconocimiento parcial si identificarnos



Sí, la ruta es el login. Tu ataque puede venir por:

Vía	Técnica ofensiva
HTML + HTTP	Interceptar credenciales (Wireshark, Burp Suite)
JavaScript	Descubrir rutas, lógicas vulnerables, hardcodeos
Login	Fuerza bruta / SQLi / credenciales por defecto
URLs ocultas	Fuzzing (gobuster)
Backdoors	Exploits conocidos (CVE)

general/
general/status.html
general/log.html
general/info.html
maintenance/
admin/
admin/config.html
print/
jobs/
network/

uso de gobuster - u