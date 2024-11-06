programa {
  funcao inicio() {
    inteiro numero, i

    escreva("Digite um número: ")
    leia(numero)

    escreva("Tabuada do ", numero, ":\n")

    para (i = 1; i <= 10; i++) {
      escreva(numero, " x ", i, " = ", numero * i, "\n")
    }
  }
}