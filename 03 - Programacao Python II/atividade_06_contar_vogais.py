def contar_vogais(frase):
  vogais = "aeiouAEIOU"
  contador = 0
  for char in frase:
    if char in vogais:
      contador += 1
  return contador


if __name__ == "__main__":
  frase = input("Digite uma frase: ")

  total_vogais = contar_vogais(frase)
  
  print(f"Número de vogais na frase: {total_vogais}")