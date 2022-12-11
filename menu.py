from libros import consultarLibro, ingresarLibro, eliminarLibro, modificarLibro
from clientes import consultarCliente, eliminarCliente, modificarCliente, ingresarCliente
from prestamos import consultarPrestamo, eliminarPrestamo, historialPrestamo, ingresarPrestamo
import sys
import os
from style import stylePrincipal, styleSubmenuConDisp, styleSubmenuConPrest, styleGestionPrestamo, styleGestionLibro, styleConsultarLibro, styleGestionCliente, styleConsultarCliente, styleResultadoLibros, styleResultadoClientes, styleResultadoHistorialDNI, styleResultadoHistorialISBN


menu = 0
subOpciones = ''

def limpioPantalla():
	sisOper = os.name
	if sisOper == "posix":   # si fuera UNIX, mac para Apple, java para maquina virtual Java
		os.system("clear")
	elif sisOper == "ce" or sisOper == "nt" or sisOper == "dos":  # windows
		os.system("cls")

def pausarPantalla():
    input("Presione cualquier tecla para volver al menú...")

def submenuConsultarCliente():
    limpioPantalla()
    tabla = "clientes"
    subOpciones = styleConsultarCliente()
    if subOpciones == 'N':
        consulta = input("Escriba el nombre (o parte del nombre) del cliente:: ")
        resultado = consultarCliente('nombre', consulta)
        estilo=styleResultadoClientes(resultado)
        print(estilo)
        pausarPantalla()
        return
    elif subOpciones == 'T':
        consulta = input("Escriba el teléfono del cliente: ")
        consultarCliente('tel', consulta)
        return
    elif subOpciones == 'A':
        consulta = input("Escriba la dirección del cliente: ")
        consultarCliente('direccion', consulta)
        return
    elif subOpciones == 'D':
        consulta = input("Escriba el DNI del cliente: ")
        consultarCliente('dni', consulta)
        return
    elif subOpciones == 'V':
        menu_principal(menu)
    else:
        print('\nSeleccione opción valida \n')
        gestion_cliente(subOpciones)

def submenuAltaCliente():
    dni = input("Ingrese el DNI: ")
    nombre = input("Ingrese el nombre: ")
    telefono = input("Ingrese el teléfono: ")
    direccion = input("Ingrese la direccion: ")
    respuesta = ingresarCliente(dni, nombre, telefono, direccion)
    print(respuesta)
    return

def submenuModificarCliente():
    dni = input("Ingrese el DNI: ")
    respuesta = modificarCliente(dni)
    print(respuesta)
    return

def submenuEliminarCliente():
    dni = input("Ingrese el DNI: ")
    respuesta = eliminarCliente(dni)
    print(respuesta)
    return

def gestion_cliente(subOpciones):
    limpioPantalla()
    subOpciones = styleGestionCliente()
    if subOpciones == 'A':
        submenuAltaCliente()
        menu_principal(0)
    elif subOpciones == 'C':
        print('CONSULTA ESTADO DEL CLIENTE')
        submenuConsultarCliente()
        menu_principal(0)
    elif subOpciones == 'M':
        print('MODIFICAR TELEFONO O DIRECCION DEL CLIENTE')
        submenuModificarCliente()
        menu_principal(0)
    elif subOpciones == 'E':
        print('ELIMINAR CLIENTE')
        submenuEliminarCliente()
        menu_principal(0)
    elif subOpciones == 'V':
        menu_principal(menu)
    else:
        print('\nSeleccione opción valida \n')
        gestion_cliente(subOpciones)


def submenuConsultarLibro():
    limpioPantalla()
    tabla = "libros"
    subOpciones = styleConsultarLibro()
    if subOpciones == 'A':
        consulta = input("Escriba el nombre del autor: ")
        resultado = consultarLibro('autor', consulta)
        estilo=styleResultadoLibros(resultado)
        print(estilo)
        pausarPantalla()
        return
    elif subOpciones == 'T':
        consulta = input("Escriba el título del libro: ")
        consultarLibro('titulo', consulta)
        return
    elif subOpciones == 'I':
        consulta = input("Escriba el ISBN: ")
        consultarLibro('ISBN', consulta)
        return
    elif subOpciones == 'V':
        menu_principal(menu)
    else:
        print('\nSeleccione opción valida \n')
        gestion_libro(subOpciones)

def submenuAltaLibro():
    autor = input("Ingrese el autor: ")
    titulo = input("Ingrese el título: ")
    isbn = input("Ingrese el ISBN: ")
    respuesta = ingresarLibro(autor, titulo, isbn)
    print(respuesta)
    return

def submenuEliminarLibro():
    isbn = input("Ingrese el ISBN: ")
    respuesta = eliminarLibro(isbn)
    print(respuesta)
    return

def submenuModificarLibro():
    isbn = input("Ingrese el ISBN: ")
    respuesta = modificarLibro(isbn)
    print(respuesta)
    return


def gestion_libro(subOpciones):
    limpioPantalla()
    subOpciones = styleGestionLibro()
    if subOpciones == 'A':
        submenuAltaLibro()
        menu_principal(0)
    if subOpciones == 'C':
        submenuConsultarLibro()
        menu_principal(0)
    elif subOpciones == 'M':
        submenuModificarLibro()
        menu_principal(0)
    elif subOpciones == 'E':
        submenuEliminarLibro()
        menu_principal(0)
    elif subOpciones == 'V':
        menu_principal(menu)
    else:
        print('\nSeleccione opción valida \n')
        gestion_libro(subOpciones)



def gestion_Prestamo(subOpciones):
    limpioPantalla()
    subOpciones=styleGestionPrestamo()
    if subOpciones == 'A':
        submenuAltaPrestamo()
        menu_principal(0)
    elif subOpciones == 'C':        
        submenuConsultarPrestamo()
        menu_principal(0)
    elif subOpciones == 'H':
        submenuHistorialPrestamo()
        menu_principal(0)
    elif subOpciones == 'E':
        submenuEliminarPrestamo()
        menu_principal(0)
    elif subOpciones == 'V':
        menu_principal(menu)
    else:
        print('\nSeleccione opción valida \n')
        gestion_Prestamo(subOpciones)


def submenuConsultarPrestamo():
    limpioPantalla()
    tabla = "prestamos"
    subOpciones = styleSubmenuConPrest()    
    if subOpciones == 'L':
        consulta = input("ISBN del libro: ")
        resultado = consultarPrestamo('isbn', consulta)
        print(resultado)
        pausarPantalla()
        return
    elif subOpciones == 'S':
        consulta = input("ID del socio: ")
        consultarPrestamo('fk_cliente', consulta)
        return
    elif subOpciones == 'F':
        consulta = input("Escriba la fecha del Prestamo: ")
        consultarPrestamo('fecha_prestamo', consulta)
        return
    elif subOpciones == 'V':
        menu_principal(menu)
    else:
        print('\nSeleccione opción valida \n')
        gestion_Prestamo(subOpciones)

def submenuAltaPrestamo():
    ISBN = input("Ingrese el ISBN del libro: ")
    DNI = input("Ingrese el DNI del cliente: ")
    fecha_prestamo = input("Ingrese La fecha de préstamo: ")
    
    respuesta = ingresarPrestamo(ISBN, DNI, fecha_prestamo, estado=1)
    print(respuesta)
    pausarPantalla()
    return

def submenuHistorialPrestamo():
    opcion = input("Ingrese D para buscar por DNI o I para buscar por ISBN.")
    if opcion=="D":
        res = historialPrestamo(input("Ingrese el número de DNI."), "dni")
        style=styleResultadoHistorialDNI(res)
        print(style)
        pausarPantalla()
        return
    elif opcion=="I":
        res = historialPrestamo(input("Ingrese el número de ISBN."), "isbn")
        style=styleResultadoHistorialISBN(res)
        print(style)
        pausarPantalla()
        return
    else:
        print("Valor no válido.")
        pausarPantalla()
        return

def submenuEliminarPrestamo():
    ISBN = input("Ingrese el ISBN: ")
    respuesta = eliminarPrestamo(ISBN)
    print(respuesta)
    pausarPantalla()
    return

def submenuConsultarDisponibilidad():
    limpioPantalla()
    tabla = "prestamos"
    subOpciones = styleSubmenuConDisp()    
    if subOpciones == 'L':
        consulta = input("ISBN del libro: ")
        resultado = consultarPrestamo('ISBN', consulta)
        if resultado:
            print(resultado)
        else:
            print("El libro se encuentra disponible.")
        return
    elif subOpciones == 'V':
        menu_principal(menu)
    else:
        print('\nSeleccione opción valida \n')
        gestion_Prestamo(subOpciones)

def menu_principal(menu):
    limpioPantalla()
    menu=stylePrincipal()
    if menu == 1:        
        submenuConsultarDisponibilidad()
    elif menu == 2:
        gestion_Prestamo(subOpciones)
    elif menu == 3:
        gestion_cliente(subOpciones)
    elif menu == 4:
        gestion_libro(subOpciones)
    elif menu == 0: 
        limpioPantalla()       
        sys.exit()        
    else:
        print('\nSeleccione opción valida \n')
        menu_principal(menu)


