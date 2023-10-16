# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 09:35:11 2023

@author: Alumno
"""

# Importamos la libreria
import camelcase

nombre = "raúl andersson lópez puris"

print(nombre.upper())
print(nombre.title())


#Creamos un objeto llamado cam
cam = camelcase.CamelCase()
print("Con camelcase....")

# imprimimos el nombre en formato título
# utilizamos camelcase
print(cam.hump(nombre))

# Para resolver el problema
# creamos otro objeto llamado cam2
# al definir el objeto, incluimos los argumentos
# 'flor' y 'león' 
cam2 = camelcase.CamelCase('raúl','puris')
print(cam2.hump(nombre))
