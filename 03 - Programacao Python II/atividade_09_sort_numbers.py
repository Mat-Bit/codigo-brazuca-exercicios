def sort_numbers(n1, n2):
    if n1 > n2:
        return n2, n1
    return n1, n2 

if __name__ == '__main__':
  print("Digite três números inteiros:")
  n1 = int(input())
  n2 = int(input())
  n3 = int(input())

  n1, n2 = sort_numbers(n1, n2)
  n1, n3 = sort_numbers(n1, n3)
  n2, n3 = sort_numbers(n2, n3)

  print("Os numeros ordenados de forma crescente sao:", n1, n2, n3)