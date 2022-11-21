import mysql.connector
import getpass

def conectarse():
    usuario = input("usuario: ")
    contrasenia = getpass.getpass("Contraseña: ", stream=None)
    #print(usuario, contrasenia)
    servidor = "127.0.0.1"
    bdd = "tpbiblioteca"

    conexion = mysql.connector.connect(
                                user=usuario,
                                passwd=contrasenia,
                                host=servidor,
                                database = bdd
                            )
    return conexion



