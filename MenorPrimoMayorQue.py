import datetime

def is_prime(number):
  """
  Determina si un número es primo.

  Args:
    number: El número entero que se evalúa como primo.

  Returns:
    True si el número es primo, False si no lo es.
  """
  if number <= 1:
    return False
  if number <= 3:
    return True
  if number % 2 == 0 or number % 3 == 0:
    return False
  i = 5
  while i * i <= number:
    if number % i == 0 or number % (i + 2) == 0:
      return False
    i += 6
  return True

# Iniciar la búsqueda a partir de 10,000,001
numberi = int(input("Ingrese un número para buscar primo mayor: "))
# Leer el tiempo inicial
TInicio = datetime.datetime.now()

if numberi%2==0:
  number=numberi+1
else:
  number=numberi+2

# Buscar el primer número primo mayor a "number"
while not is_prime(number):
  number += 2  # Solo se evalúan números impares

# Mostrar el primer número primo encontrado
print(f"El menor número primo mayor a {numberi} es: {number}")

# Calcular el tiempo transcurrido
TFin = datetime.datetime.now() - TInicio
print(f"Tiempo total: {TFin}")
