fn main() {
    // Comparacao exata
    let cor = "azul";
    match cor {
        "azul" => println!("A cor é azul"),
        "vermelho" => println!("A cor é vermelho"),
        "verde" => println!("A cor é verde"),
        _ => println!("A cor não é azul, vermelho ou verde"),
    }

    // Intervalo de valores
    let age = 18;
    match age {
        0..=12 => println!("Criança"),
        13..=17 => println!("Adolescente"),
        18..=64 => println!("Adulto"),
        _ => println!("Idoso"),
    }

    // Desestruturacao
    let point = (0, 7);
    match point {
        (0, 0) => println!("Origem"),
        (0, y) => println!("Eixo Y: {}", y),
        (x, 0) => println!("Eixo X: {}", x),
        (x, y) => println!("Ponto: ({}, {})", x, y),
    }

    // Binding
    let value = Some(5);
    match value {
        Some(v) if v > 0 => println!("Valor positivo: {}", v),
        Some(v) => println!("Valor: {}", v),
        None => println!("Nenhum valor"),
    }

    // Guard clause
    let number_2 = 8;
    match number_2 {
        n if n % 2 == 0 => println!("{} é par", n),
        _ => println!("{} é ímpar", number_2),
    }

    // Retomar valores
    let number_3 = 5;
    let description = match number_3 {
        1 => "Um",
        2 => "Dois",
        3 => "Três",
        _ => "Outro número",
    };
    println!("Descrição: {}", description);

    // Combinacao de padroes
    let number_4 = 3;
    match number_4 {
        1 | 2 | 3 => println!("Número pequeno"),
        4..=6 => println!("Número médio"),
        _ => println!("Número grande"),
    }
}
