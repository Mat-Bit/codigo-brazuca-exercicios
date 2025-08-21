fn main() {
    const PI: f64 = 3.14159;
    let mut radius = 5.0;
    let area = PI * radius * radius;

    println!("A área do círculo com raio {} é: {}", radius, area);

    radius = 10.0;
    let nova_area = PI * radius * radius;
    println!("A área do círculo com raio {} é: {}", radius, nova_area);
}
