import socket
import requests

#Pega Ip Local e Publico

ip_publico = requests.get('https://api.ipify.org/').text
ip_local = socket.gethostbyname(socket.gethostname())
print(f'IP Publico: {ip_publico}')
print(f'IP Local: {ip_local}')



