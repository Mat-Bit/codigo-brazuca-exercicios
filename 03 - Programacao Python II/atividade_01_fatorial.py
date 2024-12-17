def main():
  n = int(input("Digite um numero inteiro: "))

  print("O fatorial do numero digitado eh:", fat(n))


def fat(number):
  if number <= 1:
    return 1
  
  return number * fat(number-1)


if __name__ == "__main__":
  main()