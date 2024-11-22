def main():
  # Programa que manipula strings
  frase = input("Digite a frase aqui: ")
  letra = input("Qula letra deseja contar: ")
  contador = 0

  for l in frase:
    if l.lower() == letra.lower():
      contador += 1

  print(f"A frase acima possui {contador} letra(s) '{letra}'.")

if __name__ == "__main__":
  main()