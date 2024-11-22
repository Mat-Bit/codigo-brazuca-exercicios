def main():
  # Solicite a temperatura e retorne se o tempo está quente, frio ou agradavel
  temperatura = float(input("Digite a temperatura: "))

  if temperatura > 30:
    print("O tempo está quente")
  elif temperatura < 15:
    print("O tempo está frio")
  else:
    print("O tempo está agradável")


if __name__ == "__main__":
  main()