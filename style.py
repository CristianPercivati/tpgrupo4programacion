def stylePrincipal():
    menu=int(input('''
        ╔══════════════════════════════════════╗
        ║                                      ║     
        ║     MENÚ PRINCIPAL BIBLIOTECA        ║
        ╠══════════════════════════════════════╣
        ║                                      ║
        ║    1.Consulta de disponibilidad      ║
        ║    2.Préstamo de libro               ║
        ║    3.Gestión del cliente             ║
        ║    4.Gestión del libro               ║
        ║    0.Salir                           ║
        ║                                      ║ 
        ╚══════════════════════════════════════╝
        '''))
    return menu
def styleSubmenuConDisp():
    subOpciones=input("""
    ╔══════════════════════════════════════╗
    ║                                      ║     
    ║     CONSULTAR POR:                   ║
    ╠══════════════════════════════════════╣
    ║                                      ║
    ║    L. ID Libro0                      ║
    ║    S. ID Socio                       ║
    ║    F. Fecha Préstamo                 ║
    ║    V.Volver al menú anterior         ║
    ║                                      ║
    ║                                      ║ 
    ╚══════════════════════════════════════╝
    """
    )
    subOpciones = subOpciones.upper()
    return subOpciones
def styleSubmenuConPrest():
    subOpciones = input('''
    ╔══════════════════════════════════════╗
    ║                                      ║     
    ║     CONSULTA POR:                    ║
    ╠══════════════════════════════════════╣
    ║                                      ║
    ║    L. ISBN LIBRO                     ║
    ║    S. DNI SOCIO                      ║
    ║    F. FECHA PRÉSTAMO:                ║
    ║    V.Volver al menú anterior         ║
    ║                                      ║
    ║                                      ║ 
    ╚══════════════════════════════════════╝    
    '''
    )
    subOpciones = subOpciones.upper()
    return subOpciones
def styleGestionPrestamo():
    subOpciones = input('''
    ╔══════════════════════════════════════╗
    ║                                      ║     
    ║      GESTIÓN DEL PRESTAMO            ║
    ╠══════════════════════════════════════╣
    ║                                      ║
    ║    A.Alta Prestamo                   ║
    ║    C.Consulta estado del Prestamo    ║
    ║    H.Historiales de Préstamos        ║
    ║    E.Eliminar Prestamo               ║
    ║    V.Volver al menú anterior         ║
    ║                                      ║ 
    ╚══════════════════════════════════════╝    
    '''
    )
    subOpciones = subOpciones.upper()
    return subOpciones
def styleGestionLibro():
    subOpciones = input('''
    ╔══════════════════════════════════════╗
    ║                                      ║     
    ║      GESTIÓN DEL LIBRO               ║
    ╠══════════════════════════════════════╣
    ║                                      ║
    ║    A.Alta Libro                      ║
    ║    C.Consultar Libro                 ║
    ║    M.Modificar Libro                 ║
    ║    E.Eliminar Libro                  ║
    ║    V.Volver al menú anterior         ║
    ║                                      ║ 
    ╚══════════════════════════════════════╝
    '''
    )
    subOpciones = subOpciones.upper()
    return subOpciones
def styleConsultarLibro():
    subOpciones = input('''
    ╔══════════════════════════════════════╗
    ║                                      ║     
    ║     CONSULTAR LIBRO                  ║
    ╠══════════════════════════════════════╣
    ║                                      ║
    ║    A. Autor                          ║
    ║    T. Título                         ║
    ║    I. ISBN                           ║
    ║    V.Volver al menú anterior         ║
    ║                                      ║
    ║                                      ║ 
    ╚══════════════════════════════════════╝
    '''
    )
    subOpciones = subOpciones.upper()
    return subOpciones
def styleGestionCliente():
    subOpciones = input("""
    ╔══════════════════════════════════════╗
    ║                                      ║     
    ║      GESTIÓN DEL CLIENTE             ║
    ╠══════════════════════════════════════╣
    ║                                      ║
    ║    A.Alta Cliente                    ║
    ║    C.Consulta estado del cliente     ║
    ║    M.Modificar datos del cliente     ║
    ║    E.Eliminar cliente                ║
    ║    V.Volver al menú anterior         ║
    ║                                      ║ 
    ╚══════════════════════════════════════╝
    """  
    )
    subOpciones = subOpciones.upper()
    return subOpciones
def styleConsultarCliente():
    subOpciones = input("""
    ╔══════════════════════════════════════╗
    ║                                      ║     
    ║      CONSULTA ESTADO DEL CLIENTE     ║
    ╠══════════════════════════════════════╣
    ║                                      ║
    ║     N. Nombre                        ║
    ║     T. Teléfono                      ║
    ║     A. Dirección                     ║
    ║     D. DNI                           ║
    ║     V.Volver al menú anterior        ║
    ║                                      ║ 
    ╚══════════════════════════════════════╝     
    """
    )
    subOpciones = subOpciones.upper()
    return subOpciones

def styleResultadoLibros(res):
    subOpciones ="""
     ══════════════════════════════════════
                                                
              RESULTADOS DE LIBROS         
     ══════════════════════════════════════
        Título    ║    Autor    ║   ISBN   
     ══════════════════════════════════════  
    """
    for item in res:
        if len(item[1])>10:
            itemTitulo=item[1][0:10]+"..."
        else:
            itemTitulo=f'{item[1]: <13}'
        if len(item[2])>10:
            itemAutor=item[2][0:10]+"..."
        else:
            itemAutor=f'{item[2]: <13}'
        if len(item[3])<10:
            itemISBN=f'{item[3]: <10}'
        else:
            itemISBN=item[3]
        subOpciones=subOpciones+f"""
     {itemTitulo} {itemAutor} {itemISBN} 
    ══════════════════════════════════════   
          """
    subOpciones = subOpciones.upper()
    print(subOpciones)
    return subOpciones

def styleResultadoClientes(res):
    subOpciones ="""
     ══════════════════════════════════════
                                                
              RESULTADOS DE CLIENTES         
     ══════════════════════════════════════
        Nombre    ║    Tel.     ║   DNI   
     ══════════════════════════════════════  
    """
    for item in res:
        if len(item[2])>10:
            itemNombre=item[2][0:10]+"..."
        else:
            itemNombre=f'{item[2]: <13}'
 
        itemTel=f'{item[3]: <13}'
        itemDNI=f'{item[1]: <10}'
        subOpciones=subOpciones+f"""
     {itemNombre} {itemTel} {itemDNI} 
     ══════════════════════════════════════   
          """
    subOpciones = subOpciones.upper()
    return subOpciones

def styleResultadoHistorialDNI(res):
    subOpciones =f"""
     ══════════════════════════════════════
                                                
             RESULTADOS DE HISTORIAL
             PARA: {res[0][3]}         
     ══════════════════════════════════════
        Libro     ║   Fecha   ║   Estado   
     ══════════════════════════════════════  
    """
    for item in res:
        if len(item[0])>10:
            itemLibro=item[0][0:10]+"..."
        else:
            itemLibro=f'{item[0]: <10}'
 
        itemFecha=f'{item[1]: <13}'
        itemEstado=f'{item[2]: <10}'
        subOpciones=subOpciones+f"""
     {itemLibro} {itemFecha} {itemEstado} 
     ══════════════════════════════════════   
          """
    subOpciones = subOpciones.upper()
    return subOpciones

def styleResultadoHistorialISBN(res):
    subOpciones =f"""
     ══════════════════════════════════════
                                                
             RESULTADOS DE HISTORIAL
             PARA: {res[0][3][0:10]+"..." if len(res[0][3])>9 else res[0][3]}         
     ══════════════════════════════════════
        Cliente   ║   Fecha   ║   Estado   
     ══════════════════════════════════════  
    """
    for item in res:
        if len(item[0])>10:
            itemLibro=item[0][0:10]+"..."
        else:
            itemLibro=f'{item[0]: <10}'
 
        itemFecha=f'{item[1]: <13}'
        itemEstado=f'{item[2]: <10}'
        subOpciones=subOpciones+f"""
     {itemLibro} {itemFecha} {itemEstado} 
     ══════════════════════════════════════   
          """
    subOpciones = subOpciones.upper()
    return subOpciones