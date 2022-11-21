
def seleccionar_filtro(tabla, campo, parametro):
    consulta = f'SELECT * FROM {tabla} WHERE {campo} LIKE "{parametro}"'
    print(consulta)
    return consulta
