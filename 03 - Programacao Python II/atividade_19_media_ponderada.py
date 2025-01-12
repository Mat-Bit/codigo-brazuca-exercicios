if __name__ == "__main__":
    notas_str = input("Digite as 3 notas para calcular a média ponderada: ")
    
    notas = notas_str.split()
    pesos = [2, 3, 5]
    resultado = 0
    
    for i in range(len(notas)):
        resultado += float(notas[i]) * pesos[i]
    
    resultado = resultado / 10
    
    print("A média ponderada das notas são:", round(resultado))