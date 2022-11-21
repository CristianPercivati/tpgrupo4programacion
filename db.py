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