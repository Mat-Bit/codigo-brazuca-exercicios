programa {
  funcao inicio() {
    inteiro numero

    escreva("Digite um número: ")
    leia(numero)

    se (numero > 0) {
      escreva("O fatorial de ", numero, " é ", fatorial(numero))
    }
  }

  funcao inteiro fatorial(inteiro numero) {
    inteiro i, resultado

    resultado = 1

    para (i = 1; i <= numero; i++) {
      resultado = resultado * i
    }

    retorne resultado
  }
}