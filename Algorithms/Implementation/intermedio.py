#!/usr/bin/python
# -*- coding: utf-8 -*-
 
# Programa Servidor
# Fuente original de este codigo: www.pythondiario.com
# Utilizado para fines academicos en el curso CI-1320 

import socket
import sys
 
# Creando el socket TCP/IP
sockServ = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sockCliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Enlace de socket y puerto
intermedio_address = ('localhost', 10000)
server_address = ('localhost', 10001)

print >>sys.stderr, 'empezando a levantar %s puerto %s' % intermedio_address
sockCliente.bind(intermedio_address)

# Escuchando conexiones entrantes
sockCliente.listen(1)
 
while True:
    # Esperando conexion
    print >>sys.stderr, 'Esperando para conectarse'
    connection, client_address = sockCliente.accept()
    try:
        print >>sys.stderr, 'concexion desde', client_address
 
        # Recibe los datos en trozos y reetransmite
        while True:
            data = connection.recv(1000)
            print >>sys.stderr, 'recibido "%s" por intermedio' % data
            if data:
                data += "intermedio"
                sockServ.connect(server_address)
                print >>sys.stderr, 'enviando mensaje al servidor'
                sockServ.sendall(data)
            else:
                print >>sys.stderr, 'no hay mas datos', client_address
                break
             
    finally:
        # Cerrando conexion
        connection.close()
            
    
