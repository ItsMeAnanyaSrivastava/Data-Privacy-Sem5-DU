# Data Privacy - Semester 5 (Delhi University)

This repository contains practical implementations for the **Data Privacy** course, offered in the 5th semester at Delhi University. The practicals cover fundamental concepts of cryptography, password security, and digital signatures using Python.

## 📚 Table of Contents

- [About](#about)
- [Practicals Overview](#practicals-overview)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Practical Details](#practical-details)
  - [P1: Caesar Cipher](#p1-caesar-cipher)
  - [P2: Fernet Encryption](#p2-fernet-encryption)
  - [P3: SHA-256 Password Hashing](#p3-sha-256-password-hashing)
  - [P4: Password Leak Checker](#p4-password-leak-checker)
  - [P5: Dictionary-based Password Generator](#p5-dictionary-based-password-generator)
  - [P6: Brute Force Attack Simulation](#p6-brute-force-attack-simulation)
  - [P7: Digital Signature](#p7-digital-signature)
- [License](#license)
- [Contributing](#contributing)

## 🎯 About

This repository serves as a comprehensive collection of Python programs demonstrating various data privacy and security concepts. Each practical is designed to help students understand the implementation and application of different cryptographic techniques and security practices.

## 📋 Practicals Overview

| Practical | Topic | Description |
|-----------|-------|-------------|
| **P1** | Caesar Cipher | Substitutional cipher for encryption/decryption |
| **P2** | Fernet Encryption | Symmetric encryption using cryptography library |
| **P3** | SHA-256 Hashing | Password hashing using SHA-256 algorithm |
| **P4** | Password Leak Checker | Check passwords against breach databases |
| **P5** | Password Generator | Generate secure passwords from dictionary words |
| **P6** | Brute Force Attack | Simulate password cracking attempts |
| **P7** | Digital Signatures | RSA-based document signing and verification |

## 🔧 Prerequisites

Before running these practicals, ensure you have the following installed:

- **Python 3.6+** (Python 3.8 or higher recommended)
- **pip** (Python package installer)

## 📦 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/ItsMeAnanyaSrivastava/Data-Privacy-Sem5-DU.git
   cd Data-Privacy-Sem5-DU
   ```

2. **Install required dependencies:**
   ```bash
   pip install cryptography requests
   ```

   Or create a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install cryptography requests
   ```

## 🚀 Usage

Each practical can be run independently using Python:

```bash
python P1.py
python P2.py
# ... and so on
```

Some practicals may require additional files (e.g., `a.csv` for P4, `dictionary.txt` for P5). Ensure these files are present in the same directory before running.

## 📝 Practical Details

### P1: Caesar Cipher

**Concept:** Substitutional cipher - one of the simplest encryption techniques

**What it does:**
- Encrypts text by shifting each letter by a fixed number of positions in the alphabet
- Decrypts the encrypted text back to original form
- Preserves case (uppercase/lowercase) and non-alphabetic characters

**How to run:**
```bash
python P1.py
```

**Example:**
```
Enter the text to be encrypted: Hello World
Enter the shift value (1-25): 3
Encrypted text: Khoor Zruog
Decrypted text: Hello World
```

---

### P2: Fernet Encryption

**Concept:** Symmetric encryption using the Fernet encryption scheme

**What it does:**
- Generates a secure encryption key
- Encrypts data using the Fernet symmetric encryption
- Decrypts the encrypted data back to original form

**How to run:**
```bash
python P2.py
```

**Example:**
```
Enter the text to be encrypted: Sensitive Information
Encrypted text: b'gAAAAABl...'
Decrypted text: Sensitive Information
```

---

### P3: SHA-256 Password Hashing

**Concept:** One-way cryptographic hashing for password storage

**What it does:**
- Takes a password as input
- Generates a SHA-256 hash of the password
- Returns the hash as a hexadecimal string

**How to run:**
```bash
python P3.py
```

**Example:**
```
Enter the password to be hashed: mySecurePassword123
Hashed password: 3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s9t0u1v2w3x4y5z6a7b8c9d0e1f2g3h4
```

---

### P4: Password Leak Checker

**Concept:** Checking passwords against known data breaches using Have I Been Pwned API

**What it does:**
- Reads username-password pairs from a CSV file
- Checks each password against the Have I Been Pwned database
- Reports which passwords have been compromised

**Prerequisites:**
- Create a file named `a.csv` with username,password pairs (one per line)

**How to run:**
```bash
python P4.py
```

**Example CSV format (a.csv):**
```
user1,password123
user2,securePass456
```

**Output:**
```
Password for user user1 has been leaked
Password for user name user2 is safe
```

---

### P5: Dictionary-based Password Generator

**Concept:** Generating strong passwords using dictionary words

**What it does:**
- Reads words from a dictionary file
- Randomly selects and combines words to create a password
- Provides a more memorable yet secure password option

**Prerequisites:**
- Create a file named `dictionary.txt` with one word per line

**How to run:**
```bash
python P5.py
```

**Example dictionary.txt:**
```
apple
banana
cherry
dragon
```

**Output:**
```
Generated password: applecherrydragon
```

---

### P6: Brute Force Attack Simulation

**Concept:** Demonstrating password vulnerability through brute force

**What it does:**
- Attempts to crack a password by trying all possible combinations
- Shows the number of attempts needed to find the password
- **Warning:** Can be very time-consuming for longer passwords!

**How to run:**
```bash
python P6.py
```

**Example:**
```
Enter Password: abc
Password Found: abc in 12345 attempts
```

**Note:** For educational purposes only. Use short passwords for testing (1-3 characters recommended).

---

### P7: Digital Signature

**Concept:** RSA-based digital signatures for document authentication

**What it does:**
- Generates RSA public-private key pair
- Signs a document using the private key
- Verifies the signature using the public key
- Demonstrates non-repudiation and authenticity

**How to run:**
```bash
python P7.py
```

**Output:**
```
Document: b'Confidential document needs to be signed'
Signature: 3d4e5f6g7h8i...
✅ Signature is valid.
```

---

## 📄 License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! If you'd like to contribute:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/improvement`)
3. Make your changes
4. Commit your changes (`git commit -am 'Add new feature'`)
5. Push to the branch (`git push origin feature/improvement`)
6. Create a Pull Request

## 📧 Contact

For questions or suggestions, please open an issue in this repository.

---

**Disclaimer:** These programs are for educational purposes only. Use them responsibly and ethically. Do not use the brute force or password checking tools for malicious purposes.
