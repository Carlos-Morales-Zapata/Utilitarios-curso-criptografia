import datetime

def find_prime_factors(number):
  """
  Encuentra los factores primos de un número entero positivo.

  Args:
    number: El número entero positivo para el que se buscan los factores primos.

  Returns:
    Una lista que contiene los factores primos del número dado, o un mensaje de error si el número no es válido.
  """
  if number <= 1:
    return "No hay factores primos para números menores o iguales a 1."
  factors = []
  i = 2
  while i * i <= number:
    while number % i == 0:
      factors.append(i)
      number //= i
    i += 1
  if number > 1:
    factors.append(number)
  return factors

# Solicitar el número al usuario
number = int(input("Ingrese un número entero positivo: "))

# Inicializa cronometro 
TInicio = datetime.datetime.now()

# Encontrar y mostrar los factores primos
prime_factors = find_prime_factors(number)
if prime_factors:
  # Calcular y mostrar el tiempo transcurrido
  TFin = datetime.datetime.now() - TInicio
  print(f"Tiempo total: {TFin}")

  # Muestra los factores primos
  print(f"Los factores primos de {number} son:", prime_factors)
else:
  print(f"El número {number} no tiene factores primos.")
