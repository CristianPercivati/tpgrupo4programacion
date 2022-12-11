from db import dbConsulta, dbModificacion, consultarTabla, ingresarRegistro, modificarRegistro, eliminarRegistro
from datetime import datetime

def consultarPrestamo(campo, valor):
    res = consultarTabla(campo, valor, "libros")
    resPrestamo=consultarTabla('fk_libro', res[0][0], 'prestamos')
    respuesta = ''
    for item in resPrestamo:
        respuesta = respuesta + f'''
        **************\n
        ID_LIBRO: {item[1]}\n
        ID_SOCIO: {item[2]}\n
        FECHA_PRESTAMO: {item[3]}
        Estado Prestamo: {item[4]}-\n
        **************'''
    print(respuesta)
    return respuesta


def ingresarPrestamo(ISBN, DNI, fecha_prestamo, estado):
    fecha_prestamo2=datetime.strptime(fecha_prestamo, "%d/%m/%Y").strftime("%Y-%m-%d")
    print(fecha_prestamo2)
    try:
        idLibro = consultarTabla('isbn', ISBN, "libros")
        idCliente = consultarTabla('dni', DNI, 'clientes')
        existePrestamo=consultarTabla('fk_libro', idLibro[0][0], 'prestamos')
        if existePrestamo:
            if existePrestamo[0][3]!=0:
                prestadoA=consultarTabla('id', existePrestamo[0][2], 'clientes')
                return f"""
                El préstamo ya existe.

                A nombre de: {prestadoA[0][2]}
                En la fecha: {existePrestamo[0][4]}
                """
            else:
                print(existePrestamo[0][3])
                ingresarRegistro(
                    {
                        'fk_libro': idLibro[0][0],
                        'fk_cliente': idCliente[0][0],
                        'fecha_prestamo': fecha_prestamo2,
                        'estado': estado
                    }, "prestamos")
                return "Prestamo ingresado correctamente."
        else:
                ingresarRegistro(
                    {
                        'fk_libro': idLibro[0][0],
                        'fk_cliente': idCliente[0][0],
                        'fecha_prestamo': fecha_prestamo2,
                        'estado': estado
                    }, "prestamos")
                return "Prestamo ingresado correctamente."
    except Exception as e:
        return "Hubo un error al ingresar el Prestamo: " + str(e)


def eliminarPrestamo(ISBN):
    resLibros = consultarTabla('isbn', ISBN, "libros")
    resPrestamo=consultarTabla('estado=1 AND fk_libro', resLibros[0][0], 'prestamos')
    resClientes = consultarTabla('id', resPrestamo[0][2], 'clientes')
    respuesta = ''
    for item in resPrestamo:
        respuesta = respuesta + f'''
        **************\n
        ISBN: {resLibros[0][3]}\n
        Nombre Cliente: {resClientes[0][2]}\n
        Fecha Préstamo: {item[4]}\n
        Estado: {"En préstamo" if item[3]==1 else "Devuelto"}\n
        **************'''
    print(respuesta)

    confirmacion = input(
        "¿Está seguro que desea eliminar este Prestamo? S/N:\n")

    if confirmacion.upper() == "S":
        try:
            modificarRegistro({
                'estado': '0'
            },resPrestamo[0][0],"prestamos")
            return "Prestamo borrado exitosamente"
        except Exception as e:
            return "Ocurrió un error al intentar eliminar: " + str(e)
    elif confirmacion.upper() == "N":
        return "Operación abortada."
    else:
        return "Ingreso no válido"


def historialPrestamo(valor,tipo):
    respuesta=[]
    if tipo=='dni':
        resClientes = consultarTabla('dni', valor, "clientes")
        resPrestamo = consultarTabla('fk_cliente', resClientes[0][0], 'prestamos')
        for item in resPrestamo:
            resLibros = consultarTabla('id', item[1], "libros")
            respuesta.append([resLibros[0][1][0:15],item[4].strftime('%d/%m/%Y'),"Devuelto" if item[3]==0 else "En Préstamo.",resClientes[0][2]])
        return respuesta
    elif tipo=='isbn':
        resLibros = consultarTabla('isbn', valor, "libros")
        resPrestamo = consultarTabla('fk_libro', resLibros[0][0], 'prestamos')
        for item in resPrestamo:
            resClientes = consultarTabla('id', item[2], "clientes")
            respuesta.append([resClientes[0][2][0:15],item[4].strftime('%d/%m/%Y'),"Devuelto" if item[3]==0 else "En Préstamo.",resLibros[0][1]])
        return respuesta