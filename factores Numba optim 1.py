from numba import njit
import math
import datetime

# @njit(parallel=True)   --- No es útil en este caso

#@njit
def find_factors(number):
  """
  Encuentra los factores de un número entero positivo.

  Args:
    number: El número entero positivo para el que se buscan los factores.

  Returns:
    Una lista que contiene los factores del número dado, o un mensaje de error si el número no es válido.
  """
  factors = []

  limit = int(math.sqrt(number))
  for i in range(1, limit+1):
    if number % i == 0:
      factors.append(i)
      # si no es la raíz cuadrada, agregamos su cociente
      if i < limit or i*i != number:
        factors.append(number//i)
  return factors

# Solicitar el número al usuario
number = int(input("Ingrese un número entero positivo: "))

# Inicializa cronometro 
TInicio = datetime.datetime.now()

# Encontrar y mostrar los factores
res_factors = find_factors(number)
res_factors.sort() # Ordenamos para que se vea bien
if res_factors:
  # Calcular y mostrar el tiempo transcurrido
  TFin = datetime.datetime.now() - TInicio
  print(f"Tiempo total: {TFin}")

  print(f"Los factores de {number} son:", res_factors)
else:
  print(f"El número {number} no tiene factores.")
