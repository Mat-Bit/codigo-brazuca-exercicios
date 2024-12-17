def main():
  palavra = input("Digite uma palava qualquer: ")

  if palavra == palavra[::-1]:
    print("A palavra é um palíndromo")
  else:
    print("A palavra não é um palíndromo")


if __name__ == "__main__":
  main()