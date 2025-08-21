use regex::Regex;

fn main() {
    // Defining the valid email pattern
    let email_pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$";
    let email_regex = Regex::new(email_pattern).unwrap();

    // Emails list to validate
    let emails = ["test@example.com", "invalid-email", "user@domain.co"];

    // Validating each email
    for email in emails.iter() {
        if email_regex.is_match(email) {
            println!("'{}' is a valid email.", email);
        } else {
            println!("'{}' is not a valid email.", email);
        }
    }
}
