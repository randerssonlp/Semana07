# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 09:55:56 2023

@author: Alumno
"""

archivo = open("noticia.txt","at")
# \n es para agregar el contenido en una línea al final
contenido="\nFuente: RPP"

archivo.write(contenido)

archivo.close()
