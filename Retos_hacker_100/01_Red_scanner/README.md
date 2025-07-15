# Creacion de un escaner de red
Proyecto 1 de 100 de **retos hacker** con el objetivo de ver dispositivos activos en la red local y escanear sus puertos

## Conceptos para crear este escaner

### Redes
- **Modelo OSI** = capa 2 y 3
- **Protocolo ARP** 
- **Protocolo TCP/IP** = Puertos comunes (HTTP, SSH, DNS, etc)
- **Subredes y mascaras de red** = 192.168.0.0/24; CIDR

### Herramientes
- **Nmap** = tipos de escano, sintaxis de comando
- **Scapy** = construccion de paquetes personalizados
- **wireshark** = Ver visualmente los paquetes

### Python
- sintaxis y estructuras basicas (bucles, input, diccionarios)
- Librerias:
    - **nmap**: interfaz de python de Nmap
    - **scapy**: para el envio y recepcion de paquetes en la red

### Hacking Ético / pentesting
- conceptos de enumeracion, reconocimiento activo y escaneo de puertos
- Identificacion de servicios en base a los puertos

## Documentacion del codigo

Para tener nuestro sistema ordenado y la dependencias separadas entre progamas, creamos un ambiente virtual ***python3 -m venve "nombre_ambiente_venv*** y procedemos a activarlos ***source nombre_ambeinte_venv/bin/acitvate***

definicion de el rango de IPs a escanear ***192.168.0.0/24*** y creacion de los obejeots ***scanner = nmap.PortScanner()*** y Paquetes ARP broadcast con la finalidad de confirmar el estado de los host encontrados imprimiendolos en patalla

ingresamos una de las IPs de interes a consultar para la iteracion de un rango de puertos previamente definidos con el objetivo de ver su estado

## Resultados
- detectar dispositivos conectados a la red wifi o LAN
- Confirmacion de su precencia via Nmap y ARP
- Consultar puertos abiertos en cada host para identificar posibles servicios

## Aviso legal
Este script está diseñado únicamente para fines educativos y pruebas en redes propias o autorizadas. El uso en redes ajenas sin permiso puede ser considerado ilegal.