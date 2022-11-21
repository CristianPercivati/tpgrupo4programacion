from libros import consultarLibro, ingresarLibro, eliminarLibro, modificarLibro

# A continuación se muestra el correcto uso de las funciones desarrolladas en
# el módulo "libros". La idea es que el desarrollador simplemente pase un
# diccionario con las propiedades pertinentes para realizar una consulta.

modificarLibro({
    'autor': 'Guillermo'
}, 11069)