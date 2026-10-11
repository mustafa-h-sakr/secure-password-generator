import secrets
import random
numbers_count = 0
uppercase_count = 0
lowercase_count = 0
symbols_count = 0

def user_action(action, question_value):
    while True:
        try:
            if action.lower() == 'y':
                return True
            elif action.lower() == 'n':
                return False
            else:
                raise ValueError

        except ValueError:
            print("Invalid input! Please enter y or n.")
            action = input(question_value)

def numbrer_transformer(question_value,Number_of_available_spaces):
    while True:
      try: 
          character_value = int(input(question_value))
          if  character_value <= Number_of_available_spaces and character_value > 0 :
              return character_value
      
          else:
              print("Password length must be less than",Number_of_available_spaces)
      except ValueError:
           print("Invalid input! Please enter a number.")



while True:
    try:
        password_length = int(input("Enter password length (greater than 8 and less than 20): "))
        if password_length >= 8 and password_length <= 20:
            break
        else:
            print("Password length must be greater than or equal 8")
    except ValueError:
        print("Invalid input! Please enter a number.")


include_numbers = input("Do you want to include numbers? (y/n)")
if user_action(include_numbers,"Do you want to include numbers? (y/n)"):
   numbers_count =  numbrer_transformer("How many numbers do you want: ",password_length)

if password_length-numbers_count > 0 :
   include_uppercase = input("Do you want to include uppercase letters? (y/n)")
   if user_action(include_uppercase,"Do you want to include uppercase letters? (y/n)"):
      uppercase_count = numbrer_transformer("How many uppercase do you want: ",password_length-numbers_count)

if password_length-(numbers_count+uppercase_count) > 0 : 
   include_lowercase = input("Do you want to include lowercase letters? (y/n)")
   if user_action(include_lowercase,"Do you want to include lowercase letters? (y/n)"):
      lowercase_count = numbrer_transformer("How many lowercase do you want :",password_length-(numbers_count+uppercase_count))

if password_length-(numbers_count+uppercase_count+lowercase_count) > 0 :
   include_symbols = input("Do you want to include symbols? (y/n)")
   if user_action(include_symbols,"Do you want to include symbols? (y/n)"):
      symbols_count = numbrer_transformer("How many symbols do you want: ",password_length-(numbers_count+uppercase_count+lowercase_count))

characters = {
    "numbers": [
        "0", "1", "2", "3", "4","5", "6", "7", "8", "9"
    ],
    "uppercase": [
        "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L","M",
        "N", "O", "P", "Q", "R","S", "T", "U", "V", "W", "X","Y", "Z"
    ],
    "lowercase": [
        "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l","m",
        "n", "o", "p", "q", "r","s", "t", "u", "v", "w", "x",  "y", "z"
    ],
    "symbols": [
        "!", "@", "#", "$", "%", "^", "&", "*","(", ")", "-", "_", "=", "+", "[", "]",
        "{", "}","|", ";", ":", "'", '"',",", ".", "<", ">", "/", "?", "`", "~", "÷",

    ]
}
x1 = [secrets.choice(characters["numbers"]) for _ in range(numbers_count)]
x2 = [secrets.choice(characters["uppercase"]) for _ in range(uppercase_count)]
x3 = [secrets.choice(characters["lowercase"]) for _ in range(lowercase_count)]
x4 = [secrets.choice(characters["symbols"]) for _ in range(symbols_count)]
x5 = x1 + x2 + x3 + x4

remaining = password_length - len(x5)

x5.extend(
    secrets.choice(characters["lowercase"])
    for _ in range(remaining))

secrets.SystemRandom().shuffle(x5)
password = "".join(x5)
print("Your secret password is:", password)