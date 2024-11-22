def main():
  # Programa que solicita dois numeros e imprime as operações matemáticas entre eles

  num1 = float(input("Digite o primeiro número: "))
  num2 = float(input("Digite o segundo número: "))

  print("A soma entre", num1, "e", num2, "é", num1 + num2)
  print("A subtração entre", num1, "e", num2, "é", num1 - num2)
  print("A multiplicação entre", num1, "e", num2, "é", num1 * num2)
  print("A divisão entre", num1, "e", num2, "é", num1 / num2)
  

if __name__ == "__main__":
  main()