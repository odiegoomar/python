# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 08:39:58 2019

@author: CEC
"""

def isPrime(num):
    if num <= 1:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True     

print(isPrime(9))

def primo(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
print(primo(30))

for j in range(1, 30):
    if isPrime(j + 1):
        print(j + 1, end=" ")