# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 07:56:50 2021

@author: Interlude
"""
import random

class vehiculos:
    def __init__(self,kilometraje,modelo,precio,inventario):
        self.kilometraje=kilometraje
        self.modelo=modelo
        self.precio=precio
        self.inventario=inventario
        self.codigo='COD'+str(random.randint(10000,20000))