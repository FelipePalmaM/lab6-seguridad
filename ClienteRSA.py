#!/usr/bin/env python

#Variables
host = 'localhost'
port = 8050
#Se importa el módulo
import socket
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP



def RSA_Decrypt(Recibir):
    with open("keys/keys.pem","r") as archivo:
        llave = RSA.importKey(archivo.read())
    llavePrivada = PKCS1_OAEP.new(key= llave)


    mensaje = llavePrivada.decrypt(Recibir)
    
    with open("mensajerecibido.txt","w+") as archivo:
        archivo.write(mensaje.decode('ascii'))
    
    return mensaje

#Creación de un objeto socket (lado cliente)
obj = socket.socket()

#Conexión con el servidor. Parametros: IP (puede ser del tipo 192.168.1.1 o localhost), Puerto
obj.connect((host, port))
print("Conectado al servidor")
print()



cifrado = obj.recv(1024)   
decifrado=RSA_Decrypt(cifrado)

print(decifrado.decode('ascii'))
        
#Cerramos la instancia del objeto servidor
obj.close()
