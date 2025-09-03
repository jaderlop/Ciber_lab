📌 Guía de Comandos Esenciales de Linux
1. man → Manual de usuario

Qué hace:
Muestra el manual oficial de un comando. Es como la documentación interna de Linux.

Sintaxis:

man [comando]


Ejemplos:

man grep       # Muestra el manual de grep
man ls         # Ayuda detallada del comando ls


Por qué es útil:
Te enseña todas las opciones disponibles de un comando.

2. grep → Buscar texto en archivos

Qué hace:
Busca coincidencias de patrones en archivos o en la salida de otros comandos. Usa expresiones regulares.

Sintaxis:

grep [opciones] "patrón" [archivo]


Ejemplos:

grep "root" /etc/passwd             # Busca la palabra root
grep -i "error" log.txt             # Búsqueda sin distinguir mayúsculas
grep -R "password" /var/www/        # Busca recursivamente en directorios
dmesg | grep "usb"                  # Combina con otro comando


Por qué es útil:
Ideal para filtrar información en archivos grandes, logs y configuraciones.

3. sort → Ordenar líneas

Qué hace:
Ordena texto de forma alfabética o numérica.

Sintaxis:

sort [opciones] [archivo]


Ejemplos:

sort nombres.txt                    # Ordena alfabéticamente
sort -r nombres.txt                # Orden inverso
sort -n numeros.txt                # Orden numérico


Por qué es útil:
Cuando trabajas con listas, logs o datos repetidos.

4. uniq → Eliminar duplicados

Qué hace:
Elimina líneas duplicadas consecutivas en un archivo.

Sintaxis:

uniq [opciones] [archivo]


Ejemplos:

sort nombres.txt | uniq            # Ordena y elimina duplicados
uniq -c nombres.txt               # Cuenta cuántas veces se repite cada línea


Por qué es útil:
Combinado con sort, es excelente para procesar listas.

5. strings → Extraer texto legible

Qué hace:
Muestra el texto legible dentro de archivos binarios.

Sintaxis:

strings [archivo]


Ejemplos:

strings /bin/ls                    # Muestra cadenas legibles del ejecutable
strings imagen.jpg                 # Intenta extraer metadatos o texto oculto


Por qué es útil:
Muy usado en ciberseguridad y análisis forense.

6. base64 → Codificar y decodificar

Qué hace:
Convierte datos a formato Base64 y viceversa.

Sintaxis:

base64 [archivo]
base64 --decode [archivo]


Ejemplos:

echo "hola" | base64               # Codifica: aG9sYQ==
echo "aG9sYQ==" | base64 --decode  # Decodifica: hola


Por qué es útil:
Para transferir datos, manipular credenciales y trabajar con APIs.

7. tr → Transformar caracteres

Qué hace:
Reemplaza, elimina o cambia caracteres.

Sintaxis:

tr [opciones] SET1 [SET2]


Ejemplos:

echo "hola" | tr a-z A-Z           # Convierte a mayúsculas: HOLA
echo "123-456-789" | tr -d '-'     # Elimina los guiones: 123456789


Por qué es útil:
Perfecto para limpiar datos o cambiar formatos rápidamente.

8. tar → Comprimir y descomprimir

Qué hace:
Crea y extrae archivos empaquetados .tar.

Sintaxis:

tar [opciones] [archivo]


Opciones principales:

-c → Crear archivo

-x → Extraer archivo

-v → Modo detallado

-f → Nombre del archivo

-z → Comprimir con gzip

-j → Comprimir con bzip2

Ejemplos:

tar -cvf backup.tar carpeta/       # Crear un tar
tar -xvf backup.tar               # Extraer un tar
tar -czvf backup.tar.gz carpeta/  # Comprimir con gzip


Por qué es útil:
Para copias de seguridad y transferencias.

9. gzip → Comprimir archivos

Qué hace:
Comprime archivos individuales en formato .gz.

Sintaxis:

gzip [archivo]
gunzip [archivo.gz]


Ejemplos:

gzip log.txt                       # Crea log.txt.gz
gunzip log.txt.gz                 # Descomprime

10. bzip2 → Compresión avanzada

Qué hace:
Similar a gzip, pero con mejor tasa de compresión.

Sintaxis:

bzip2 [archivo]
bunzip2 [archivo.bz2]


Ejemplos:

bzip2 log.txt                     # Comprime log.txt.bz2
bunzip2 log.txt.bz2              # Descomprime

11. xxd → Ver y editar en hexadecimal

Qué hace:
Muestra contenido de archivos en formato hexadecimal.

Sintaxis:

xxd [archivo]


Ejemplos:

xxd imagen.jpg                    # Ver encabezado hexadecimal
xxd -r hex.txt binario            # Reconstruir binario desde hex


Por qué es útil:
Indispensable en análisis forense, malware y reversing.

12. find → Buscar archivos y directorios

Qué hace:
Busca archivos por nombre, tamaño, fecha, usuario, permisos, etc.

Sintaxis:

find [ruta] [criterios]


Ejemplos:

find /home -name "*.txt"           # Buscar archivos .txt
find /var/log -type f -size +5M    # Archivos mayores a 5MB
find / -perm 777                  # Archivos con permisos inseguros


Por qué es útil:
Ideal para auditorías de seguridad y administración de sistemas.

13. file → Identificar tipo de archivo

Qué hace:
Determina el tipo real de un archivo, sin depender de su extensión.

Sintaxis:

file [archivo]


Ejemplos:

file foto.jpg                     # Detecta si es realmente una imagen
file script.sh                    # Verifica si es ejecutable

14. ls → Listar archivos

Qué hace:
Muestra el contenido de un directorio.

Sintaxis:

ls [opciones]


Ejemplos:

ls -l                             # Lista detallada
ls -lh                            # Tamaños legibles
ls -la                            # Incluye archivos ocultos

15. cd → Cambiar de directorio

Qué hace:
Navega entre carpetas.

Sintaxis:

cd [ruta]


Ejemplos:

cd /home/usuario                  # Ir a la carpeta usuario
cd ..                            # Subir un nivel
cd ~                             # Ir a tu home

16. Combinando comandos: ejemplos prácticos
a) Buscar y contar errores en logs
grep "ERROR" /var/log/syslog | wc -l


🔹 Útil para monitorear fallos.

b) Encontrar archivos sospechosos
find / -type f -perm 777 | xargs ls -lh


🔹 Perfecto para auditoría de seguridad.

c) Extraer cadenas legibles de un binario
strings /bin/ls | grep "GNU"


🔹 Útil en análisis forense.

Si quieres, puedo prepararte un PDF visual con todos estos comandos, ejemplos, diagramas y flujos para que lo uses como manual de referencia rápida.
Además, podría agregar comandos avanzados para hacking ético como netstat, tcpdump, nmap y lsof.

¿Quieres que prepare ese manual avanzado y lo organice en una especie de diccionario visual?