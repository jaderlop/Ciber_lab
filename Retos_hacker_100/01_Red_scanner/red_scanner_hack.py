#!/usr/bin/env python3
import nmap
from scapy.all import ARP, Ether, srp

def main():
    # Inicializacion del objeto scaner y definicion del rango de IPs
    # Que queremos escanear
    scanner = nmap.PortScanner()
    ip_range = '192.168.0.0/24'

    # Construimos un paquete ARP broadcast
    arp = ARP(pdst=ip_range)  
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")  
    packet = ether / arp  # Apilamos Ethernet + ARP
    print("[!!] Escaneando red local con Nmap (ping scan)...")

    # Escaneo ping al rango de ips establecidos con -sn para ver los host activos
    scanner.scan(hosts=ip_range, arguments='-sn')

    # Iteramos sobre todos los hosts encontrados para ver su setado UP , DOWN
    for host in scanner.all_hosts():
        state = scanner[host].state()         
        host_name = scanner[host].hostname()  
        print(f'[+] Host detectado: {host} ({host_name}) - Estado: {state}')

    # Escaneo ARP con scapy para confirmacion del estado de los host
    print('\n[!!] Enviando solicitudes ARP para confirmación...')
    result = srp(packet, timeout=3, verbose=0)[0]

    for sent, received in result:
        print(f'[+] {received.psrc} está activo vía ARP')

    # Escaneo de puertos en un host específico
    target = input("\n[?] Ingresa la IP que deseas escanear puertos: ")
    print(f"[!!] Escaneando puertos 1–1024 en {target} con Nmap (TCP SYN scan)...\n")
    scanner.scan(hosts=target, ports='1-1024', arguments='-sS')

    # Recorremos protocolos y puertos abiertos
    for proto in scanner[target].all_protocols():
        lports = scanner[target][proto].keys()
        for port in sorted(lports):
            state = scanner[target][proto][port]['state']
            print(f'--> Puerto {port}/{proto}: {state}')

if __name__ == "__main__":
    main()
