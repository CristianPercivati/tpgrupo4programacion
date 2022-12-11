from db import dbConsulta, dbModificacion, consultarTabla, ingresarRegistro, modificarRegistro, eliminarRegistro


def consultarLibro(campo, valor):
    res = consultarTabla(campo, valor, "libros")
    return res


def ingresarLibro(autor, titulo, isbn):
    try:
        ingresarRegistro({
            'autor': autor,
            'titulo': titulo,
            'isbn': isbn
        }, "libros")
        return "Libro ingresado correctamente."
    except Exception as e:
        return "Hubo un error al ingresar el libro: " + str(e)


def eliminarLibro(isbn):
    res = consultarTabla('isbn', isbn, "libros")
    respuesta = ''
    for item in res:
        respuesta = respuesta + f'''
        **************\n
        Título: {item[1]}\n
        Autor: {item[2]}\n
        ISBN: {item[3]}\n
        Estado: -\n
        **************'''
    print(respuesta)

    confirmacion = input("¿Está seguro que desea eliminar este libro? S/N:\n")

    if confirmacion.upper() == "S":
        try:
            eliminarRegistro(item[0], 'libros')
            return "Libro borrado exitosamente"
        except Exception as e:
            return "Ocurrió un error al intentar eliminar: " + str(e)
    elif confirmacion.upper() == "N":
        return "Operación abortada."
    else:
        return "Ingreso no válido"


def modificarLibro(isbn):
    #
    item = consultarTabla('isbn', isbn, "libros")
    print(item)
    respuesta = ''
    respuesta = respuesta + f'''
        **************\n
        Título: {item[0][1]}\n
        Autor: {item[0][2]}\n
        ISBN: {item[0][3]}\n
        Estado: -\n
        **************'''
    print(respuesta)
    print("A continuación modifique los datos del libro. Si no desea modificar el dato, presione Enter.")
    titulo = str(input("Titulo: "+item[0][1]) or item[0][1])
    print("Nuevo valor: "+titulo)
    autor = str(input("Autor: "+item[0][2]) or item[0][2])
    print("Nuevo valor: "+autor)
    isbn = str(input("isbn: "+item[0][3]) or item[0][3])
    print("Nuevo valor: "+isbn)
    try:
        modificarRegistro({'titulo': titulo, 'autor': autor, 'isbn': isbn}, item[0][0], "libros")
        return "modificado con éxito"
    except Exception as e:
        return "Error: "+str(e)

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