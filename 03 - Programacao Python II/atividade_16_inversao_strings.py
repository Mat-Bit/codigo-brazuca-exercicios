if __name__ == "__main__":
    palavra = input("Digite uma palavra e veja a mesma invertida: ")
    
    inv_palavra = ''
    
    for p in range(0, len(palavra)):
        print(palavra[p])
        inv_palavra += palavra[len(palavra) - (p +1)]
    
    print("A palavra invertida é:", inv_palavra)