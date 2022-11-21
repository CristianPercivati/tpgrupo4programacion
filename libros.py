from db import dbQuery

def consultarLibro(params):
    consulta = {
        'tabla': 'libros',
        'campo': ','.join(params),
        'parametro': ','.join([params[param] for param in params])

    }
    print(consulta)
    dbQuery('select', consulta)


#def ingresarLibro():
#def eliminarLibro():
#def modificarLibro():
#def consultarEstadoLibro():
#def prestarLibro():


