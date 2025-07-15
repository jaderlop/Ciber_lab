## Intro security info

La seguridad ofensiva consisten en entrar dentro de sisitemas informaticos aprovechandonos de bugs o loopholes que esten en las aplicaciones y nos permitan ganar acceso sin autorizacion

un paso como al ingresar a un sistema es usar una herramienta llamada **dirb**
<dirb http://"paginapagina.com">

## Defensive security into

Consiste en mantener a salvo un cistema informatico, de intrusos no deseados para ello las tareas de un Blue team son:
- **Concientizacion de los riesgos ciberneticos**
- **Documentacion y gestion de activos** 
- **Actualizacion y correcion en errores del sistema**
- **Configuracion de sistemas de seguridad preventivos:** firewall, IPS
- **Configuracion de equipos de registro y monitoreos**

**Topicos relacionados**
- Security operations center (SOC)
- Threat Intelligence
- Digital Forensic and incident Response (DFIR)
- Malware analysis

## Security operations center (SOC)

son los profesionales con la responsabilidad de monitoriar la red y cervicios en busca de intrusos, o detectar eventtos maliciosos algunas areas de interes del SOC son:
- **Vulnerabilities** = Cualquier sistema es vulnerable, lo importante es ecntrar esta volnerablidad y arreglar ya sea usando los paquetes actualizados necesario, una vez detectada una volnerabilidad lo urgente es arreglarla cuanto antes para mitigar los daños, aunque esto es vital para el SOC, no necesariamente es asignado a el.
- **Policy violation** = Son las reglas definidas para proteger un sistema y definir amenzas, por ejemplo no conectar USB extrañas o un trabajador que carga informacion de los empleadores a un sitio de ventas en internet
- **Unathorized activite** = Esto se puede dar cuando las credenciales de algun miembro del equipo han sido robadas, o dadas de baja, la deteccion de esta actividad podria ser considerada como sospechosa y es perentorio mitigarla antes de que pueda hacer mas daños
- **Network instrusions** = No importa que tan buena se la seguridad si un compañero da click en un enlace raro o un atacante explota un servicio publico, estas intruciones deben ser detectadas cuanto antes para mitigar los daños

El SOC cubre varias tareas para asegurar la proteccion de los sitemas una de ellas es *threat inteligence* la inteligencia de amenazas

**Threat inteligence**
En este contexto la inteligencia es la recoleccion de informacion que puede obtener el enemigo y los daños vendria a ser cualquier accion que interrumpa o rompa el sistema, la inteligencia de amenaza recolecta informacion que ayuda a la compañia a estar mejor preparada frente a un posible enemigo, desde uno que pueda detener su sistema de facturacion o secuestra sus datos

La inteligencia de amenzas necesita recoger informacion, procesar la informacion y analizar, esta informacion puede ser obtenida desde diferentes fuentes ya sea la red propia, foros de internet o registros de red, esto nos brindaria informacion sobre los motivos que tienen los posibles atacantes y por donde podrian abordarnos

## Digital Forensics and Incident Response (DFIR)

### Digital forensic
La ciencia forence se basa en la reconstruccion de los hechos durante un incidente, en el ambito digital se utilizara para determinar como ocurrio un ataque, que daño, y que evidencias queda, puede investigar echos como una violacion a las politicas de privacidad, accesos no autorizados, ransomware o exfiltracion de datos para ello el **digital forensinc** se puede enfocar en diferentes areas

- ***file System:*** Es la revision de bajo nivel de los ficheros  o directorios del sistema, ver si fueron creadas copias, se reescribieron algunos ficheros o se eliminaron estos mismos
- ***System memory*** Si los atacante ejecturan un programa malisioso en el sistema, o hay evidencia de actividad sospechosa que no queda guardada en disco se podria detectar en tiempo real cono una revision a la memoria del sistema
- ***System logs***  Estos ficheros contienen informacion de que es lo que esta sucediendo dentro del sistema, proveen informacion clave para entender que ocurre incluso si el atacante intenta borrar sus rastros, quedarian algunas huellas
- ***Network logs*** Revisar los registros de paquetes podria a ayudar a dectectar si esta ocurriendo un ataque, que conexiones hubo y esto que implicaciones tiene

### Incident response 
No todas las alertas son graves o critacas puede ser una mala configuracion, o un intento de intrucion o puede ser un ***Cyber attack*** que nos prive del ingreso al sistema, romma un servicio web o secuetre nuestra informacion, el ***Incident responce** Es una etapa vital para entender y saber que hacer antes, durante y depues de un ataque o intento de daño, esto es vital para mitigar los riesgo en la medida de los posible y mientras mas rapido sea mejor, se puede mapear en cuatro etapas

- ***Preparation*** Esto requiere un equipo entrenao y listo para saber como manejar un incidente, es ideal tene varias medidas antes de que un incidete tenga lugar en primer lugar

- ***Detection and analysis*** El equipo debe de estar listo y tener los recursos necesario para detectar cualquier incidente, es esencial para identificar el tipo de incidente y su gravedad

- ***Containment, eradication and recovery*** Una ves el inicidente fue detctado, es crucial detenerlo para que no afecte otros sistemas, eliminarlo y recuperar los sistemas infectados, por ejemplo una vez detectamos la infeccion del sistema con un virus este debe de ser detenido, antes de que infecte otros sistemas, se elimina el virus y se garantiza la adecuada recuperacion del sistema

- ***Post incident*** Despues de una recuperaccion exitosa y generar un reporte de lo sucedido hay que preguntarse que leccion aprendimos para evitar casos similares en un futuro

![Procesos claves en una respuesta de incidentes](imag/incident_response_process.png)

### Malware analysis
un malware se refiere a un software malicioso, ya sea una pieza de programa, un documento o un fichero que puede ser guardado en un diso o enviado por la red, los malware incluyen varios tipos como:

- **Virus** Es una piesa de codigo que se adjunta a un programa, esta diseñado para pasar de un computador a otro, alterando, sobre escribiendo programas o borrando documentos, sus consecuencias van desde hacer lento un computador o dejarlo inutilizable

- **Trojan hourse** Es un Programa que a simple vista parase util o deseable, pero que en el fondo oculta una funcion maliciosa, por ejemplo una victima puiede descargarse un videojuego o una pelicula de un sitio web dudoso, esta descarga podria darle total acceso a un atacante

- **Ransomware** Es un programa malicioso que secuestra la informacion de un sistema encriptandola solo pudiendo leerla con una clave que el atacante tiene, este atacante puede ofrecer la llave a cambio de un pago

El ***Malware Analysis*** busca aprender sobre como funcionan los virus usando diferentes medios:

- ***Static Analysis*** Inpeccionando los binarios del programa sin tener que ejecutar, requiere una gran conocimiento acerca del legunaje ***Assembly*** 
    - **Herramientas comunes**: strings, objdump, IDA Pro, Ghidra

- ***Dynamic analysis*** se emplea ejecutando programas en entornos controlados y seguros para monitorear la actividades del virus como por ejemplo usando una sand-box
    - **Herramientas comunes**: Cuckoo Sandbox, Procmon, Wireshark, Regshot

## Securitu Analyst
Es un profesional responsable de proteger los activos digitales de una empresa sus funciones principales son **Monitorear detectar y responder amenzas de seguridad**

**habilidades:**
- Conocimiento en redes y sistemas
- Interpretacion de logs, alertas y anomalias
- Comunicacion efectiva con otros equipos tecnicos

**Lecturas recomendadas**
- [ ]  https://tryhackme.com/careers/cyber-security-analyst             
- [ ]  https://tryhackme.com/resources/blog/become-level-1-soc-analyst  
- [ ]  https://tryhackme.com/resources/blog/interview-with-soc-analyst  
- [ ]  https://tryhackme.com/resources/blog/soc-analyst-interview-guide 
- [ ]  https://tryhackme.com/resources/blog/haydens-success-story       
S
## Security Engineers
Profesionales encargados de implementar soluciones de seguridad a los activos digitales de una empresa y proteger la informacion vulnerable, ya sea de amenazas de red, ataques a aplicaciones web, a daptandose a las ultimas amenazas, su objetivo principal es retener y adoptar medidas de seguridad para mitigar los riesgos y el robo de informacion
**Habilidades**
- Redes (TCP/IP, DNS, routing, VLANs)
- Sistemas operativos (Linux, Windows)
- Seguridad en la nube (AWS, Azure, GCP)
- Automatización con Python, Bash o herramientas como Terraform
- Herramientas como:
    - Snort, Suricata, Zeek
    - SIEMs (Splunk, ELK)
    - Firewalls, EDR, WAF

**Lecturas recomendadas**
- [ ]  https://tryhackme.com/careers/security-engineer                        
- [ ]  https://tryhackme.com/resources/blog/become-security-engineer           
- [ ]  https://tryhackme.com/resources/blog/interview-with-security-engineer   
- [ ]  https://tryhackme.com/resources/blog/security-engineer-interview-guide  
- [ ]  https://tryhackme.com/resources/blog/richard-success-story              

## Incident responders
Profsionales en cargados de generan planes, politicas y protocolos durante y despues de un incidente, son miembros con una alta son claves en un equipo de seguridad y su actuar debe de ser inmediato para mitigar riesgos, usan metricas como MTTD (Mean Time to Detect), MTTA (Mean Time to Acknowledge) Y MTTR (Mean Time to Recover) Estas metricas ayudan a identificar cuan rapido y eficiente reacciona la organizacion ante una amenza

## Digital forensics
Profesionales en cargados de revisar los registros del sistema y entender que fue lo que sucedio, como sucedio y quien estuvo involucrado realmente

## Malware analyts
Entender como actual un malware y que impicaciones tiene este es de las principales funciones del profesional, requiere un alto conocimiento en sistemas y programasion sobretodo a bajo nivel como **assembly** o **C**
generando reportes para compartir con las partes interesadas

## Penetration tester
Este profesional es el encargado de evaluar la seguirdad de sistemas, redes y aplicaciones de una organizacion simulando ataques reales, con el fin de detectar vulnerabildades antes de que lo haga un ente malicioso

**Lecturas recomendadas**
- [ ]  https://tryhackme.com/careers/penetration-tester
- [ ]  https://tryhackme.com/resources/blog/how-to-become-a-penetration-tester
- [ ]  https://tryhackme.com/resources/blog/jr-pentester-interview-guide
- [ ]  https://tryhackme.com/resources/blog/tom-success-story

## Red teamer
Tiene responsabilidades similares a las de ***Penetration tester*** solo que con mas objetivos especificos para cada rol, los **Pentesters** buscan descubrir muchas vulnerabilidades de la empresa para mantener un la ciberseguridad en buenas condiciones, mientras que el ***Red team*** se encarga de probar las capacidades de, detecion y respuesta de la mepresa, esta area requiere imitar las acciones de los ciber criminales, emular ataques maliciosos, mantener acceso y evadir detecciones, pueden trabajar por un periodod de tiempo definido, por lo general son subcontrados por otras empreas o organizaciones que ofrecen estos servicios

- **Lecturas recomendadas:**
- [ ]  https://tryhackme.com/resources/blog/red-teaming-jobs-salaries-opportunities

## Que es Networking 
ElNetworiking es conexion, se puede ver en diferentes aspectos de la vida, desde el transporte publico, el servicio de mensajeria, el sistema electrico o de acueducto, en computacion es la misma idea solo que con componentes informaticos

![Networking](imag/Networking.png)

## Que es el internet
El internet es una red global que interconecta millones de redes privadas, publicas, academicas, corportativas y gubernamentales, surge apartir del neteworking ya que el internet conecta diferntes redes sin importar su ubicacion fisica indentificandolos con **etiquetas**

![Internet](imag/internet.png)

## Identificacion de equipos en una red

En el mundo real para saber con quien hablamos y poder identificarlos podemso usar dos cosas, su nombre y sus huellas dactilares, con los dispositivos es igual, solo que con ellos usamos:
- Dierccion IP
- Direccion MAC (Numero de serie del dispositivo)

### Direccion IP
ip (Internt Protocol) brevemente es un protocolo de internet que sirve para indetificar y que los dipositivos se identifiquen entre si, un equipo (host) en una red ya sea un servidor, una camara de seguridad o un reloj inteligente, esta ip se conpone por 4 octetos, cada uno va desde el 0 al 255

![IP](imag/IP.png)

IPv4 nos brinda una capacida 2^32 (4.29 billones) de direcciones IP, conforme ah pasado el tiempo y mas dispositivos se han concetado se ah creado una nueva version del protocolo IPv6 2^128 (340 trillion)

![IPv4 y IPv6](imag/ipv4-ipv6.png)

### Direccion MAC (Media Access Control)
Los dispositivos en la red tiene una direccion fisica la cual se encuentra en un microchip qye esta en la placa madre, esta interfaz asigna una direccion unica conocida como la direccion MAC, esta compuesta por 12 caracteres de numeros hexadecimales di vivdidales en 2 y separados por dos pundos ":" por ejemplo ***a4:c3:f0:85:ac:2d*** los primero seis caracteres represnta la empresa que los fabrico los ultimos seis es el numero unico

![MAC adress](imag/MAC_adress.png)

Algo importante a recalcar es que esta direccion mac puede ser falsificada en un proceso conocido como spoofed, rompiendo asi protocolos de seguridad ya que si una red confia en direcciones MAC para autorizar accesos puede ser engañada si un atacante suplanta una direccion confiable

## PING
Ping es una de la principales herramienta para usar ren redes, Ping usa **ICMP** (**I**nternet **C**ontrol **M**essage **P**rotocol) con esto se puede determinar el comportamiento de la conexion entre dos dispositivos, por ejemplo si esta conexion existe, es segura, su tiempo de latencia y detectar perdida de paquetes o fallas de conexion











