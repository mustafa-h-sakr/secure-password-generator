Secure Password Generator 🔐

A command-line password generator built with Python's secrets module. Generate passwords with a customizable length and choose how many numbers, uppercase letters, lowercase letters, and symbols to include.

✨ Features
Custom Password Length: Choose a password length between 8 and 20 characters.
Flexible Character Selection: Decide whether to include numbers, uppercase letters, lowercase letters, and symbols.
Custom Character Counts: Specify how many characters of each selected type to include.
Secure Randomness: Uses Python's built-in secrets module for security-oriented random selection.
Shuffled Output: Shuffles the generated characters to avoid grouping them by type.
No External Dependencies: Uses Python's standard library.
🛠️ Built With
Python
secrets — secure random selection and shuffling
input() and exception handling — interactive command-line experience
📋 Requirements
Python 3.8 or newer
No third-party packages required
🚀 Getting Started
1. Clone the repository
git clone https://github.com/mustafa-h-sakr/secure-password-generator


Replace YOUR_USERNAME with your GitHub username.

2. Navigate to the project directory
cd secure-password-generator

3. Run the program
python secure-password-generator.py


If your system uses python3, run:

python3 secure-password-generator.py

💻 Example Usage
Enter password length (greater than 8 and less than 20): 12
Do you want to include numbers? (y/n)y
How many numbers do you want: 3
Do you want to include uppercase letters? (y/n)y
How many uppercase do you want: 3
Do you want to include lowercase letters? (y/n)y
How many lowercase do you want :4
Do you want to include symbols? (y/n)y
How many symbols do you want: 2

Your secret password is: [generated password]


The generated password will vary each time you run the program.

🔒 Security Notes
Password characters are selected using Python's secrets module rather than the standard random module.
The program is intended as a learning project and a basic command-line utility.
Review the generated password and your organization's password requirements before using it for important accounts.
Never commit real passwords, API keys, or other secrets to a public repository.
🗺️ Roadmap

Planned improvements for future releases:

Support password lengths beyond 20 characters.
Improve input validation and error messages.
Allow users to exclude ambiguous characters.
Add an option to copy the generated password to the clipboard.
Add automated tests.
Add a command-line interface using command-line arguments.
Add configuration options for password policies.
📁 Project Structure
secure-password-generator/
├── secure-password-generator.py
├── README.md
├── LICENSE
├── CHANGELOG.md
└── .gitignore

📌 Versioning

This project follows Semantic Versioning.

PATCH (1.0.1): Bug fixes.
MINOR (1.1.0): Backward-compatible features.
MAJOR (2.0.0): Significant changes that may break compatibility.

See CHANGELOG.md for release history.

👨‍💻 Author

Mostafa Hamdy Abdel Fattah

GitHub: @YOUR_USERNAME

📄 License

This project is licensed under the MIT License. See the LICENSE file for details.

If you find this project useful, consider giving it a ⭐ on GitHub!
