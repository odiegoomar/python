# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 20:15:06 2019

@author: CEC
"""

def hi(name):
    print("Hi,", name)
    
def hiAll(name1, name2):
    print("Hi,", name2)
    print("Hi,", name1)

hi("Diego")
hiAll("Diego","Ortiz")

def address(street, city, postalCode):
    print("Your address is:", street, "St.,", city, postalCode)
    
s = input("Street: ")
pC = input("Postal Code: ")
c = input("City: ")

address(s, c, pC)

#1era forma de pasa parametros
def subtra(a, b):
    print(a - b)
    
subtra(5, 2)
subtra(2, 5)

#2da froma de pasar parametros
def subtra(a, b):
    print(a - b)
    
subtra(a=5, b=2)
subtra(b=2, a=5)

#3ra forma de pasar parametros
def subtra(a, b):
    print(a - b)
    
subtra(5, b=2)
subtra(5, 2)
