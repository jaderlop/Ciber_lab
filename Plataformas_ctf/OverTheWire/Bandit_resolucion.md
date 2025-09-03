# Link 
https://overthewire.org/wargames/

## niveles y banderas

### level 0 --> 1
- **host**: bandit.labs.overthewire.org,
- **Credenciales**:U:bandit0 P:bandit0
- **Concepto**: Conexion SSH
<usuario>@<hostname> -p <puerto>

- **bandera 0**  ZjLjTmM6FvvyRnrb2rfNWOZOTa6ip5If

### level 1 --> 2
- **Credenciales** U:bandit1 P:Bandera level0
- **Concepto** Ficheros con nombres especiales
- **Tecnica usada** Especificacion de la ruta relativa del fichero con nombre especial
- **Comandos usados** cat ./-
- **bandera 1** 263JGJPfgU6LtdEvgfWU1XP5yac29mFx
- **Explicacion** El nombre del arcivo literalmente es "-" lo cual puede confundirece con la opcion de ingresar un comando
***Borrar banderas***

### level 2 --> 3
- **Credenciales** U:bandit2 P:Bandera level1
- **Concepto** Espacio en nombres de archivos
- **Tecnica usada** Encapsulamiento de una cadena de texto con comillas simples ' '
- **Comandos usados** cat ./'--spaces in this filename--'
- **bandera 2** MNk8KNH3Usiio41PRUEoDFPqfxLPlSmx
- **Explicacion** Al usar el comando cat y ir acompañar de guiones -- y espacios lo puede interpretar como opciones el comando usado evitando su correcto funcionamiento

### level 3 --> 4
- **Credenciales** U:bandit3 P:Bandera level2
- **Concepto**  Archivos ocultos
- **Tecnica usada** Ocultar archivos mediante el prefijo '.'
- **Comandos usados** cat, ls -all
- **bandera 3** 2WmrDFRmJIq3IPxneAaMGhap0pFhF3NJ
- **Explicacion** Los archivos ocultos no son listados predefinidamente por el comanod ls para ello hay que abordarlo con la opcion -all que le indica que queremos ver todos los archivos, algo interesante esque el nombre tenia 3 puntos 

### level 4 --> 5
- **Credenciales** U:bandit4 P:Bandera level3
- **Concepto** Archivos con informacion solo leible por humanos
- **Tecnica usada** se crearon varios archivos pero solo uno era tipo texto ASCII que es leible por humanos
- **Comandos usados** file ./*
- **bandera 4** 4oQYVPkxZOOEOO5pTW81FB8j8lxXGUQw
- **Explicacion** la dificultad radica en saber que archivo esta destinado a que nosotroS lo leamos, al ser varios archivos podemos pasar la salida del comando file./* que me revisara todos los archivos al comando grep por medio de un pipe '|' usando un comando tal que asi file ./* | grep 'ASCII'

### level 5 --> 6**
- **Credenciales** U:bandit5 P:Bandera level4
- **Concepto** Ubicacion de archivos con especificaiones como not executable, de un tamaño determinado y que sea solo leido por humanos
- **Tecnica usada** se uso el comando find para filtar entre la gran cantidad de archivos que existian y el contenido de estos la estructura de find es 'find [ruta] [opciones] [accion]
- **Comandos usados** find . -type f -size 1033c
- **bandera 5** HWasnPhtq9AVKe0dmk45nxy20cvUa6EG



### level 6 --> 7**
- **Credenciales** U:bandit6 P:Bandera level5
- **Concepto** Ubicacion de archivos con especificaiones como un usuario en particular, un tamaño en particular y a que grupo pertenece
- **Tecnica usada** se uso el comando find para filtar entre la gran cantidad de archivos que existian y el contenido de estos la estructura de find es 'find [ruta] [opciones] [accion]
- **Comandos usados** find . -type f -size 33c -group bandit6 -user bandit7 -exec ls -l {} \; 2>dev/null
- **bandera 6** morbNTDkSW6jIlUc0ymOdMaLnOlFVAaj
