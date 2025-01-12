from numpy import average

if __name__ == "__main__":
    lista_raw = input("Insira uma lista de números: ")
    
    lista = list(map(float, lista_raw.split()))
    
    maior = max(lista)
    menor = min(lista)
    media = average(lista)
    
    print("O maior número da lista é:", maior)
    print("O menor número da lista é:", menor)
    print("A média dos valores da lista:", media)