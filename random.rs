use std::fs::File;
use std::io;
use std::io::prelude::*;
use std::time::Instant;

fn main() {
    let words: Vec<String> = get_words_list();
    let boxed_words: Vec<Box<str>> = create_boxed_list(&words);
    let password: String = get_user_password().trim().to_string();

    let time = Instant::now();
    for word in words.iter() {
      println!("{word}");
        for word_two in boxed_words.iter() {
            let mut new_word = word.clone();
            
            new_word.push_str(&word_two);
            //println!("{new_word\n}");

            if new_word == password {
                println!("{word}");
                println!(
                    "Password found in {} microseconds",
                    time.elapsed().as_millis()
                );
                return;
            }
        }
    }
    println!("passwrd not found");
}

fn get_file_text(text_name: &str) -> String {
    // Create a path to the desired file
    //let path = Path::new(text_name);
    //let display = path.display();
    let mut file = match File::open(text_name) {
        Err(why) => panic!("unable to open {}: {}", text_name, why),
        Ok(file) => file,
    };
    let mut text_contents = String::new();
    match file.read_to_string(&mut text_contents) {
        Err(why) => panic!("unable to read {}: {}", text_name, why),
        Ok(_) => return text_contents,
    }
}

fn get_words_list() -> Vec<String> {
    let dictionary_text = get_file_text("dictionary.txt");

    let mut words: Vec<String> = Vec::new();

    let mut new_word: String = String::new();
    for letter in dictionary_text.chars() {
        if letter == '\n' {
            words.push(new_word);
            new_word = String::new();
        } else {
            new_word.push(letter);
        }
    }

    return words;
}

fn get_user_password() -> String {
    let mut user_password = String::new();
    println!("Enter your password:");

    io::stdin()
        .read_line(&mut user_password)
        .expect("Error parsing input");

    return user_password;
}

fn create_boxed_list(strings: &Vec<String>) -> Vec<Box<str>> {
  let mut new_boxed = Vec::new();

  for string in strings.iter() {
    new_boxed.push(string.clone().into_boxed_str())
  }

  return new_boxed;
}
