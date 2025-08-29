fn main() {
    let a: i32 = 8;
    let b: i32 = 3;
    
    let soma = a + b;
    let subtracao = a - b;
    let multiplicacao = a * b;
    let divisao = if b != 0 { Some(a / b) } else { None };

    let maior = a > b;
    let soma_par = soma % 2 == 0;

    println!("Resultados:");
    println!("Soma: {}", soma);
    println!("Subtração: {}", subtracao);
    println!("Multiplicação: {}", multiplicacao);

    match divisao {
        Some(valor) => println!("Divisão: {}", valor),
        None => println!("Divisão: Não é possível dividir por zero"),
    }

    println!("Maior: {}", maior);
    println!("Soma de 'a' com 'b' é par: {}", soma_par);
}
