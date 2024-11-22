def main():
  # Programa solicite ao usuário números e imprima a soma deles
  # O programa deve parar de solicitar números quando o usuário digitar 0
  soma = 0
  numero = int(input("Digite um número: "))
  while numero != 0:
    soma += numero
    numero = int(input("Digite outro número: "))

  print(f"A soma dos números digitados é: {soma}")


if __name__ == "__main__":
  main()