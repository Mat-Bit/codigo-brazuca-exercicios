if __name__ == "__main__":
    soma_pares = 0
    range_sup = 100
    
    for i in range(1, range_sup + 1):
        if i % 2 == 0:
            soma_pares += i
    
    print("O resultado da soma de números pares entre 1 e", range_sup, "é:", soma_pares)