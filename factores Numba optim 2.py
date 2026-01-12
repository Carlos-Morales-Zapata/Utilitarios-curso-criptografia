import numpy as np
from numba import njit
import math
import time

@njit
def gcd(a, b):
    """Algoritmo de Euclides para el MCD, acelerado con Numba"""
    while b:
        a, b = b, a % b
    return a

@njit
def pollard_rho(n):
    if n % 2 == 0: return 2
    if n == 1: return 1
    
    x = 2; y = 2; d = 1; c = 1
    
    # Función f(x) = (x^2 + c) % n
    f = lambda x, n, c: (x*x + c) % n
    
    while d == 1:
        x = f(x, n, c)           # La tortuga (1 paso)
        y = f(f(y, n, c), n, c)  # La liebre (2 pasos)
        d = gcd(abs(x - y), n)
        
        if d == n: # Fallo, hay que reintentar con parámetros distintos
            return pollard_rho(n) 
            
    return d

# Ejemplo con un número de 15 dígitos (difícil para el código anterior)
numero_grande = 100000000000031 * 100000000000037 # Producto de dos primos
print(f"Factorizando: {numero_grande}...")

inicio = time.time()
factor = pollard_rho(numero_grande)
fin = time.time()

print(f"Factor encontrado: {factor}")
print(f"Tiempo: {fin - inicio:.5f} segundos")