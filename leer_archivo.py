# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 09:48:45 2023

@author: Alumno
"""

noticia = open("noticia.txt","rt")
datos_noticia = noticia.read()
print(datos_noticia)
noticia = open("noticia.txt","rt",encoding='utf8')
datos_noticia = noticia.read()
print(datos_noticia)
