#!/usr/bin/env python

#Variables
host = 'localhost'
port = 8050
#Se importa el módulo
import socket

def llaves(lista):
    q = int(lista[0].strip())
    key = int(lista[1].strip())
    p = int(lista[2].strip())
    return q,key,p

def power(a, b, c):
    x = 1
    y = a
 
    while b > 0:
        if b % 2 != 0:
            x = (x * y) % c
        y = (y * y) % c
        b = int(b / 2)
 
    return x % c

def decrypt(en_msg, p, key, q): 
 
    dr_msg = []
    h = power(p, key, q)
    for i in range(0, len(en_msg)):
        dr_msg.append(chr(int(en_msg[i]/h)))
    # Lista con el mensaje desencriptado
    return dr_msg




#Creación de un objeto socket (lado cliente)
obj = socket.socket()

#Conexión con el servidor. Parametros: IP (puede ser del tipo 192.168.1.1 o localhost), Puerto
obj.connect((host, port))
print("Conectado al servidor")
print()



cifrado = obj.recv(1024)   

with open("keys/keys.txt","r") as archivo:
    q,key,p = llaves(archivo.readlines())

mensaje_seguro = cifrado.decode('ascii').split(" ")
mensaje_seguro = [int(x) for x in mensaje_seguro]

textoplano = decrypt(mensaje_seguro, p, key, q)
textoplano = ''.join(textoplano)
print(textoplano)
with open("mensajerecibido.txt","w+") as archivo:
    archivo.write(textoplano)

#Cerramos la instancia del objeto servidor
obj.close()
