import mysql.connector
import getpass

def conectarse():
    try:
        f = open("config.cfg","r")
        usuario = f.readline().strip()
        contrasenia = f.readline().strip()
        servidor = f.readline().strip()
        bdd = f.readline().strip()
        f.close()
    except:
        usuario = input("usuario: ")
        contrasenia = getpass.getpass("Contraseña: ", stream=None)
        servidor = input("servidor: ")
        bdd = input("bbd: ")
        f = open("config.cfg","w")
        f.write('\n'.join([usuario,contrasenia,servidor,bdd]))
        f.close()

    conexion = mysql.connector.connect(
                                user=usuario,
                                passwd=contrasenia,
                                host=servidor,
                                database = bdd
                            )
    return conexion



