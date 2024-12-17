def tabuada(numero):
  for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")


if __name__ == "__main__":
  numero = int(input("Digite um número para ver a tabuada: "))
  tabuada(numero)