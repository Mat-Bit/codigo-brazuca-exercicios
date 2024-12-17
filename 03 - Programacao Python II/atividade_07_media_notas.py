def calcular_media_notas():
  notas = []
  while True:
    nota = float(input("Digite uma nota: "))
    if nota == -1:
      break
    try:
      notas.append(nota)
    except ValueError:
      print("Por favor, insira um valor numérico válido.")
  
  if notas:
    media = sum(notas) / len(notas)
    print(f"A média das notas inseridas é: {media:.2f}")
  else:
    print("Nenhuma nota foi inserida.")

if __name__ == "__main__":
  calcular_media_notas()