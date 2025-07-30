## Tabla de contenido
- [Que es una red](#que-es-una-red)
- [Tipos de redes](#tipos-de-redes)
- [Topologias de red](#topologias-de-red)
- [Patrones de distribucion de trafico](#patrones-de-distribucion-de-trafico)
- [Que es una IP](#que-es-una-ip)
- [Que es una mascara de subred](#que-es-una-mascara-de-subred)
- [Que es una direccion MAC (Media Access Control)](#que-es-una-direccion-mac-media-access-control)
- [Modelo OSI](#modelo-osi)
- [Componentes del hardware de una red](#componentes-del-hardware-de-una-red)
- [Que es un puerto?](#que-es-un-puerto)
- [Que es un protocolo](#que-es-un-protocolo)
- [Que es un servicio](#que-es-un-servicio)
- [Puertos comunes asociados a servicios](#puertos-comunes-asociados-a-servicios)
- [Que es y como funciona el protocolo ARP](#que-es-y-como-funciona-el-protocolo-arp)
- [Que es y como funciona el protocolo DHCP](#que-es-y-como-funciona-el-protocolo-dhcp)
- [Que es y como funciona el protoclo DNS](#que-es-y-como-funciona-el-protoclo-dns)
- [Que es y como funciona el protocolo ICMP y explicacion del TTL](#que-es-y-como-funciona-el-protocolo-icmp-y-explicacion-del-ttl)
- [Que es y como funciona el protocolo TCP](#que-es-y-como-funciona-el-protocolo-tcp)

## Que es una Red
Es una estructura compuesta por varios nodos, los nodos pueden ser diferentes dispositivos que intercambian comunicacion entre si, el intercambio de informacion se hace mediante "canales" los cuales pueden ser fisicos como cables de cobre o fibra optica, y caneles inalambricos que usan tecnologias como wifi, lifi o bluetooh ***La finalidad de toda red es compartir informacion, ficheros, directorios o dispositivos de hardwere*** facilitando asi al comunicacion entre dispositivos o personas

Existen redes diferentes desde las de uso domestico, academico o gubernamental, las redes se comunican enviando datos dentro de "paquetes" ***Unidades discretas de informacion*** desde un dispositivo a otro siguiendo diferentes protocolos como **IP** **TCP** **UDP**

## Tipos de redes
Las rede se pueden dividir en abse a su alcance y los usuarios que puede impactar existen las redes
- **LAN:** Local Arean Netework, red pequeña que podemos encontrar en nuestros hogares o empresas, perfectas para gestionarse mejor

- **WAN:** Wide Area Network, Esta red interconecta ciudades o paises ***Internet*** pudiendo conectar muchas redes LAN

- **MAN:** Metropolitan Area Network, red de tamaño intermedio que puede cubrir una ciudad entera pero no intercomunicar paises como una red WAN

- **PAN:** Personal Area Network Tipo de red mas pequeño posible donde mis dispositivos se pueden conectar entre si

- **VPN** Virtual Private Network Se puede pensar como un canal seguro por donde se envian los datos un lugar apartado de el envio de paquetes publicos, cambaido tu direccion IP o sifrado de trafico
 
## Topologias de red
Describe como se organizan o conectan los dispositovos en una red, ya sea de forma fisica o logica donde se describen como los datos fluyen dentro de la red, algunas de estas topologias son:
- BUS: Todos los dispositvos estan conectados a un cable central, es mas riesgosa ya que depende de un clable si este falla todo cae
- ESTRELLA: Todos los dispositivos estan conectados a un hub o swithc, es la topologia mas comun actualmente si un dispositivo falla no afecta al resto
- ANILLO: La informacion pasan de un dispositivo a otro en una unica direccion formando un anillo cerra, si un dispositivo se rompe se puede perder la conexion a la red
- MALLA: Todos los dispositivos estan conectados entre si, soluciona el problema de que si se pierde un host la comunicacion no se interrumpe muy confiable costosa de implementar pero tiene tolerancia a fallos
- ARBOL: Variante de la topologia de estrella ya que combina varias de estas topologias en una estructura gerarquica permitiendo segmentarlas por zonas o departamentos, muy usada en redes empresariales o campus

## Patrones de distribucion de trafico
Describen como se transmiten los datos entre los dispositivos de una red

- Unicast: Un solo emisor le envia los datos a un solo receptor 1 a 1
- Broadcast: Se envian los datos a todos los dispositivos en una red, util para configura y analizar redes
- Multicast: Se envian los datos a un grupo especifico de dispositivos en especifico 
- Loopback: Nos permite enviarnos paquetes a nosotros mismos usando la ip, util para hacer pruebas en local
- Anycast: Varios dispositivos comparten la misma direccion IP pero solo la recibe el dispoditivo mas cercano
- GeoCast: Similar a el Anycast que envian la informacion a los dispositivos de un area determinada
- Peer to peer (p2p): Comunicacion directa entre dos dispositivos la diferencia entre esta red y una unicast es que en la unicast solo hay un unico emisor y un unico receptor en la red p2p los dispositivos actuan como clientes y servidores al mismo tiempo, sin necesdidad de un servidor central
- Point to multipoint(p2mp) un unico emisor transmite a multiplics receptores

## Que es una IP 
IP significa **Internet Protocol**, consiste en la asignacion de un unico numero identificador dentro de una red, tambien permite saber su ubicacion dentro de la red para enviarle informaicon, la direccion IP pueden ser:
- Estatica: que no cambia se configura manualmente
- Dinamica: Se asignan manualmente y si pueden cambiar
***Una IP dentro de una misma red no se puede repir ya que habria confusion y la informacion no sabria a donde ir, la IP se podria repetir dentro de una red aparte ya que no habria una comunicacion directa con el otro dispositivo que comparte la misma IP***

## Que es una mascara de subred
Una mascara de subred es un numero en la direccion IP que actua como filtro para separar la direcion IP en dos partes:
- la direccion de la red ( a que red pertenece)
- La parte de host (dispositivo especifico dentro de la red)
Una direccion IP esta compuesta por 4 octetos, y cada uno de estos puede tomar valores desde el 0 hasta el 255, la mascara de subred indica cuantos bits pertenecen a la red y cuantos al host, por ejemplo.
- IP: 192.168.100.10
- Mascara: 255.255.255.0
Esto quiere decir que los primeros tres octetos (192.168.1) son la direccion de la red, el ultimo octeto identifica el host de esa red (.10)
***las direcciones IP que puedo obtener de esa mascara son desde 192.168.100.1 hasta la 192.168.100.254***

## Que es una direccion MAC (Media Access Control)
Es un identificador unico asignado por el fabricante del dispositivo, esta direccion esta grabada a nivel del hardaware, a nivel de software si se puede cambiar mediante un proceso conocido como MAC spoofing

## Modelo OSI
Siglas de Open Systems Interconnection, es un marco de referencia creado por la  ISO  dividido por 7 capas, cuando enviamos un mensaje, este mensaje pasa por esta 7 capas:
- capa 1: Nivel fisico: Transmision y recepcion de datos, ya sea por medio fisicos
- capa 2: Nivel enlace de datos: Se asegura que los mensajes se envie sin errores para los dispositivos que lo van a recibir
- capa 3: Nivel de red: Gestiona la ruta mas eficiente para que el mensaje llegue a su destino
- capa 4: Nivel de transporte: Segmentacion de informacion para facilitar su envio aqui trabajan protocolos como **TCP** (Fible) **UDP** (Rapido pero no confiable)
- capa 5: Nivel de sesion: Se administra que las sesiones sean correctas y el mensaje haya llegado a su destino correcto
- capa 6: Nivel de presentacion: Ayuda a la representacion de los datos y la informacion sea entregada pueda ser entendida por el receptor
- capa 7: Nivel de aplicacion: Donde reside la interfaz del usuario final

### Capa fisica (1) del modelo OSI
Capa fundamental para el envio de datos binarios "0" o "1",En esta capa se convierten las señales digitales en señales fisicas, ya sean electricas, opticas o electromagneitcas esto depende del medio de transmision, los dispositivos que operan en esta capa son fisicos, como rutes, hub o swithch, lo importante de esta capa es la modulacion, la transformacin de los bits, en señales y fisicas y la retransformacion de estas señales en bits

### Capa de enlace de datos (2) modelo OSI
Los datos aqui se organizan en "tramas",se detectan fallos y corrige errores, aqui se introducen las direcciones MAC del emisor y receptor tambien nos encotramos la segmentacion y reensamblaje de informacion, "se envia un paquete grande en paquetes mas pequeños", podemos encontra el concepto del control de flujo, donde se asegura de que el emisor no sobre cargue al receptor con demasiados datos 

### Capa de red (3) modelo OSI
Aqui se introduce el "enrutamiento" encargado de dirigir los paquetes de datos desde el origen hasta su destino, las tramas se encapsulan en paquetes, se asigna direcciones IP de origen y destino para que los datos puedan cruzar multiples redes, se decide la mejor ruta posible para el envio de paquetes y se pueden fragmentar los paquetes si la red intermedia no soporta el tamaño origina del paquete, los paquetes se enrutan salot a salto (hop by hop)

### Capa de Transporte (4) modelo OSI
Capa encargada de que los paquetes sean entregdos correctamente los paquetes se convierten en segmentos si se usa el protoclo TCP o data gramas si se usa el protocolo UDP, aqui los protocolos fundamentales son TCP y UDP
- TCP: Conexiones con orden, fiabilidad  y estabilidad
- UDP: Conexiones priorizando la velocidad si n importar la calidad de lainformacion

### Capa de sesion (5) modelo OSI
Aqui se establecen, se gestionan y se terminan la sesiones de comunicacion entre aplicaciones de dispositivos diferentes, puede inseratar puntos de control, por si hay fallos la comunicacion pueda reanudarse desde un punto intermedio, cordina el inicio y cierre correcto de las sesiones entre aplicaciones

### Capa de presentacion (6) modelo OSI
Convierte los datos de forma tal que la red los pueda entender y sea adecuado en el destino, Se genera en esta capa el cifrado y desifrado, tanto para el remitente como para el destinatario, esta capa es vulnerable a taques relacionados con cifrados y formatos

### Capa de aplicacion (7) modelo OSI
Aqui recide toda la interaccion con el usuario final, capa del producto final de las anteriores capas, todo lo que el usuario hace o curre en la capa 7


## Componentes del hardware de una red
- Hub: Dispositivo baisco que envia la iformacion a todos los puertos, no distingue origen ni destino, actua como repetidor fisico, actua en la capa 1

- Switch: A diferencia del hub este dispositivo almacena las direcciones MAC de cada dispositivo en la red y lo envia al puerto correspondiente trabaja en la capa 2

- Acces point: Transmite y recibe señales inalambircas, tambien puede trabajar en la capa 2 al gestionar direcciones Mac

- Router: Division de redes, se encarga de encaminar los paquetes a su destino final, este hardware aplica en la ruta 3, los Router actuales ya contienen Switches y acces point en su interior

## Que es un puerto?
Un puerto es un canal de entrada y salida de datos para identificar servicios especificos en un host, los puertos van desde el 0 hasta el 65535 Se pueden dividir en 3 categorias
- 0 al 1023 (well-known ports) puertos bien conocidos asigando por la IANA
- 1024 al 49151 (Registered ports) son puerto que tienen mas facilidad
- 49152 al 65535 estos puertos suelen ser usado por algun servicio de forma temporal

## Que es un protocolo
Un protocolo de red define el formato y el orden de los mensajes a nivel de intercambio de dos o mas dispositivos, un protocolo establece las directrices por las cuales se rige la comunicacion los protocolos pueden actuar de diferentes capas del modelo OSI o del modelo TCP/IP dependiendo de su funcion especifica

## Que es un servicio
Un servicio es una funcion ofrecida por un dispositivo (sevidor) para otro dispositvo (cliente) atraves de la red, ya sea acceder a una web, a una impresora o sistema de striming

La mayoria de estos servicios se basan en una arquitectura cliente servidor, el cliente manda solicitudes a por medio de la red usando un protocolo por ejemplo http, y si el puerto de este servicio esta abierto mi peticio puede ingresar y brindarme un servicio

## Puertos comunes asociados a servicios
Los siguientes puertos han sido asignados para correr estos servicios por la IANA es una convencion util para mantener el orden, no es obligatorio seguirlos pero es parte de los estandares se ordenaron en el siguiente cuador de la siguiente manera numero de puerto = Servicio = Protocolo = Explicacion

- Puerto 21 = FTP (Control) = FTP = Comandos de control de transferencia
- Puerto 22 = SSH = SSH = Acceso remoto seguro por terminal
- Puerto 23 = Telnet = Telnet = Acceso remoto sin cifrado (inseguro)
- Puerto 25 = SMTP = SMTP = Envio de correos electronicos
- Puerto 53 = DNS = DNS = Resolucion de nombres de dominio
- Puerto 80 = HTTP = HTTP = Navegacion web sin cifrar
- Puerto 110 = POP3 = POP3 = Descarga de correos (cliente -> servidor)
- Puerto 135 = RPC = RPC = Llamadas a procesos remotos en Windows
- Puerto 139 = NetBIOS/SMB = NetBIOS/SMB = Comparticion de archivos en redes Windows
- Puerto 143 = IMAP = IMAP = Acceso remoto a correos (cliente <-> servidor)
- Puerto 161 = SNMP = SNMP = Monitoreo y gestion de dispositivos de red
- Puerto 443 = HTTPS = HTTPS (SSL/TLS) = Navegacion web segura
- Puerto 445 = SMB = SMB (Direct) = Comparticion de archivos moderna (sin NetBIOS)
- Puerto 465 = SMTPS = SMTP + SSL/TLS = Envio de correos cifrados
- Puerto 993 = IMAPS = IMAP + SSL/TLS = Acceso cifrado a correos
- Puerto 995 = POP3S = POP3 + SSL/TLS = Descarga segura de correos
- Puerto 1433 = Microsoft SQL = TDS = Conexión a base de datos SQL Server
- Puerto 3306 = MySQL = MySQL Protocol = Conexion a base de datos MySQL
- Puerto 5432 = PostgreSQL = PostgreSQL Protocol = Conexion a base de datos PostgreSQL
- Puerto 6379 = Redis = RESP = Base de datos NoSQL en memoria
- Puerto 27017 = MongoDB = BSON over TCP = Base de datos NoSQL tipo documento
- Puerto 3389 = RDP = RDP = Escritorio remoto (Windows)
- Puerto 9200 = Elasticsearch API = HTTP REST = Consultas y gestion de cluster Elasticsearch
Puerto 9300 = Elasticsearch Node = TCP internode = Comunicacion entre nodos de Elasticsearch

## Que es y como funciona el protocolo ARP
**ARP (Address Resolution Protocol)** protocolo que pertenece a la capa 2 del modelo OSI, este protocolo resuelbe direcciones IP a direcciones MAC en redes locales, Cuando un dispositivo(A) necesita comunicarce con otro en una red local y solo conoce su direccion IP, el dispositivo (A) envia una solicitud ARP en broadcast, el dispositivo (B) que tiene esa direccion IP responde con un ARP Replay, dindicando su direccion MAC la cual es guardada en una **tabla ARP** del emisor para futuros envios

Este protocolo no tiene una autentificacion de identidad y cualquier dispositivo podria enviar respuestas falsas, lo cuales permite ataque como **ARP spoofig** o **ARP poisoning**, donde un atacante engaña a los dispositvos para que crean que su direccion MAC es la del router o host legitimo facilitando ataque como **man in the middle**

## Que es y como funciona el protocolo DHCP 
Protocolo encargado de asignar direcciones IP a un Host evitando esta asignacion a los admnistrradores de configurar las IP manualmente, emplea un proceso llamado DORA
- Discover: El cliente busca servidores DHCP con un broadcast
- Offer: Los servidores DHCP ofrecen configuracion al cliente
- Request: El cliente solicita una configuracion especifica de un servidor
- Acknowledge: El servidor confirma y asigna la configuracion al cliente
Este protocolo solo actua con IP dinamicas por defecto pero se puede confiugara

DHCP no tiene autentificacion por defecto, por lo cual es vulnerable a ataques como:
- **Rogue DHCP**: Un atacante se hace pasar por servidor DHCP y entrega configuraciones maliciosas
- **DHCP Starvation**: Se agotan las IPs disponibles al enviar muchas solicitudes falsas desde direcciones MAC distintas.

## Que es y como funciona el protoclo DNS
Protocolo de nombre de asignacion de Dominios, "traduce" la URL a una direccion IP asociada con ese nombre de Dominio, Este protocolo opera siguiendo una gerarquia
1) Busca una cache local = sitios visitados antes, guardado por un tiempo definido
2) Busca en un ficher Host = Archivo local que puede ser definido manualmente
3) Busca en DN configurados provistos por el proveedor de internet = Consulta en un servidor DNS

El protocolo DNS por defecto **no está cifrado ni autenticado**, lo que permite ataques como:
- **DNS Spoofing** o **DNS Cache Poisoning**  
  El atacante inyecta respuestas falsas en la cache de un servidor DNS para redirigir al usuario a sitios falsos
- **DNS Hijacking**  
  Modificacion de la configuracion DNS (por malware o red comprometida) para que los dominios apunten a servidores controlados por el atacante.
- **Exfiltracion de datos por DNS**  
  En entornos restringidos, los atacantes pueden usar peticiones DNS para enviar informacion fuera de la red (DNS Tunneling).

## Que es y como funciona el protocolo ICMP y explicacion del TTL
Protocolo de control de envio de errores de mensajes en internet, util para el mantenimiento de Red, util para diagnositcar y reportar fallo en pruebas de conectividad por ejemplo. la comunicacion con un dispositvo por medio de un protoclo ICMP se genera en tres pasos
1) Generacion del mensaje ICMP por algun problema generado en la conexion
2) Encapsulamiento del mensaje ICMP usando la informacion basica del IP
3) Transmision del mensaje

**Como se genera** Se generan con el comando Ping, El cual genera un mensaje ICMP, lo encapsula y envia al destinatario, el mensaje es recivio y responde de vuelta, este proceso de envio es conocido como Echo Requests ICMP y el proceso de respuesta es conocido como Echo Reply ICMP 

**TTL (Time To Live)** es un valor dentro del encabezado IP que indica cuántos saltos (routers) puede atravesar un paquete antes de ser descartado. Cada vez que un paquete pasa por un router, su TTL disminuye en 1. Si llega a 0, el paquete se descarta y se devuelve un ICMP “Time Exceeded”.

un TTL de 64 esta asociado a dispositivos UNIX un TTL de 128 esta asignado a windows y uno de 255 a routers y switches, estos valores pueden variar

**Aunque es una herramienta útil, también puede usarse en ataques como:**
- **Ping of Death**: Envio de paquetes ICMP fragmentados maliciosamente que al unirse superan el tamaño permitido.
- **Smurf Attack**: Ataque DDoS donde una IP victima es suplantada en paquetes ICMP enviados a una red de broadcast.
- **ICMP Tunneling**: Usar ICMP como canal encubierto para exfiltracion de datos o bypass de firewalls.

## Que es y como funciona el protocolo TCP
El protocolo TCP (Protocolo de Control de Transmion) Es un protocolo fundamental en la comunicacion de redes garantizando la entrega congiable de datos entre aplicaciones establece y mantiene la conexion entre el emisor y el receptor durante el proceso de transferencia, algo propio de este protocolo es el **Three Way Handshake** lo cual vendria a ser una formalizacion para entablar una comunicacion
- SYN: El cliente inicia la conexión enviando un mensaje al servidor indicando que quiere establecer comunicación.
- SYN-ACK: El servidor responde aceptando la solicitud y proponiendo también su número de secuencia.
- ACK: El cliente confirma que recibió la respuesta del servidor. A partir de aquí, la comunicación está establecida y puede comenzar el intercambio de datos. 

























