def main():
  # Programa que cria lista de compras, podendo adicionar itens e imprimir a lista
  lista_compras = []
  print("Sua lista de compras está vazia.")

  while True:
    opcao = int(input("Digite 1 para adicionar um item na lista, 2 para imprimir a lista ou 0 para sair: "))
    if opcao == 0:
      break
    elif opcao == 1:
      item = input("Digite o item que deseja adicionar na lista: ")
      lista_compras.append(item)
    elif opcao == 2:
      print("Sua lista de compras:")
      for item in lista_compras:
        print(f"- {item};")
    else:
      print("Opção inválida.")
      

if __name__ == "__main__":
  main()