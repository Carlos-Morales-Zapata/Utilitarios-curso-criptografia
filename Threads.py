import threading

def worker(num):
  """Función para realizar un trabajo simulado."""
  print(f"Hilo {threading.current_thread().name} procesando: {num}")
  # Simular trabajo computacional
  for i in range(num * 1000):
    pass

# Crear y ejecutar hilos
num_threads = 4
threads = []
for i in range(num_threads):
  thread = threading.Thread(target=worker, args=(i + 1,))
  threads.append(thread)
  thread.start()

# Esperar a que finalicen los hilos
for thread in threads:
  thread.join()
