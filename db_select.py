#Cada función de este módulo transforma el objeto obtenido de los módulos
#libros y clientes y devuelve una consulta SQL en limpio

def seleccionar_filtro(tabla, campo, parametro):
    consulta = f'SELECT * FROM {tabla} WHERE {campo} LIKE "{parametro}"'
    print(consulta)
    return consulta

def seleccionar_foraneas(tabla, tablasForaneas, campos, parametro):
    consulta = f'SELECT {campos} FROM {tabla} {["INNER JOIN "+x for x in tablasForaneas]} WHERE {parametro}"'
    print(consulta)
    return consulta

#def eliminar_registro
#def actualizar_registro
#def ingresar_registro