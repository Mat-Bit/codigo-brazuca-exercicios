if __name__ == "__main__":
    print("Calculadora express")
    
    expressao = input("Digite a conta que deseja realizar: ")
    
    num1, op, num2 = expressao.split()
    
    if op not in ['+', '-', '*', '/']:
        print("A operação não é válida")
        exit(1)
    
    num1 = float(num1)
    num2 = float(num2)
    
    if op == '+':
        resultado = num1 + num2
    elif op == '-':
        resultado = num1 - num2
    elif op == '*':
        resultado = num1 * num2
    else:
        resultado = num1 / num2
    
    print("O resultado da expressão é:", round(resultado, 2))