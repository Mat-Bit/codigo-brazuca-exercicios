def main():
  # Programa que solicite um número ao usuário e informe se ele é par ou ímpar
  number = int(input("Digite um número: "))
  even_or_odd(number)
  

def even_or_odd(number):
  if number % 2 == 0:
    print("O número é par.")
  else:
    print("O número é ímpar.")
      

if __name__ == "__main__":
  main()