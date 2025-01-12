if __name__ == "__main__":
    numero = int(input("Digite um número para verificar se é perfeito: "))
    
    soma_divisores = 0
    
    for i in range(1, (numero // 2) + 1):
        if numero % i == 0:
            soma_divisores += i
    
    if numero == soma_divisores:
        print("Parabéns achou um número perfeito!!")
    else:
        print("O número não é perfeito... tente outra vez")