import db_conexion
import db_select

def dbQuery(type='connect',params={}):
    conexion = db_conexion.conectarse()
    print(conexion)
    cursor = conexion.cursor()

    if type=='connect':
        #Mostrar tablas
        cursor.execute("SHOW TABLES")
        tablas = cursor.fetchall()
        for tabla in tablas:
            print(tabla[0])
        print(params)

    elif type=='select':
        print(params)
        #Realizo una consulta
        consulta_select = db_select.seleccionar_filtro(**params)
        #Ejecuto la consulta
        cursor.execute(consulta_select)
        resultado_consulta = cursor.fetchall()
        #Imprimir resultados de consulta
        for resultado in resultado_consulta:
            print(resultado)

    #Cerrar conexion
    conexion.close()
