# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 20:02:11 2019

@author: CEC
"""
"""
import math
x = float(input("Enter x:"))
y = math.sqrt(x)
print("The square root of", x, "equals to", y)

value = 1
value /= 0

#Manejo de excepciones

try:
    print("1")
    x = 1 / 0
    print("2")
except:
    print("Oh dear, something went wrong..")
    
print("3")


try:
    x = int(input("Enter a number:"))
    y = 1 / x
    print(y)
except ZeroDivisionError:
    print("You cannot divide by zero, sorry.")
except ValueError:
    print("You must enter an integer value.")
except:
    print("Oh dear, something whrn wrong..")
print("THE END")


try:
    y = 1 / 0
except ArithmeticError:
    print("Arithmetic problem!")
except ZeroDivisionError:
    print("Zero Division!")
print("THE END")


def badFun(n):
    try:
        return 1 / n
    except ArithmeticError:
        print("Arithmetic Problem!")
    return None
badFun(0)
print("THE END")

"""

def badFun(n):
    return 1 / n

try:
    badFun(0)
except ArithmeticError:
    print("What happened? An exception was raised!")
print("THE END")