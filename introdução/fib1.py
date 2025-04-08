

def fibonacci(n):
    a,b = 0,1

    for _ in range(n):
            a, b = b, a + b

    return a 

resultado = fibonacci(1)
print(f"{resultado}")

def fibonacci_recursivo(n):
      if n <= 1:
            return 1
      
      return fibonacci_recursivo(n-1) + fibonacci_recursivo(n-2)

for n in range(40):
      print(fibonacci_recursivo(n), end= " | ")