#!/usr/bin/env python

#Se importa el módulo
import socket
import random

def gcd(a, b):
    # Mayor comun divisor
    if a < b:
        return gcd(b, a)
    elif a % b == 0:
        return b;
    else:
        return gcd(b, a % b)
    
def gen_key(q):
    # Genera una llave para el servidor
    key = random.randint(pow(10, 20), q)
    while gcd(q, key) != 1:
        key = random.randint(pow(10, 20), q)

    return key

def power(a, b, c):
    x = 1
    y = a
 
    while b > 0:
        if b % 2 != 0:
            x = (x * y) % c
        y = (y * y) % c
        b = int(b / 2)
 
    return x % c

def encrypt(msg, q, h, g):
 
    en_msg = []
 
    k = gen_key(q) # Llave para el servidor
    s = power(h, k, q)
    p = power(g, k, q)
     
    for i in range(0, len(msg)):
        en_msg.append(msg[i])
 
    for i in range(0, len(en_msg)):
        en_msg[i] = s * ord(en_msg[i])
    # Lista con el mensaje encriptado y p
    return en_msg, p
 
    
    
    

#instanciamos un objeto para trabajar con el socket
ser = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Puerto y servidor que debe escuchar
ser.bind(("", 8050))

#Aceptamos conexiones entrantes con el metodo listen. Por parámetro las conexiones simutáneas.
ser.listen(1)

#Instanciamos un objeto cli (socket cliente) para recibir datos
cli, addr = ser.accept()


a = random.randint(2, 10)
q = random.randint(pow(10, 20), pow(10, 50))
g = random.randint(2, q)
    
key = gen_key(q)# llave privada para el cliente

    

print("Leyendo el mensaje...\n")
with open("mensajeentrada.txt","r+") as archivo:
    texto = [x.strip() for x in archivo]
    texto = " ".join(texto)

h = power(g, key, q)
print("Enviando mensaje Seguro...\n")
mensaje_seguro, p = encrypt(texto, q, h, g)

mensaje_seguro = [str(x) for x in mensaje_seguro]

mensaje_seguro = " ".join(mensaje_seguro).encode('ascii')

with open("keys/keys.txt","w+") as archivo:
    archivo.write(str(q))
    archivo.write('\n'+str(key))
    archivo.write('\n'+str(p))

cli.send(mensaje_seguro)

cli.close()
    

    
        
    

#Cerramos la instancia del socket cliente y servidor
cli.close()




    