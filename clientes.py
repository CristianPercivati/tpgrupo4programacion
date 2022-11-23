from db import dbConsulta, dbModificacion, consultarTabla, ingresarRegistro, modificarRegistro, eliminarRegistro


def consultarCliente(campo, valor):
    res = consultarTabla(campo, valor, "clientes")
    print(res)
    respuesta = ''
    for item in res:
        respuesta = respuesta + f'''
        **************\n
        DNI: {item[1]}\n
        Nombre: {item[2]}\n
        Teléfono: {item[3]}\n
        Dirección: {item[4]}\n
        Estado: -\n
        **************'''
    return respuesta


def ingresarCliente(dni, nombre, telefono, direccion):
    try:
        ingresarRegistro(
            {
                'dni': dni,
                'nombre': nombre,
                'tel': telefono,
                'direccion': direccion
            }, "clientes")
        return "Cliente ingresado correctamente."
    except Exception as e:
        return "Hubo un error al ingresar el Cliente: " + str(e)


def eliminarCliente(dni):
    res = consultarTabla('dni', dni, "clientes")
    respuesta = ''
    for item in res:
        respuesta = respuesta + f'''
        **************\n
        DNI: {item[1]}\n
        Nombre: {item[2]}\n
        Teléfono: {item[3]}\n
        Dirección: {item[4]}\n
        Estado: -\n
        **************'''
    print(respuesta)

    confirmacion = input(
        "¿Está seguro que desea eliminar este cliente? S/N:\n")

    if confirmacion.upper() == "S":
        try:
            eliminarRegistro(item[0], 'clientes')
            return "Cliente borrado exitosamente"
        except Exception as e:
            return "Ocurrió un error al intentar eliminar: " + str(e)
    elif confirmacion.upper() == "N":
        return "Operación abortada."
    else:
        return "Ingreso no válido"


def modificarCliente(dni):
    #
    item = consultarTabla('dni', dni, "clientes")
    print(item)
    respuesta = ''
    respuesta = respuesta + f'''
        **************\n
        DNI: {item[0][1]}\n
        Nombre: {item[0][2]}\n
        Teléfono: {item[0][3]}\n
        Dirección: {item[0][4]}\n
        Estado: -\n
        **************'''
    print(respuesta)
    print(
        "A continuación modifique los datos del cliente. Si no desea modificar el dato, presione Enter."
    )
    dni = str(input(f'DNI: {item[0][1]}') or str(item[0][1]))
    print("Nuevo valor: " + dni)
    nombre = str(input(f'Nombre: {item[0][2]}') or str(item[0][2]))
    print("Nuevo valor: " + nombre)
    telefono = str(input(f'Teléfono: {item[0][3]}') or str(item[0][3]))
    print("Nuevo valor: " + telefono)
    direccion = str(input(f'Dirección: {item[0][4]}') or str(item[0][4]))
    print("Nuevo valor: " + direccion)
    try:
        modificarRegistro(
            {
                'dni': dni,
                'nombre': nombre,
                'tel': telefono,
                'direccion': direccion
            }, item[0][0], "clientes")
        return "modificado con éxito"
    except Exception as e:
        return "Error: " + str(e)
