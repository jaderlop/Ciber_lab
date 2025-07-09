# Linux para ciberseguridad

## Tabla de contenido

- [Que es un sistema operativo?](#que-es-un-sistema-operativo)
- [Que es el codigo abierto?](#que-es-el-codigo-abierto)
- [Que es una distribucion?](#que-es-una-distribucion)
- [Distribuciones basadas en otras](#distribuciones-basadas-en-otras)
- [Estructura de linux](#estructura-de-linux)
- [Componentes del sistema de ficheros](#componentes-del-sistema-de-ficheros)
- [Otros conceptos clave](#otros-conceptos-clave)
- [¿Que es un comando?](#¿que-es-un-comando)
- [Ficheros mas importantes en linux](#ficheros-mas-importantes-en-linux)
- [Principales directorios en linux](#principales-directorios-en-linux)
- [Variables de entorno](#variables-de-entorno)
- [Comandos de ayuda y soporte](#comandos-de-ayuda-y-soporte)
- [Rutas, rutas absolutas y relativas](#rutas-rutas-absolutas-y-relativas)
- [Diferencia entre parametros y argumentos](#diferencia-entre-parametros-y-argumentos)
- [Comandos de navegacion, gestion de ficheros y directorios](#comandos-de-navegacion-gestion-de-ficheros-y-directorios)
- [STDIN, STDOUT, STDERR](#stdin-stdout-stderr)
- [Comandos de gestion de usuarios](#comandos-de-gestion-de-usuarios)
- [Guia rapida para gestionar grupos y permisos](#guia-rapida-para-gestionar-grupos-y-permisos)
- [Permisos SUID Y SGID](#permisos-suid-y-sgid)
- [Permisos Sticky bit](#permisos-sticky-bit )
- [Permisos sudoers](#permisos-sudoers)
- [Comandos de genstion de grupos](#comandos-de-genstion-de-grupos)
- [Comandos de gesiton de paquetes](#comandos-de-gestion-de-paquetes)
- [Redes](#redes)
- [Comandos de gestion de redes](#comandos-de-gestion-de-redes)
- [Comandos de gestion de ficheros comprimidos](#comandos-de-gestion-de-ficheros-comprimidos)
- [Operadores logicos en linux](#operadores-logicos-en-linux)
- [Comandos de gestion de procesos](#comandos-de-gestion-de-procesos)
- [Redirecciones en linux](#redirecciones-en-linux)
- [Comandos de busqueda](#comandos-de-busqueda)
- [Editores de texto desde la terminal](#editores-de-texto-desde-la-terminal)
- [Comandos utiles](#comandos-utiles)
- [Atajos en linux](#editores-de-texto-desde-la-terminal)
- [Alias en linux](#alias-en-linux)
- [Bibliografia de comandos](#bibliografia-de-comandos)
- [Nota](#nota)

## Que es un sistema operativo?

Un sistema operativo o SO, es un conjunto de programas que gestionan los recursos de hardaware como la memori, el procesador los dispositovos de entrada y de salida. (de esto se encarga el kernel que viene a ser como el motor y esqueleto de un automovil lo que permite que todo funcione por dentro) el sistema operativo completo ademas del kernel, inclye los comandos, interfaces graficas, bibliotecas para hacer mas amigable lainteraccion con una maquina (el sistema operativo vien a se le volante, sillon, espejos y grenos de nuestro vehiculo permitiendo usarlo de forma comoda y controlada)

## Que es el codigo abierto?

El codigo abierto (Opens source) es un modelo de desarrollo de software basado en la colaboracion abierta,donde el codigo fuente es publico. Ampliando la participacion de terceros permitiendo que estos modifiquen el codigo fuente y compartan esta tecnologia,

## Que es una distribucion?

Una distribucion o distro es un conjunto de software especifico, incluido el sistema operativo ya compilado y configurado para su uso

***Imagen referencial de las distribuciones y su evolucion:*** https://wpollock.com/Unix/us__en_us__ibm100__linux__linux_timeline.pdf

***Informacion de los sistmas operativos y caracteristicas:*** https://archiveos.org/

***Principales cambios y actualizaciones de las distribuciones:*** https://distrowatch.com/

## Distribuciones basadas en otras

Si ya existe la rueda ¿para que re inventarla? lo mejor es usarla y mejorarla, con este pensamiento se parte de distribuciones base como (Debian o Ubuntu y se empiezan agregar o quitar funciones segun las necesidades del proyecto) gracias a esto existe una bifurcacion de distribuciones basadas en distros ya creadas que se adaptan a diferentes necesidades, educativos, empresariales, hacking, de rendimiento, etc.

## Estructura de linux

La estructura de linux se basa en una estructura gerarquica partiendo desde la raiz, en esta estructura todo se representa como un fichero desde: los archivos, los documentos, los dispositivos y procesos. ***Los ficheros almacena datos o configuraciones que influyen directamente en el comportamiento del sistema***. Los ficheros se pueden organizar en particiones, cada uno con su propio sistema de archivos

## Componentes del sistema de ficheros

En el nucleo del sistema de ficheros estan los INODOS, BLOQUES y SUPER BLOQUES

- **INODOS** = Guarda informacion o metadatos de un fichero como permisos, propietarios o tamaño que ocupa (no almacena el nombre del archivo solo su informacion) si los inodos no tienen referencia se pueden usar para guardar informacion de forma oculta no infalible ***inodos huerfanos***

- **BLOQUES** = Unidades de datos donde se guarda la informacion de los ficheros, donde se relacionan el nombre del fichero y numero de direccion del inodo (para saber a nivel de sistema que fichero esta dentro de que directorio)

- **SUPER BLOQUE** = Contiene la informacion crucial del sistema de ficheros, como el tamñano, numero de inodo estado del sistema de archivos, tipo de sistema de archivos (ext4)

## Otros conceptos clave

- *Fichero == Archivo*
- *Directorio == Carpeta*
- **Enlace duro(hard link)**: Referencia adicional al inodo de un archivo existente (Es muy util porque puedo acceder a un archivo desde una carpeta diferente)

- **Enalce blando(soft link)**: Referencia a una ruta o un fichero (Como un acceso directo una o una referencia a la ruta de otro archivo)

**PERMISOS:** Los permisos en linux se dividen en tres: 
- lectura(read): Ver contenido
- escritura(write): Modificar contenido
- ejecucion(Execute): Ejecutar al archivo o acceder a un directorio

Se pueden asignar estos permisos a tres tipos de usuarios dentro del sistema.
1) Propietario(u): Quien creo el fichero o directorio 
2) Grupo(g): Grupo al que pertence el propietario
3) Otros(o): Todos los demas usuarios

**Lo importante y critico son los permisos que tengo no la direccion en la que me encuentro para ejecutar comandos.**

***- Los permisos se asignan de forma octal o simbolica***

***- The quieter you become, the more you are able to hear*** 

## ¿Que es un comando?
Son instrucciones que es usuario envia al sistema operativo atraves de una shell, las cuales generalmente ejecutan un programa o una funcion interna, estos tambien pueden incluir argumento

## Shell vs emulador de terminal
**Emulador de terminal:** Interfaz grafiaca que permite la entrada y salida de texto, y sirve como entorno donde se ejecuta una shell

**Shell:** Interprete de los comandos que el usarion envia para que el sistema opertivo las ejecute ya sea un fragmento de codigo o una funcion

- sh(shell): Una de las primeras shell presente en casi todas las distribuciones.
- bash(Bourne again shell): Ampliamente usada en GNUlinux, Permite hacer scripting avanzado
- zsh: Shell moderna con autocompletado, resaltado y mayor interactividad

***El emulador de terminal el canal, La shell es el interprete, El sistema operativo es el ejecutor***

## Ficheros mas importantes en linux

- **/etc/passwd** = Contiene informacion basica de los usuarios del sistema (nombre,UID[identificador de usuario], GID[Identificador de grupo])
- **/etc/group** = Lista los grupos del sistema y los usuarios que pertenecen a ellos 
- **/etc/shadow** = Contraseñas de los usuarios encriptadas y configuracion de expiracion 
- **/etc/fstab** = Define como y donde montar las particiones al iniciar el sistema
- **/etc/network/interfaces** = Configura interfaces de red de forma manual
- **/etc/hostname** = nombre del host del sistema (nombre de la maquina)
- **/etc/resolv.conf** = Servidores DNS para traducir los nombres de dominio en otros sistemas con Ubuntu se gestiona con Netplan
- **~/.bash_history** = Guarda un historial de los comandos usados

## Principales directorios en linux

Hay directorios ocultos y estos empiezan con ./

- **/boot** = Informacion necesaria para el arranque del sistema (kernel,GRUB[GNU GRand Unified Bootloader])
- **/etc** = Ficheros de configuracion del sistema y aplicaciones
- **/var** = Datos variables: logs, correos, cache, colas de imprecion, etc
- **/var/log** = Contiene los logs del sistema como syslog, auth.log, etc
- **/usr** = Contine ficheros y directorios de uso general para los usuarios del sistema
- **/usr/bin** = Comandos y programas ejecutables para todos los usuarios
- **/usr/lib** = Librerias necesarias para ejecutar binarios
- **/home** = Directorios personales de cada usuarion no-root
- **/root** = Directorio personal del usuario root
- **/tmp** = Archivos temporales del sistema, descarga de aplicaciones, scripts se limpia al reiniciar
- **/dev** = representacion de dispositivos Fisicos [hardaware]
- **/sbin** = Ejecutables del sistema y recuperacion, usados por root para administrar

**Directorios delicados/especiales:** 

- **/procp** = Sistema de archivos virtual, expone informacion de procesos y kernel en tiempo real
- **/sys** = Hardaware del sistema, y control del hardware y del kernel
- **dev/null** = como una papalera de reciclaje, mas semejante a un agujero negro donde tirar las cosas
- **/etc/apt/soruces.list** = fichero de donde apt saca las rutas para la instalacion de paquetes o dependencias
- **/etc/apt/source.list.d** = fichero con rutas de otros deispositivos repositorios de terceros

***/etc configura, /usr ejecuta, /var registra, /dev conecta, /home guarda, /root manda, /proc revela.***

## Variables de entorno
son valores los cuales el sistema y progrmas usan para definir comportamientos, se guardan en memoria y afectan el comportamiento de SO

1) **echo $NOMBRE_VARIABLE** = conocer el contenido de una variable
2) **export VAIABLE=VALOR** = Creacion de una variable y asignacion de un valor
3) **export VARIABLE=NUEVO_VALOR** = Reasignacion de un valor a una variable
4) **unser VARIABLE** = Eliminacion de variable

- **env** = Enlista las variables
- **export** = Crreamos una variable
- **echo** = contenido de una variable
- **unset** = Eliminacion de una variable

***Variables importantes para el entorno:***

- **PATH** = Rutas donde se buscan los ejecutables
- **HOME** = Directorio ***Home*** del usuario
- **USER** = Nombre del usuario actual
- **SHELL** = Shell actual en uso
- **TERM** = Terminal actual en uso
- **EDITOR** = Editor de texto predeterminado

***Variables de entorno persisten***

Son aquellas variables que no se borran cuando se reinicia elsistema. **las variables que defino con export solo estan hasta que la sesion este abierta**

**¿Como hacer variables persistentes?**

Para ello debemos saber que Shell estamos usando podemo ver lo con **echo $SHELL** (o llendo al fichero /etc/passwd y buscar nuestro usuario con la informacion) una vez con esto claro, para crear variables persistente debemos registrarlas en el archio correspondiente de nuestra shell en este caso ***.bashrc*** que es un archivo oculto

1) Nano ~/bashrc
2) export NOMBRE_VARIABLE CONTENIDO
3) Guardamos las modificaciones con ctrl + 0, enter, ctrl + x
4) Recargamos el archivo source ~/bashrc

## Comandos de ayuda y soporte

Sirven para saber como funciona un comando, que parametros acepta y como utilizarlo correctamente

- man(manual): Muestra el manual completo del comando, dividido por secciones = **man ls**
- info: Muestra una documentacion mas extensa (si esta disponible) = **info ls**
- whatis: Da una descripcion breve del comando (una sola linea) = **whatis ls**
- --help: Casi todos los comando aceptan --help para una ayuda rapida el mismo comando nos dice como usarlo = **ls --helpls**
- apropos: busca en los manuales (man) cualquier concidencia con la palabra clave que le pasemos = **apropos "palabra_clave**[Es bastante similar a usar **man -k "palabra_clave**]
- whereis: nos da la ubicacion del binario y manulaes de un comando en especifico
- which: Busca ejecutables relacionados a un comando dentro de la variable de entorno PATH 

## Rutas, rutas absolutas y relativas
**Rutas:** Una ruta es una direccion que nos lleva a un fichero o directorio dentro del sistema de archivos la necesitaremos al movernos entre carpetas, ejecutar scripts o indicar archivos a los comandos

**Rutas absolutas:** Son las que empiezan desde la raiz "/" que es la primera barra, no confundir con los separadores "/" Que dividen los directorios. **Muestra todo el camino completo**

**Ruta relativa:** Empienza en el directorio donde nos encontramos, No empieza desde la raiz es util para trabajar dentro de proyectos o estructuras de carpetas profundas

***¿Cuando usar una relativa o una absoluta?*** Depende de la situacion, si estamos trabajando en un fichero que esta muy abajo de la gerarquia de carpetas y debemos usar un script o ver el contenido de un documento que esta en una carpeta con un orden superior de 1, osea por encima de nosotros lo mejor es usar una ruta relativa ../scripts/python1.py, ya que indicar una ruta absoluta nos conllevaria especificar todas las carpetas que estan desde la raiz hasta la que almacena el script.

Por otro lado si queremos un fichero o un script que esta cerca de la raiz es mas util usar una ruta absoluta ya que es mas directa que escribit ../../../../../../../../../home/Scripts/java.java

***Linux no distingue entre mayusculas, minusculas o espacios, hay que ser especifico***

- . = Directorio de trabajo actual
- ..= Directorio padre el que esta por encima donde nos encontramos
- ~= Directorio Home

## Diferencia entre parametros y argumentos
**Parametros:** Son las opciones que alteran el comportamiento de un comando se usa (-) con una letra o (--) con una palabra

**Argumentos:** Son los datos que el comando recibe para poder ejecutarse al rededor de ellos, o valores que la funcion necesita para funcionar correctamente

***El parametro modifica como se hace algo, el argumento dice sobre que se hace***

## Comandos de navegacion, gestion de ficheros y directorios

**Navegacion**
- cd = cambia de directorio
- pwd = directorio actual de trabajo
- ls = lista de ficheros y diretorios
    - ls -a = parametros ocultos
    - ls -l = formato largo
    - ls -r = recursivo

**Gestion de ficheros**
- touch = crea ficheros basicos
    - touch -a acceder a hora del fichero
    - touch -m constancia de modificacion del fichero
- cp = copia directorios y ficheros (cp "ruta_de_origen" "ruta_de_destino")
    - cp -r = copia la estructura interna de directoris del fichero
- mv = mover o renombrar ficheros o directorios (mv "ruta_de_origen" "ruta_de_destino")
    - mv "antiguo_nombre" "nuevo_nombre"
-rm = eliminar ficheros o directorios
    -rm -i = confirmacion
    -rm -r = directorios

**Gestion de ficheros**
- cat = ver contenido de ficheros, tambien puede concatenar el interios de los ficheros (cat fichero_1 fichero_2 > fichero_3)
- head = Muestra las primeras lineas de un fichero (head -n10 -> muestra las primeras 10 lineas)
- tail = Muestra las ultimas lineas de un fichero (tail -n10 -> muestra las ultimas 10 lineas)
- lees = Nos pagina un fichero, vemos el contenido de un fichero pagina por pagina

## STDIN, STDOUT, STDERR

- stdin = standar input es la entrada estandar de un programa por defecto el teclado **descriptor de archivos 0**

- stdout = stadar output salida estandar de un programa **descriptor de archivos 1**

- stderr = salida usada para mensajes de errores **descriptor de archivo 2** ls archivo_no_existente 2> error.txt
 
**Descriptor de archivo** = Son numeros que representan recursos de entrada y salida de archivos
es util para gestionar la respuesta del programa y almacenarla en archivos por ejemplo si al ejecutar un script queremos guardar su output error sabemos que este es 2 > Readme.txt o enviarla a /dev/null

## Comandos de gestion de usuarios

- **useradd** = agregar usuarios con opciones personalizada **forma tecnica** ejemplo ***sudo useradd -m -s /bin/bash nombre_usuario***[-m: crea el directorio. -s: especifica la shell predeterminada]
- **userdell** = eliminar usuarios del sistema ***ejemplo*** sudo userdel nombre_usuario
- **adduser** = **Interfaz amigable** para useradd con guia paso a paso, agregando la informacion al fichero /etc/
    - **passwd, crea el fichero, crea la contraseña y agrega inforamcion de contacto extra**
- **deluser**  = Forma **recomendada** para eliminar usuarios ***ejemplo sudo deluser --remove-home nombre_usuario*** con esto tambien eliminamos su directorio
- **whoami** = muestra el nombre del usuario actual
- **id** = Identfica informacion del usuario actual
- **finger** = Muestra detalles del usuario
- **usermod** = parametro que permite **modificar las caracteristicas de los usuarios** creados nombre, directorio home, grupo etc 
    1) sudo usermod -n nombre_nuevo nombre viejo = cambia el nombre
    2) sudo usermod -d /home/nombre_nuevo -m nombre_nuevo = cambian el home y mueve los archivos
    3) sudo usermod -g nuevo_grupo nombre_usuario = cambia le grupo primario
    4) sudo usermod -aG grupo_nombre usuario_nombre = agraga el usuario al grupo indicado

- **passwd** = Cambia la contraseaña del usuario
    - passwd -l = bloquea la contraseña
    - passwd -u = desbloquea contraseña

- **who** = Quien esta conectado al sistema (-u usarios conectados con su hora)
- **su** = Cambio de usuario dentro de la misma terminal
    - su -c "whoami" andres: me ejecutara este comando como andres aunque este en root
- **sudo** = ejecuta comando con privilegios
    - sudo -u andres whoami: Ejecuta este comando con sudo desde el perfil de andres
    - sudo -i: Inicia una shell como usuario root

## Guia rapida para gestionar grupos y permisos

**Permisos en linux**

En linux, cada archivo o directorio tiene un conjunto de permisos que controlan las accione que pueden tener los individuos sobre este, ya sea leero, ejecutarlo o escribirlo

**ls -l** = Lista los elementos del directorio y muestro los permisos

| Sección          | Descripción                              |
|------------------|------------------------------------------|
| Primer carácter  | Tipo de archivo (`-`, `d`, `l`)          |
| 1º grupo (`rwx`) | Permisos del **propietario**             |
| 2º grupo (`r-x`) | Permisos del **grupo**                   |
| 3º grupo (`r--`) | Permisos de **otros usuarios**           |

- como lo veriamos en terminal: -**rwx**r-x**r--**

**Significados del primer caracter**
- **-** = Indica que es un fichero regular
- **l** = Indica que es un enlace simbolico / blando
- **d** = Indica que es un directorio

**interpretacion de los permisos de cada grupo**
Apartir del primer caracter cada grupo se representa en conjuntos de 3, cada caracter puede ser
- **r** = Read(lectura)
- **w** = Write(Escritura)
- **x** = Execute(ejecucion)
- **-** = permiso no concedido

**Asignacion octal**
Los permisos se dividen en tes categorias propietario, grupo y otros cada permiso tiene un valor numerio
- **r** = Read(lectura) = 4
- **w** = Write(Escritura) = 2 
- **x** = Execute(ejecucion) = 1

para asignar los permisos se hacen sumanod los valores par acada categoria en especifico si solo queremos darle permisos de escritura(2) y ejecucion(1) a los propietarios sera ***chmod 300 archivo.txt *** solo se asigna a cada categoria en 

**sudo chown -R "usuario":"usuario /var/www/crud** = cambia el propietario de el directorio especificado

**CHMOD** = comando importante para otorgar permisos a usuarios y modificarlos

**sudo chown :developers /var/www/lab_test/dev_notes.txt** = Le entrega la propiedad del archivo especificado en la ruta absoluta al grupo o usuario especificado

**sudo chmod 770 /var/www/lab_test/dev_notes.txt** = le otorga todos los permisos al propietario, al grupo pero a otros usuairos no les da permisos

1) Como asiganar varios usuarios a un grupo == sudo usermod -aG "nombre_grupo" "nombre_usuario"

2) Hacer que un grupo sea propietario de un directorio / fichero == sudo chown :"nombre grupo" /"ruta directa del fichero/directorio"

3) otorgar permisos a los propietarios del fichero == sudo chmod 770 /"ruta directa del fichero/directorio"

4) que ocurre si un usuario que no esta en el grupo propietaro intenta acceder, leer o editar algo de del fichero == segun los permisos otorgados a los propietarios un usuario externo no deberia póder realizar ninfuna de estas acciones, obteniendo un permision denied

5) que ocurre si dentro del fichero comunal un propietario crea un fichero o directorio aparte == aun que este en un grupo donde todos pueden acceder si un propietario crea un docuemnto solo el podra accerder a este sin importar que se encuentre dentro de un grupo comunal

6) solo los usuarios autorizados como "sudoers" pueden usar el comando sudo

## Permisos SUID Y SGID
Estos tipos de permisos permiten a los usuarios ejecutar ficheros o comandos con los permisos que tengan el propietario o el grupo en cuestion 
- **SUID** = Set user ID = valor simbolico es **s** = 4 remplazando el **x** de executable del propietario
- **SGID** = Set gruop ID = valor simbolico es **s** = 2 remplazando el **x** de executable del grupo

## Permisos Sticky bit 
Es un permiso especial que aplica solamente para directorios compartidos, impide que otros suarios renombren o borreb ficheros, esto solo lo podria hacer el propietario del fichero o el usuario root
- Valor simbolico **t** 

## Permisos sudoers
Ficero sumamente sensible ya que si se compromete a un suario que se encuetntre definido en este fichero es muy facil la escalada de privilegios no modificar, sin saber que se va a hacer

## Comandos de genstion de grupos

- **addgroup** = permite crear grupos dentro del sistema operativo y agregarlos al fichero /etc/group:
    - addgruop "nombre_grupo" = addgroup empresa_1

- **delgroup** = Elimina el grupo indicado, para ello elgrupo debe de estar vacio sino no funciona
    - delgrup "nombre_grupo" = delgroup empresa_1

- **groupmod** = Permite cambiar aspectos del grupo es similar usermod
    - groupmod -n nuevo_nombre nombre_actual

- **gpasswd** = administrar contraseñas y mienbros de cada grupo
    - gpasswd grupo_interes = con esto cambio la contraseña = Cambia la contraseña de un grupo
    - gpasswd grupo_interes -a nuevo_usuario grupo_interes = Me agrega un usuario a un grupo
    - gpasswd grupo_interes -d eliminar_usuario grupo_interes = Elimina un usuario de un grupo

- **groups** = Consulta los grupos a los cuales pertenece el usuario
    1) groups = en que grupos esta el usuario que ejecuto el comando
    2) groups usuaro = en que grupos esta el usuario que pase como parametro

## Comandos de gestion de paquetes

- **Paquetes:** Coleccion de archivos que permite la instalacion de un programa y la configuracion inicial para que el programa funcione
- **Repositorio:** Almacen centralizdo donde se mantine los paquetes del software
- **Dependencia:** Parte del software que se requiere para que otro programa funcione

- apt = instalacion, actualizacion, eliminacion de paquetes y dependecias
    1) apt update = actualizar la lista de paquetes disponibles
    2) apt upgrade = Instala la lista de paquetes disponibles
    3) apt full-upgrade = Maneja tambien los cambios con las dependencias 
    4) apt install = ***apt install nombre_paquete -y*** instala el paquete en especifico que queremos
    5) apt remove  ***apt remove nombre_paquete -y*** desinstala el paquete en especifico que queremos
    6) apt auto-remove = ***apt auto-remove -y*** Elimina dependecias que ya no son necesarias

- dpkg = Gestiona paquetes de bajo nivel, en especifico .deb de debian es como apt pero mas tecnico
    1) dpkg -i ruta-absoluta-del-paquete.deb = instala un paquete en especifico [sudo dpgk -i paquete.dev]
    2) dpkg -l = Lista de todos los paquetes instalados en el sitema
    3) dpkg -r = Elimina paquetes (no elimina los archivos de configuracion)
    4) dpkg -P = Elimina el paqueta con todo y arcvhivos de configuracion
    5) dpkg-query --status locales = consulta a la base de datos de dpkg
    6) dpkg-reconfigure locales = util en la importacion de maquinas virtuales para reconfigurar paquetes instalados
    7) dpkg-trigger = util para activar eventos en el sistema de paquetes que se activen cuando parte cierta actualizacion

- apt-get = casi parecida a apt pero mas estable, dentro de los scripts
    1) apt-get dist-upgrade: Maneja de forma inteligente los cambios en nuevas dependencias de los paquetes es equivalente a apt full-upgrade

- apt-cache = busca y obtiene informacion de los paquetes en la cache de apt:
    1) apt-cache depends nombre_paquete = muestra las dependencias de este
    2) apt-cache policy nombre_paquete = Politica instalada de un paquete
 
## Redes

**Paginas de interes:** 
1) https://www.redeszone.net/tutoriales/redes-cable/comandos-basicos-redes-linux/
2) http://es.tldp.org/Manuales-LuCAS/GARL2/garl-2.0.pdf
3) https://www.tokioschool.com/noticias/interfaz-red/

**¿Que es una interfaz de red:** De forma reducida una interfaz de red es un punto de coneccion entre un dispositivo y una red, este punto (interfaz de red) puede ser fisico o virtual y tiene un papel muy importante **en la transferencia de datos** entre distintos dispositivos de una misma red.

Esta interfaz puede ser fisica como la coneccion de un disposito a un router o como las interfaces virtuales de un ordenador, decualquier medida esta configuracion es clave para la eficiencia de el intercambio de informacion de distintos dispositivos conectados a una red

Tenemos 2 tipos de nombres para las interfaces nombres tradicionales y nombres predictivos:

- **nombres tradicionales:** no son persistente, poco descriptivos (no indica ubicacion fisica o tipo de hardware de la nic)
- **Nombres predictivos:** son persistentes, y estan basados en la topologia de hardware o ubicacion

**NIC:** Tarjeta de interfaz de red

**Elementos esenciales en el diseño de una interfaz de red:** Cuando pensamos en diseñar una interfaz de red los aspectos mas importantes son:

1)**Ancho de banda:** Este elemento determina que volumen de datos se pueden transferir en un periodo de tiempo determinado, una red con un buen ancho de banda sirve para evitar cuellos de botella y garantizar una conexion eficiente y fiable

2)**Topologia de red:** Existen diferentes tipos de topologia de red y es fundamental escoger el adecuado para cada caso de diseño y configuracion ya sea decidir entre una red en estrella, malla o bus, es algo que puede afectar la eficiencia y fiabilidad de la interfaz
    
3)**Latencia:** Es el tiempo de retraso que hay en la transferencia de datos entre dos puntos de una red.

4)**Escalabilidad:** Cuando pensamos en interfaces de red tenemos que orientar el diseño a largo plazo, al futuro. si la configuracion actual necesita de un entorno de red pequeño, puede que en el futuro sea  necesario escalarlo

5)**Seguridad:** Es importante la incorporacion de firewalls y antivirus, actualizaciones de seguridad, incorporar autenticaciones seguras para el acceso a la interfaz y tambien realizar auditorias de seguridad regulares una vez que se haya implementado

**Protocolos comunes utilizdos en la interfaz de red**: Una vez diseñada la interfaz teniendo en cuenta los aspeoctos mas importantes hay que determinar que protocolos de red van a establecer las normas y el formato para el intercambio y la transferencia de datos. los mas comounes son:

1) **TCP/IP**: Estos protocolosa son la columna, el pilar sobre el que se sotiene internet se trata de un tipo de protocolo que da base a la mayoria de las comunicaciones en red y garantiza la transmision fiable de la  informacion

2) **UPD:** (User datagram protocol) es otro importante pero es menos fiable que TCP/IP ya que este se usa en aplicaciones donde prima la velocidad sobre la integridad de los datos

3) **HTTP/HTTPS:** Es lo esencia en la navegacion por internet ya que uno maneja la tranferencia de datos que no son seguros mientras que el otro cifra las comunicacciones.

4) **OSPF:** (Open Shortest Path First) Este protocolo de enrutamiento juega un papel clave en la eficiencia de la conectividad, especialmente en redes de gran tamaño. OSPF permite que los routers intercambien informacion sobre la topologia de la red y calculen la mejor ruta para  la transmision de datos.

**Una red mal optimizada puede traer muchos problemas**, buenas practicas son:
- monitorizacion constante del trafico de red para identificar cuellos de botella.
- tener todo actualizado para garantizar las ultimas mejoras en seguridad y rendimientos
- la segmentacion de red tambien facilita la gestion y la eficiencia de la misma
- el ancho de banda es importanticimo de igual manera para evitar cuellos de botella

## Comandos de gestion de redes

- **ifconfig** = Listado de las redes activas detalles como direccion ip, mascara subred, estadistica de paquetes
    - ifconfig (nombre de red) = informacion de es red en especifico
    - sudo ifconfig (nombre de interfaz de red) up = Activar red
    - sudo ifconfig (nombre de interfaz de red) down = Desactivar red
    - ifconfig (nombre de interfaz de red) direccion_ip = asignacion de direccion ip a una interfaz de red
- **ip** = Comando usado para mostrar y configurar, rutas, dispositivos y tuneles
    - ip a = interfaz de red con su direccion ip
    - ip route = Tabla de enrutamiento por donde viajan los paquetes
    - sudo ip route add direccion_red via puerta de enlace = añadir nueva ruta de enrutamiento 
- **netstat** = Muestra Tablas de enrutamiento, estadistica de interfaces, conecciones masquerales, miembros multicas 
    - netstat -t = muestra la conecciones por tcp
    - netstat -u = muestra las conecciones por udp
    - netstat -l = Muestra los puertos en escucha
    - netstat -p = Muestra el PID 
    - Netstat -e = Informacion estendida
- **ping** = Herramienta de diagnostico que nos permite ver la conectividad con otros host, se pueden enviar tanto ips, como dominios
    - ping -c# = cantidad de paquetes que podemos enviar al host o dominio
- **traceroute** = Herramienta que muestra la ruta que toman los paquetes hasta llegar al destino
    traceroute -m = numero maximo de saltos hasta de tener el ratro
- **nslookup** = Consulta a los DNS de los activos que tengamos
    nslookup -type = tipo de registro que queremos buscar
- **hostname** = Configura el nombre del sistema operativo esto igual esta en el fichere ***/etc/hostname***

## Comandos de gestion de ficheros comprimidos

- **tar** = se utiliza para archivar y comprimir archivos y directorios
    - tar -c = creacion de ficreo
    - tar -z = cracion de un zip para la compresion
    - tar -v = modo verbose que muestra los ficheros procesados
    - tar -f = muestra el fichero de salida
    - tar -x = descomprimir archivos
- **gzip** = para comprimir archiov individuales 
    -gzip -d "archivo_comprimido.zip" = descomprime un archivo
- **zip** = comprime ficheros y los convierte en punto zip ***zip nombre_fichero_comprimido nombre_del_fichero_a_comprimir***
- **unzip** = descomprime archivos .zip ***unzip ruta_absoluta_delficher.zip*** 

## Operadores logicos en linux
Permiten encadenar comando y controlar su ejecucion segun las condiciones de exito o fallo, especialmente untiles en scripts

- **&&** = Es similar al and en programacion, para que se ejecute el segundo tiene que haberse ejecutado el primero
- **||** = Es similar al or en programacion, si no se ejecuta el primer comando ejecuta el segundo, si se ejecuto el primero olvida el segundo
- **!** = Not en programacion
- **;** = Ejecucion seguida de comandos independientemente si se ejecutan bien o mal el primer comando
- **&** = Se envia un comando a segundo plano

## Comandos de gestion de procesos
Un procesos es una instancia de un programa que se esta ejecutando, un proceso requiere de recursos del sistema como: memoria, CPU y tiempo E/S cada proceso es identificado por un numero unico llamado **PID (process identifier**)

**Tipos de procesos**
- Procesos del usuario = Creados por el usuario (abrir un navegador, correr un script)
- Procesos del sistema = Servicios que mantien el sistema en funcionamiento (ej. systemd, crn, etc)

**Estados de los procesos:**
- Running = En ejecucion
- Sleeping = durmiendo 
- Stoped = detenido
- zombie = Terminado pero aun listado por el padre

- **PS** = Muestra informacion de los procesos activos
    - ps -a = procesos de todos los usuarios
    - ps -u = informacoin detallada del usuario
    - ps -x = ***procesos que no tienen una terminal asociado***
- **top** = liista real de los procesos en ejecucion y su consumo de recursos
- **kill** = le envia una señal a un procesos **kill "señal" "proces_id"
    - posibles señales a enviar:
        - **SIGHUP = Se usa para reiniciar procesos**
        - **SIGINT = Interrumpe un proceso equivale a CTRL + C en la terminal**
        - SIGQUIT = Sale del proceso y genera un volcado de memoria
        - SIGILL = Indica una instruccion ilegal
        - SIGTRAP = Señala una interrupcion anormal, usualmente por abortos
        - SIGBUS = Indica un error de bus, como un fallo de alineacion de memoria
        - SIGFPE = Reporta errores de punto flotante
        - **SIGKILL = Mata un proceso de inmediato y no puede ser ignorada**
        - SIGUSR1 Y SIGUSR2 = Señales definidas por el usuario
        - SIGSEGV = Indica violacion de segmento, como acceso a memoria no permitido
        - SIGPIPE = ocurre cuando un proceso escribe en un pipe sin lecotres
        - SIGALRM = Señal de alarma usada para temporizadores
        - **SIGTERM = señal de terminacion permite la finalizacion segura de procesos**
        - SIGSTKFLT = Indica desbordamiento de pila en coprocesadores
        - SIGCHLD = Envia un proceso cuando uno de sus procesos hijo termina
        - **SIGCONT = Continua un proceso que ha sido detenido**
        - **SIGSTOP = Detiene un procesos**
        - **SIGTSTP = Detecncion de proceso controlado por el teclado, similar al CTRL + Z**
        - SIGTTN y SIGTTOUT = Señales para manejo de entrada y salida en terminales
        - SIGURG = indica datos urgentes en socket
        - SIGXCPU = Limite de CPU excedido
        - SIGVTALRM Y SIGPROF = Señales para temporizadores y perfiles
        - SIGWNCH = camnio en el tamaño de la ventana del terminal
        - SIGIO = indica E / S asincrona
        - SIGPWR = Fallo de alimentacin
        -SIGSYS = Argimento de sistema incorrecto
- **killall** = Termina con todos los procesos ***killall "proceso"***

## Redirecciones en linux

Con linux podemos redirigir la salida(***stdout***) de un comando a un archivo en ves de mostrarla en pantalla:
- **>** = sobre esribo contenido ***echo "hola mundo" > saludo.txt***
- **>>** = Agrego contenido al final del fichero ***echo "adio mundo" >> saludo.txt***
- **<** = Toma un archivo como argumentro de entrada (***stdint***) para un comando ***sort < nombres.txt***

**Tuberias  | (pipes)**
Usamos el simbolo **|** para encadenar comandos, en otras palabra la salida de un comanod se convierte en la entrada del siguiente
- **cat archivo.txt | grep "error** = busca la palabra error en el contenido del archivo.txt
- **grep** = busca patrones e texto dentro de archivos o entradas estandar

- **comandos utiles con tuberias |**
    1) **dmerg | grep usp** = grep muestra la lineas del log con la palabra USB
    2) **ls *.txt | xargs cat** = concatena el contenido de todos los txt del directorio 
    3) **find . -name ".log" | xargs rm** = elimina todos los archivos .log encontramos

## Comandos de busqueda 

- **find** = Sirve para buscar ficheros y directorios dentro del sistema de fichero
    - find /home/ -name "*.txt" = * representa cualquier secuencia de texto
- **grep** = Busca patrones de texto en el fichero o directorio que le indiquemos
    - grep -i = hace que la busqueda  sea insensible a las mayusculas y minusculas
    - grep -c = contar cantidad de veces que aparece una coicnidecia en el documento ***grep -c "error" reporte.txt***
- **Locate** = Comando usado para encontrar la ubicacion de ficheros dentro del sistema, usa su propia base de datos para guardar esta rutas de ficheros 
    -sudo updatedb = actualiza la base de datos con los ficheros

## Editores de texto desde la terminal

- **vim** = Editor de los mas usados, tiene varios modos, modo comando, insercion y visual ***vim "ruta absoluta del fichero"*** 
    - Modo normal de vim = se usan teclas y comando para navergar dentro del contenido del fichero en este modo no se puede insertar texto manualmente:
        - *h* = movernos a la izquierda
        - *j* = nos movemos asia abajo
        - *k* = asi arriba
        - *l* = nos movemos a la derecha
        - *w* = nos vamos al inicio de la siguiente palabra
        - *e* = alfinal de la palabra actual
        - *dd* = borramos la linea donde estamos
        - *yy* = copiar
        - *p* = pegamos lo copiado / eliminado
        - *i* = modo insersion
        - *:* = modo comando

    - Modo de insersion = desde el modo normal apretamos la tecla *i* aqui si podemos añadir texto
    - Modo comando = para ejecutar comandos muy util en la escalada de privilegios
        - *:w* = guardar
        - *:q* = salir
        - *:q!* = salir sin guardar
        - *:wq: = guardar y salir
        - *:/* = buscar cierta palabra en el texto

- **nano** = es como vim pero mas amigable, las opciones estan abajo en la pantalla
    - **nano -m** = habilita el uso del raton dentro de nano
    - **nano -l** = muestra la cantidad de lineas dentro del fichero
    - **nano -v** = muestra el fichero en modo lectura        

## Comandos utiles**
- **nc** = netcat = abre y cierra puerta
    - **nc -l** = nos pone en escucha en un puerto
    - **nc -v** = activa el modo verbose y nos muestra mas detalles
    - **nc -p** = indica un puerto
    - **nc -n** = no se realice la resolucion dns
    - **nc -u** = usa el protocolo UDP ne lugar del TCP
- **echo** = impre por panlla valores o contenidos de variables
    - **echo -n** = no imprime la linea nueva al final del texot
    - **echo -e** = interpretacion de secuencias de escape como
        - \n = salto de linea
        - \t = tabulacion 
- **sort** = ordena lineas de texto 
    - sort -f = ignora el case sensitive y no diferencia entre mayusculas y minusculas
    - sort -o = guarda el resultado de la organizacion en un fichero
- **wget** = descarga ficheros de internet
    - wget -c = continua una descarga que fue interrumpida
    - wget --no-check-certificate = Ignora la verificacion del certificado dlc
- **curl** = tranposta datos desde un servidor a otro usado en el testeo de apis, soporta varios protocolos
    - **curl -x** = Se especifica el metodo de solicitud http
    - **curl -H** = añadimos encabezados a la solicitud
- **du** = muestra el espacio utilizado en memoria por el fichero a consultar
- **free** = estado de la memoria del sistema
    - **free -b** muestra la informacion en bits

## Atajos en linux

**Comandos a nivel de linea de comandos**
- ctrl + a = me envia al inicio de la linea
- ctrl + e = me envia al final de la linea
- ctrl + b = mueve un caracter a tras
- ctrl + f = mueve un caracter a delante
- alt + b = mueve el cursos una palabra a tras
- alt + f = mueve el cursos una palabra a delante
- ctrl + xx = va desde el inicio de la linea asta el final 

- **atajos a nivel de procesos**
    - ctrl + c = termina el proceso actual
    - ctrl + z = suspende le proceso actual
        - **fg** = trae a primer plano un proceso que se esta ejecutando en segundo plano indicando el numero de procesos
        - **jobs** = me muestra los indicadores de proceso
        - **bg** = Despierta un proceso que este dormido pero la ejecucion es en segundo plano
    - ctrl + d = sale de la terminal si no hay texto
- **atajos de historiales de comandos**
    - ctrl + p = comando anterior en el historial
    - ctrl + n = comando siguiente en el historisl
    - ctrl + r = buscamos dentro del historial
    - ctrl + o = buscamos dentro del historial ejecuta el comando
    - alt + . o alt + _ = Inserta el ultimo arugmento del comando anterior
- **atajos de control del emulador de terminal**
    - ctrl + l = limpiamos pantalla
    - ctrl + s = detenemos el desplazamiento de salida de la terminal
    - ctrl + q = reanudamos el desplazamienot de salida de la terminal
    - ctrl + alt (f1-f6) = cambiamos entre terminales TTI

- **disown** = elimina de la lista de trabajo el proceso llamado apra que se ejecute de forma independiente

## Alias en linux

Es una forma de ejecutar comandos o funciones personalizadas o ya establecidas atraves de un apalabra clave que nosotros creemos, estos son temporales a no ser que los agreguemos al archivo .bashrc

- **alias** = los comandos registrados
- **alias comando=funcion** = craecion y registro de alias
- **unalias** = elimina el alias en cuestion

----------------------------------------------------------------------------------------------------------
# Bibliografia de comandos

**Introduccion** = https://manpages.ubuntu.com/manpages/noble/man1/intro.1.html

¿Mas usos del ssh?
conexion ssh
ssh <username>@<server> -p <port>
**cat**: para leer nombres que empiecen con - hay que usar le -- para que cat no espere mas opciones de comando

los directorios o ficheros que tienen espacio en su nombre pueden ser remplazado por \ para que puedan se rinterpretados o dentro de comillas
**file**: me indica que tipo de archivo tengo y que hay en su interior
**du**: (disk usage) Info de el tamaño de un fichero o directorio que ocupa en nuestro sistema
**df**: (disk free)informacion de las partciones que tiene nuestro sistema y estado de memoria
**find** ***find <directory_path> <search_parameter>*** inicia una busqueda recursiba en la jerarquia de directorios









-----------------------------------------------------------------------------------------------------------
## Nota

🧰 Este documento esta en constante acutalizacion, esta basado en mi propio proceso de aprendizaje como hacker Ético, y administrador de sitemas Linux. por favor si ves algun error o tienes alguna sugerencia, me encantara leer tu comentario

- JL 🕸️🕷️



