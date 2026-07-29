# 🔐 Secure Password Generator

A robust, user-friendly Python-based password generation tool that creates strong, customizable passwords with real-time complexity assessment.

## 📋 Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Security Considerations](#security-considerations)
- [Code Structure](#code-structure)
- [Contributing](#contributing)
- [License](#license)

## ✨ Features

- **Customizable Character Sets**: Choose from lowercase, uppercase, numbers, and special symbols
- **Minimum Length Enforcement**: Ensures passwords meet security standards (minimum 8 characters)
- **Input Validation**: Robust error handling for all user inputs
- **Security Assessment**: Provides instant complexity feedback (Strong/Weak)
- **Secure Generation**: Uses Python's `random` module with cryptographically secure pseudo-random number generation
- **User-Friendly Interface**: Clear prompts and visual feedback

## 🚀 Installation

### Prerequisites
- Python 3.6 or higher

### Setup

Clone the repository:
```bash
git clone https://github.com/yourusername/password-generator.git
cd password-generator
```

No additional dependencies required - uses only Python's standard library!

## 💻 Usage

Run the script directly:
```bash
python password_generator.py
```

### Interactive Example

```
🔐 Secure Password Generator
------------------------------
Enter password length (min 8): 16
Include uppercase letters? (y/n): y
Include numbers? (y/n): y
Include symbols? (y/n): y

Generated Password: K#8mP$2nL@4qR!9v
Length: 16 characters
Complexity: Strong
```

### Input Options

| Input | Description |
|-------|-------------|
| **Length** | Minimum 8 characters, no upper limit |
| **Uppercase** | Include A-Z characters |
| **Numbers** | Include 0-9 digits |
| **Symbols** | Include !@#$%^&*()_+-=[]{}|;:,.<>? |

## 🛡️ Security Considerations

- **Minimum Length**: Enforces 8-character minimum to resist brute-force attacks
- **Character Diversity**: Encourages using multiple character types for stronger passwords
- **Complexity Assessment**: Provides instant feedback on password strength
- **Secure Generation**: Utilizes Python's `random.choice()` with system randomness

⚠️ **Note**: For maximum security, always use unique passwords for different services and consider using a password manager.

## 🏗️ Code Structure

```
password_generator/
├── password_generator.py    # Main application
├── README.md               # Documentation
└── LICENSE                 # MIT License
```

### Key Functions

- `get_user_preferences()`: Handles user input with validation
- `generate_password()`: Core password generation logic
- `main()`: Orchestrates the application flow

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Contribution Guidelines
- Ensure code follows PEP 8 style guide
- Add comments for complex logic
- Update documentation as needed
- Test changes thoroughly

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with Python's standard library
- Inspired by best practices in password security
- Thanks to the open-source community for security insights

## 📊 Security Best Practices

When using this generator, remember:
- ❌ Never share passwords via email or messaging
- ✅ Use different passwords for different accounts
- ✅ Consider using a password manager
- ✅ Enable 2FA wherever possible

---

**Built with ❤️ for better password security**
