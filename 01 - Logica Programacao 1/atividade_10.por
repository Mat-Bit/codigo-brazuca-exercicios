programa {
  funcao inicio() {
    inteiro numero, contador = 0

    para (inteiro i = 1; i <= 5; i++) {
      escreva("Digite um número: ")
      leia(numero)

      se (numero > 0) {
        contador++
      }
    }

    escreva("Quantidade de números positivos: ", contador)
  }
}