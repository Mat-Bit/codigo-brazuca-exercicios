def main():
  temp_c = float(input("Qual a temperatura atual em graus Celsius: "))

  temp_f = (temp_c * 9/5) + 32
  temp_k = temp_c + 273.15

  print("\nA temperatura informada em Fahrenheit (°F) eh:", temp_f)
  print("A temperatura informada em Kelvin (°K) eh:", temp_k)


if __name__ == "__main__":
  main()