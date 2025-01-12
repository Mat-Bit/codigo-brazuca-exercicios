if __name__ == "__main__":
    num = int(input("Digite um número natural: "))
    
    soma = 0
    for i in range(num+1):
        soma += i
    
    print("A soma dos números até o", num, "é:", soma)