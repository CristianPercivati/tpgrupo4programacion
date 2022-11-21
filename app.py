from db import dbQuery
from libros import consultarLibro, consultarEstadoLibro, ingresarLibro, eliminarLibro, modificarLibro

# A continuación se muestra el correcto uso de las funciones desarrolladas en
# el módulo "libros". La idea es que el desarrollador simplemente pase un
# diccionario con las propiedades pertinentes para realizar una consulta.

print(
    consultarLibro(
    {
        'autor': 'J.K. Rowling',
        }
    )
)

print(
    ingresarLibro(
        {
            'tabla': 'tabla1',
            'titulo': 'prueba',
            'autor': 'prueba2',
            'isbn': 1231242
        }
    )
)

print(
    eliminarLibro(
        {
            'tabla': 'tabla1',
            'parametro': 'id=10'
        }
    )
)

print(
    modificarLibro(
        {
            'tabla': 'tabla1',
            'camposValores': {
                'campo1': 'asd',
                'campos2': 'asd2'
            },
            'parametro': 'id=10'
        }
    )
)

print(
    consultarEstadoLibro(
        {
            'tabla': 'tabla1',
            'tablasForaneas': (
                #En este item, lo que hago es pasar una tupla de listas que contienen
                #tanto las tablas foráneas como las claves relacionadas en ON.
                ['tabla2','pktabla2','fktabla1'],
                ['tabla3','pktabla2','fktabla1']
                ),
            'campos': ['campo1', 'campo2'],
            'parametro': 'campo1 = 2'
        }
    ))

