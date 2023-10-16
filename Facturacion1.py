# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 09:27:13 2023

@author: Alumno
"""

# Dado el subtotal, calcular el IGV y el total

import financieros
subtotal = 800.77
print(f"Subtotal: {subtotal}")
print(f"IGV: {financieros.obtenerIGVconSubtotal(subtotal): .2f}")
print(f"Total: {financieros.obtenerTotalconSubtotal(subtotal):.2f}")
