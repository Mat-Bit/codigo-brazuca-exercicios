def main():
  # Encontre todos os números primos dentro de um intervalo específico
  number_range = input("Digite dois números (separados por vírgula) e descubra todos os números primos entre eles: ").split(',')
  begin_range = int(number_range[0])
  end_range = int(number_range[1])

  if end_range < begin_range:
    aux = begin_range
    begin_range = end_range
    end_range = aux

  save_primes = []
  for i in range(begin_range, end_range + 1):
    if is_prime(i):
      save_primes.append(i)

  print(f"Os números primos entre {begin_range} e {end_range} sao:")
  print(save_primes)


def is_prime(number):
  if number <= 1:
    return False
  
  for i in range(2, int(number // 2) +1):
    if number % i == 0:
      return False
    
  return True


if __name__ == "__main__":
  main()