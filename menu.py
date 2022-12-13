from libros import consultarLibro, ingresarLibro, eliminarLibro, modificarLibro
from clientes import consultarCliente, eliminarCliente, modificarCliente, ingresarCliente
from prestamos import consultarPrestamo, eliminarPrestamo, historialPrestamo, ingresarPrestamo, consultarDisponibilidadPrestamo
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
        resultado = consultarCliente('tel', consulta)
        estilo=styleResultadoClientes(resultado)
        print(estilo)
        return
    elif subOpciones == 'A':
        consulta = input("Escriba la dirección del cliente: ")
        resultado = consultarCliente('direccion', consulta)
        estilo=styleResultadoClientes(resultado)
        print(estilo)
        return
    elif subOpciones == 'D':
        consulta = input("Escriba el DNI del cliente: ")
        resultado = consultarCliente('dni', consulta)
        estilo=styleResultadoClientes(resultado)
        print(estilo)
        print(resultado)
        pausarPantalla()
        submenuConsultarCliente()
        #return
    elif subOpciones == 'V':
        gestion_cliente(subOpciones)
    elif subOpciones == "0":
        limpioPantalla()
        menu_principal(0)
    else:
        print('\nSeleccione opción valida \n')
        pausarPantalla()
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
    elif subOpciones == 'C':
        print('CONSULTA ESTADO DEL CLIENTE')
        submenuConsultarCliente()        
    elif subOpciones == 'M':
        print('MODIFICAR TELEFONO O DIRECCION DEL CLIENTE')
        submenuModificarCliente()        
    elif subOpciones == 'E':
        print('ELIMINAR CLIENTE')
        submenuEliminarCliente()        
    elif subOpciones == 'V':
        menu_principal(menu)
    elif subOpciones == 0: 
        menu_principal(0)
    else:
        print('\nSeleccione opción valida \n')
        pausarPantalla()
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
        resultado = consultarLibro('titulo', consulta)
        estilo=styleResultadoLibros(resultado)
        print(estilo)
        pausarPantalla()
        return
    elif subOpciones == 'I':
        consulta = input("Escriba el ISBN: ")
        resultado = consultarLibro('ISBN', consulta)
        estilo=styleResultadoLibros(resultado)
        print(estilo)
        pausarPantalla()
        return
    elif subOpciones == 'V':
        gestion_libro(subOpciones)
    elif subOpciones == "0": 
        limpioPantalla()
        menu_principal(0)
    else:        
        print('\nSeleccione opción valida \n')
        pausarPantalla()
        submenuConsultarLibro()

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
    elif subOpciones == "0": 
        limpioPantalla()       
        menu_principal(0)
    else:
        print('\nSeleccione opción valida \n')
        pausarPantalla()
        gestion_libro(subOpciones)


def gestion_Prestamo():
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
        menu_principal(0)
    elif subOpciones == "0": 
        limpioPantalla()       
        sys.exit()
    else:
        print('\nSeleccione opción valida \n')
        pausarPantalla()
        gestion_Prestamo()


def submenuConsultarPrestamo():
    limpioPantalla()
    tabla = "prestamos"
    subOpciones = styleSubmenuConPrest()    
    if subOpciones == 'L':
        consulta = input("ISBN del libro: ")
        resultado = consultarPrestamo('isbn', consulta,"libro")       
        print(resultado)
        pausarPantalla()
        return
    elif subOpciones == 'S':
        consulta = input("DNI del socio: ")
        resultado = consultarPrestamo('dni', consulta,"cliente")
        print(resultado)
        pausarPantalla()
        return
    elif subOpciones == 'V':
        gestion_Prestamo()
    elif subOpciones == "0": 
        limpioPantalla()       
        sys.exit()
    else:
        print('\nSeleccione opción valida \n')
        pausarPantalla()
        submenuConsultarPrestamo()

def submenuAltaPrestamo():
    ISBN = input("Ingrese el ISBN del libro: ")
    DNI = input("Ingrese el DNI del cliente: ")
    #fecha_prestamo = input("Ingrese La fecha de préstamo: ")
    
    respuesta = ingresarPrestamo(ISBN, DNI,  estado=1)
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
    if subOpciones == 'I':
        consulta = input("ISBN del libro: ")
        resultado = consultarDisponibilidadPrestamo('isbn', consulta,"isbn")
        print(resultado)
        pausarPantalla()
        return
    else:
        print('\nSeleccione opción valida \n')
        pausarPantalla()
        submenuConsultarDisponibilidad()

def menu_principal(menu):
    limpioPantalla()
    while True:
        try:
            menu=stylePrincipal()
            if menu == 1:        
                submenuConsultarDisponibilidad()
            elif menu == 2:
                gestion_Prestamo()
            elif menu == 3:
                gestion_cliente(subOpciones)
            elif menu == 4:
                gestion_libro(subOpciones)
            elif menu == 0: 
                limpioPantalla()       
                sys.exit()        
            else:
                print('\nSeleccione opción valida \n')
                pausarPantalla()
                menu_principal(menu)
        except ValueError:
            print('\nSeleccione opción valida \n')
            pausarPantalla()
            menu_principal(menu)
