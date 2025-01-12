from random import randint

if __name__ == "__main__":
    secret_number = randint(1, 100)
    
    palpite = int(input("Adivinhe o número escolhido entre  1 e 100: "))
    
    while secret_number != palpite:
        if palpite < secret_number:
            print("Número é MAIOR que este, tente novamente...")
        else:
            print("Número é MENOR que este, tente novamente...")
        
        palpite = int(input("Novo palpite: "))
    
    print("Parabéns, você adivinhou!!")