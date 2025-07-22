# RSA Encryption/Decryption Tool
*Author*: elryan7  
*Repository*: https://github.com/elryan7/rsa-encryption-tool  
*License*: MIT  

## Description
This Python CLI tool implements RSA encryption and decryption, including key generation and digital signatures for data integrity. It allows users to generate RSA key pairs, encrypt/decrypt files, and sign/verify data.

## Features
- Generate RSA key pairs (public and private keys)
- Encrypt and decrypt files using RSA
- Sign and verify data with digital signatures
- Command-line interface for ease of use

## Prerequisites
- Python 3.8+
- Library: `pycryptodome`

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/elryan7/rsa-encryption-tool.git
   cd rsa-encryption-tool
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
Run the tool with:
```bash
python3 rsa_tool.py --help
```
Available commands:
- Generate keys: `python3 rsa_tool.py generate`
- Encrypt a file: `python3 rsa_tool.py encrypt input.txt output.enc public_key.pem`
- Decrypt a file: `python3 rsa_tool.py decrypt output.enc decrypted.txt private_key.pem`
- Sign a file: `python3 rsa_tool.py sign input.txt signature.bin private_key.pem`
- Verify a signature: `python3 rsa_tool.py verify input.txt signature.bin public_key.pem`

## Project Structure
- `rsa_tool.py`: Main script for RSA operations
- `requirements.txt`: List of required Python libraries
- `public_key.pem`, `private_key.pem`: Generated key files
- `signature.bin`: Generated signature file

## Contributing
Contributions are welcome! Please submit a pull request or open an issue on GitHub.

## Disclaimer
This tool is for educational purposes only. Ensure proper key management in production environments.