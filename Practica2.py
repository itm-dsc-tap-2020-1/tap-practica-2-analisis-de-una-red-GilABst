import os
hostname = "www.itmorelia.edu.mx"
respuesta = os.system("ping -c 1 " + hostname)
if respuesta == 0:
    print(hostname + ": esta en funcionamiento")
else:
    print(hostname + ": no funciona")

red = "200.33.171.0/24"
os.system("nmap -sP " + red)

#--- denebvirtual.itmorelia.edu.mx ping statistics ---
#1 packets transmitted, 1 received, 0% packet loss, time 0ms
#rtt min/avg/max/mdev = 1.641/1.641/1.641/0.000 ms
#www.itmorelia.edu.mx: esta en funcionamiento
#Nmap scan report for mail.itmorelia.edu.mx (200.33.171.3)
#Host is up (0.0030s latency).
#Nmap scan report for 200.33.171.13
#Host is up (0.0024s latency).
#Nmap scan report for denebvirtual.itmorelia.edu.mx (200.33.171.77)
#Host is up (0.0025s latency).
#Nmap scan report for sappp.itmorelia.edu.mx (200.33.171.80)
#Host is up (0.0052s latency).
#Nmap scan report for 200.33.171.85
#Host is up (0.012s latency).
#Nmap scan report for vinculacion.itmorelia.edu.mx (200.33.171.124)
#Host is up (0.0035s latency).
#Nmap scan report for 200.33.171.125
#Host is up (0.0034s latency).
#Nmap scan report for 200.33.171.127
#Host is up (0.016s latency).
#Nmap done: 256 IP addresses (8 hosts up)