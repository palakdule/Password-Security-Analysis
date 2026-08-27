# 🔐 Password Security Analysis

A Python-based cybersecurity project that analyzes password security by comparing **SHA-256 and bcrypt hashing**, simulating a **controlled offline dictionary attack**, and analyzing **password reuse patterns** using synthetic test data.

## 📌 Project Overview

This project evaluates common password-security risks in an online gaming platform scenario. It demonstrates how fast hashing and password reuse can increase the risk of offline password-guessing and account compromise.

The project uses synthetic passwords and fictional user accounts in a controlled local environment.

## 🎯 Objectives

* Analyze the security limitations of fast password hashing.
* Compare SHA-256 with bcrypt for password protection.
* Simulate a controlled offline dictionary attack.
* Identify password reuse among synthetic users.
* Apply bcrypt-based mitigation and perform retesting.
* Verify correct and incorrect password authentication.

## 🛠️ Technologies Used

* **Python**
* **SHA-256**
* **bcrypt**
* **Python hashlib**
* **Controlled Dictionary Attack**
* **Password Reuse Analysis**

## ⚙️ Project Workflow

```text
Synthetic Test Data
        ↓
SHA-256 Hashing
        ↓
bcrypt Hashing
        ↓
Controlled Offline Attack
        ↓
Password Reuse Analysis
        ↓
Mitigation using bcrypt + Strong Password
        ↓
Retesting & Verification
```

## 🔍 Features

### SHA-256 Hashing

Generates a fixed-length 256-bit hash and demonstrates the limitation of fast hashing for password storage.

### bcrypt Password Hashing

Uses salting and a configurable computational cost to provide stronger protection against offline password-guessing attacks.

### Controlled Offline Dictionary Attack

Tests a predefined list of synthetic candidate passwords against an authorized test hash.

### Password Reuse Analysis

Analyzes fictional user accounts to identify passwords reused by multiple users.

### Mitigation Testing

A stronger password is hashed using bcrypt and tested against the same candidate list to compare the result before and after mitigation.

### Password Verification

Tests both correct and incorrect passwords using bcrypt verification.

## 📊 Results

The implementation demonstrated:

* SHA-256 and bcrypt hashes were successfully generated.
* The controlled dictionary attack successfully identified the weak test password `Game@123`.
* Password reuse was identified among multiple synthetic users.
* The stronger password used after mitigation was not found in the same candidate list.
* Correct password verification returned `True`.
* Incorrect password verification returned `False`.

## 🔒 Security Findings

The project demonstrated that:

* Fast general-purpose hashing such as SHA-256 is not ideal as the primary password-storage mechanism.
* Password reuse increases the potential impact of credential compromise.
* Password-specific hashing algorithms such as bcrypt provide stronger resistance to offline password-guessing.
* Strong and unique passwords improve account security.

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone <git clone https://github.com/palakdule/Password-Security-Analysis.git>
cd Password-Security-Analysis
```

### 2. Install the required package

```bash
pip install -r requirements.txt
```

### 3. Run the program

```bash
python main.py
```

## 📁 Project Structure

```text
Password-Security-Analysis/
│
├── main.py
├── requirements.txt
└── README.md
```

## ⚠️ Ethical Considerations

This project uses only **synthetic test passwords, fictional user accounts, and controlled attack scenarios**. No real credentials, unauthorized systems, or external services were accessed.

## 📚 References

* W. Stallings, *Cryptography and Network Security: Principles and Practice*, 8th ed.
* National Institute of Standards and Technology (NIST), *Secure Hash Standard (SHS)*.
* OWASP Foundation, *Password Storage Cheat Sheet*.
* Python Documentation - `hashlib`
* PyCA `bcrypt` documentation

## 👩‍💻 Author

**Palak Dule**
