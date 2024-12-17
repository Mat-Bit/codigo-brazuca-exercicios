def fibonacci(n):
  if n <= 1:
    return n
  else:
    return fibonacci(n - 1) + fibonacci(n - 2)
  

if __name__ == "__main__":
  n = int(input("Digite um número inteiro: "))
  for i in range(n):
    print(f"Termo {i+1} =  {fibonacci(i)}")