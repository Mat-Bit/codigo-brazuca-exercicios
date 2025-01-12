from numpy import pi

if __name__ == "__main__":
    raio = float(input("Digite o raio do círculo para calcular a área: "))
    
    area = pi * raio * raio
    
    print("A área do círculo é: ", round(area, 3))