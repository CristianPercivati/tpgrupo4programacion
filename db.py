import db_conexion
import db_select

def dbConsulta(consulta):
    conexion = db_conexion.conectarse()
    cursor = conexion.cursor()
    cursor.execute(consulta)
    resultado_consulta = cursor.fetchall()
    conexion.close()
    return resultado_consulta

def dbModificacion(consulta):
    conexion = db_conexion.conectarse()
    cursor = conexion.cursor()
    cursor.execute(consulta)
    conexion.commit()
    conexion.close()

def consultarTabla(campo, valor, tabla):
    consulta = f'SELECT * FROM {tabla} WHERE {campo} LIKE "%{valor}%"'
    print(consulta)
    res=dbConsulta(consulta)
    return res
    
def ingresarRegistro(valoresPar, tabla):
    consulta = f'''INSERT INTO {tabla} ({",".join([campo for campo in valoresPar])}) VALUES ({",".join([f"'{valoresPar[campo]}'" for campo in valoresPar])})'''
    print(consulta)
    try:
        res=dbModificacion(consulta)
        return res
    except Exception as e:
        return e
        
def eliminarRegistro(id, tabla):
    consulta = f'DELETE FROM {tabla} WHERE id={id}'
    print(consulta)
    try:
        dbModificacion(consulta)
    except:
        print('Hubo un error al eliminar el libro')

def modificarRegistro(valoresPar, id, tabla):
    consulta = f'''UPDATE {tabla} SET {",".join([campo+"='"+valoresPar[campo]+"'"  for campo in valoresPar])} WHERE id={id}'''
    try:
        res=dbModificacion(consulta)
        print("Modificado con éxito")
    except Exception as e:
        print('Hubo un error al ingresar el libro: '+str(e))