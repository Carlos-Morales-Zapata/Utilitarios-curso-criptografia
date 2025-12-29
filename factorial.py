import datetime
import sys
sys.set_int_max_str_digits(1000000)

def factorial(numero):
  """
  Calcula el factorial de un número entero no negativo.

  Args:
    numero: El número entero no negativo para el que se calcula el factorial.

  Returns:
    El factorial del número dado, o un mensaje de error si el número no es válido.
  """
  if numero < 0:
    return "El factorial no está definido para números negativos."
  elif numero == 0:
    return 1
  else:
    factorial = 1
    for i in range(1, numero + 1):
      factorial *= i
    return factorial

# Solicitar el número al usuario
numero = int(input("Ingrese un número entero no negativo: "))

# Marcar el inicio
TInicio = datetime.datetime.now()

# Calcular y mostrar el factorial
resultado_factorial = factorial(numero)
TTotal = datetime.datetime.now() - TInicio
print(f"Tiempo total: {TTotal} ")

print(f"El factorial de {numero} es:", resultado_factorial)