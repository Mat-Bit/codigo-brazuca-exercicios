fn main() {
    let numbers = [7.5, 8.0, 10.45];
    let sum: f64 = numbers.iter().sum();
    let count = numbers.len();
    let average = sum / count as f64;
    println!("A média é: {:.2}", average);
}
