from db import dbConsulta, dbModificacion


def consultarLibro(campo, valor):
    consulta = f'SELECT * FROM libros WHERE {campo} LIKE "{valor}"'
    res=dbConsulta(consulta)
    print(res)
    return res
    
def ingresarLibro(valoresPar):
    consulta = f'''INSERT INTO libros ({",".join([campo for campo in valoresPar])}) VALUES ({",".join([f"'{valoresPar[campo]}'" for campo in valoresPar])})'''
    print(consulta)
    try:
        res=dbModificacion(consulta)
        print("Ingresado con éxito")
        return res
    except Exception as e:
        print('Hubo un error al ingresar el libro: '+str(e))

def eliminarLibro(id):
    consulta = f'DELETE FROM libros WHERE id={id}'
    print(consulta)
    try:
        dbModificacion(consulta)
    except:
        print('Hubo un error al eliminar el libro')

def modificarLibro(valoresPar, id):
    consulta = f'''UPDATE libros SET {",".join([campo+"='"+valoresPar[campo]+"'"  for campo in valoresPar])} WHERE id={id}'''
    try:
        res=dbModificacion(consulta)
        print("Modificado con éxito")
    except Exception as e:
        print('Hubo un error al ingresar el libro: '+str(e))

'''
def consultarEstadoLibro(id):
    consulta = f'SELECT estado FROM prestamos INNER JOIN libros ON libros.pklibro = prestamos.fklibro WHERE libros.id={id}'
    return consulta

def prestarLibro(idLibro, idCliente):
    consulta = f'INSERT INTO prestamos () WHERE fklibro={idLibro} AND fkcliente={idCliente}'
    return consulta

def devolverLibro(valor):
    consulta = f'UPDATE prestamos SET estado=0 WHERE fklibro={valor}'
    return consulta
'''