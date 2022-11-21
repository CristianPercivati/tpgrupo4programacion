from db import dbQuery
from libros import consultarLibro

print(
    consultarLibro(
    {
        'autor': 'J.K. Rowling',
        }
    )
)


