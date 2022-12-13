import db_conexion
import db_select

def dbConsulta(consulta):
    conexion = db_conexion.conectarse()
    cursor = conexion.cursor()
    try:
        cursor.execute(consulta)
        resultado_consulta = cursor.fetchall()
    except Exception as e:
        print(e)
    conexion.close()
    return resultado_consulta

def dbModificacion(consulta):
    conexion = db_conexion.conectarse()
    cursor = conexion.cursor()
    try:
        cursor.execute(consulta)
    except ValueError as e:
        print(e)
    conexion.commit()
    conexion.close()

def consultarTabla(campo, valor, tabla):
    consulta = f'SELECT * FROM {tabla} WHERE {campo} LIKE "%{valor}%"'
    try:
        res=dbConsulta(consulta)
        return res
    except Exception as E:
        print("Erorr:"+str(e))
        exit()

    
def ingresarRegistro(valoresPar, tabla):
    consulta = f'''INSERT INTO {tabla} ({",".join([campo for campo in valoresPar])}) VALUES ({",".join([f"'{valoresPar[campo]}'" for campo in valoresPar])})'''
    try:
        res=dbModificacion(consulta)
        return res
    except Exception as e:
        print("Erorr:"+str(e))
        exit()
        
def eliminarRegistro(id, tabla):
    consulta = f'DELETE FROM {tabla} WHERE id={id}'
    try:
        dbModificacion(consulta)
    except Exception as e:
        print("Erorr:"+str(e))
        exit()

def modificarRegistro(valoresPar, id, tabla):
    consulta = f'''UPDATE {tabla} SET {",".join([campo+"='"+valoresPar[campo]+"'"  for campo in valoresPar])} WHERE id={id}'''
    try:
        res=dbModificacion(consulta)
        print("Modificado con éxito")
    except Exception as e:
        print("Erorr:"+str(e))
        exit()