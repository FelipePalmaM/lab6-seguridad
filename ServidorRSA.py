#!/usr/bin/env python

#Se importa el módulo
import socket
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
 

def RSA_Encryption():
    key = RSA.generate(1024)
    with open("keys/keys.pem","wb") as archivo:
        archivo.write(key.exportKey('PEM'))
    print("Leyendo el mensaje...\n")
    with open("mensajeentrada.txt","r+") as archivo:
        texto = [x.strip() for x in archivo] 
        texto = " ".join(texto)
        
    texto = texto.encode('ascii')
    print("Enviando mensaje Seguro...\n")
    public_key = PKCS1_OAEP.new(key.publickey())
    mensaje_seguro = public_key.encrypt(texto)
    return mensaje_seguro
    
    
    

#instanciamos un objeto para trabajar con el socket
ser = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Puerto y servidor que debe escuchar
ser.bind(("", 8050))

#Aceptamos conexiones entrantes con el metodo listen. Por parámetro las conexiones simutáneas.
ser.listen(1)

#Instanciamos un objeto cli (socket cliente) para recibir datos
cli, addr = ser.accept()


cifrado= RSA_Encryption()
cli.send(cifrado)
cli.close()
    

    
        
    

#Cerramos la instancia del socket cliente y servidor
cli.close()




    