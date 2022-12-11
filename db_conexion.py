import mysql.connector
import getpass
import os

def conectarse():
    rootDir=os.path.dirname(__file__)
    cfgFile = os.path.join(rootDir,"config.cfg")
    try:
        f = open(cfgFile,"r")
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
        try:
            f = open(cfgFile,"w")
            f.write('\n'.join([usuario,contrasenia,servidor,bdd]))
            f.close()
        except Exception as e:
            print(e)
    conexion = mysql.connector.connect(
                                user=usuario,
                                passwd=contrasenia,
                                host=servidor
                            )
    cursor = conexion.cursor(buffered=True)
    cursor.execute(f"SHOW DATABASES LIKE '{bdd}'")
    res=cursor.fetchone()
    if res:
        conexion.close()
        conexion = mysql.connector.connect(
                                user=usuario,
                                passwd=contrasenia,
                                host=servidor,
                                database=bdd
        )
        input("DB encontrada, presione una tecla para continuar.")
        return conexion
    else:
        cursor.execute(f"CREATE DATABASE {bdd}")
        conexion.commit()
        conexion.close()
        conexion = mysql.connector.connect(
                        user=usuario,
                        passwd=contrasenia,
                        host=servidor,
                        database=bdd
        )
        cursor = conexion.cursor()
        datasetFile = os.path.join(rootDir,"tpbiblioteca.sql")
        f = open(datasetFile,"r", encoding="utf8")
        sql=''
        for line in f:
            if line.strip():                
                sql=sql+str(line)
        cursor.execute(sql)
        input("DB no encontrada. Se ha creado automáticamente. Presione una tecla para continuar.")
        return conexion

conectarse()
