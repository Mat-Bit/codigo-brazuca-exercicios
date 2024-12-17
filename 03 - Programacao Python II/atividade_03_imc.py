def main():
  altura = float(input("Digite sua altura (em metros): "))

  peso = float(input("Digite seu peso (em kilogramas): "))

  imc = peso / (altura * altura)

  print(f"Seu IMC eh: {imc:.2f}")


if __name__ == "__main__":
  main()