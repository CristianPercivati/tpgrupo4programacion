from db import dbQuery

#Lo que hace cada función es elaborar un diccionario directamente
#formateado desde los datos ingresados, para que los módulos de DB 
#puedan realizar las consultas sin ningún tipo de operación, sencillamente
#tomando los ítems correspondientes..

def consultarLibro(params):
    consulta = {
        'tabla': 'libros',
        'campo': ','.join(params),
        'parametro': ','.join([params[param] for param in params])

    }
#    dbQuery('select', consulta)

def consultarEstadoLibro(params):
    consulta = {
        'tabla': params['tabla'],
        'tablasForaneas': [f'{param[0]} ON {param[1]}={param[2]}' for param in params['tablasForaneas']],
        'campos': ','.join(params['campos']),
        'parametro': params['parametro']
    }
    return consulta
    

def ingresarLibro(params):
    consulta = {
        'tabla': params['tabla'],
        'campos': 'titulo,autor,isbn',
        'valores': ','.join([params['titulo'],params['autor'],str(params['isbn'])])
    }
    return consulta

def eliminarLibro(params):
    consulta = {
        'tabla': params['tabla'],
        'parametro': params['parametro']
    }
    return consulta
    
def modificarLibro(params):
    consulta = {
    'tabla': params['tabla'],
    'campos': ','.join([param for param in params['camposValores']]),
    'valores': ','.join([params['camposValores'][param] for param in params['camposValores']]),
    'parametro': params['parametro']
    }
    return consulta

#def prestarLibro():


