import datetime

def find_factors(number):
  """
  Encuentra los factores de un número entero positivo.

  Args:
    number: El número entero positivo para el que se buscan los factores.

  Returns:
    Una lista que contiene los factores del número dado, o un mensaje de error si el número no es válido.
  """
  if number <= 0:
    return "No hay factores para números no positivos."
  factors = []
  for i in range(1, number + 1):
    if number % i == 0:
      factors.append(i)
  return factors

# Solicitar el número al usuario
number = int(input("Ingrese un número entero positivo: "))

# Inicializa cronometro 
TInicio = datetime.datetime.now()

# Encontrar y mostrar los factores
factors = find_factors(number)
if factors:
  # Calcular y mostrar el tiempo transcurrido
  TFin = datetime.datetime.now() - TInicio
  print(f"Tiempo total: {TFin}")

  print(f"Los factores de {number} son:", factors)
else:
  print(f"El número {number} no tiene factores.")
