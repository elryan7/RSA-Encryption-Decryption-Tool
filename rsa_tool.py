from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
import argparse
import os

def generate_keys():
    """Generate RSA key pair and save to files."""
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    
    with open('private_key.pem', 'wb') as f:
        f.write(private_key)
    with open('public_key.pem', 'wb') as f:
        f.write(public_key)
    print("Keys generated: private_key.pem, public_key.pem")

def encrypt_file(input_file, output_file, public_key_file):
    """Encrypt a file using RSA public key."""
    with open(public_key_file, 'rb') as f:
        public_key = RSA.import_key(f.read())
    cipher = PKCS1_OAEP.new(public_key)
    
    with open(input_file, 'rb') as f:
        data = f.read()
    
    encrypted_data = cipher.encrypt(data)
    
    with open(output_file, 'wb') as f:
        f.write(encrypted_data)
    print(f"File encrypted: {output_file}")

def decrypt_file(input_file, output_file, private_key_file):
    """Decrypt a file using RSA private key."""
    with open(private_key_file, 'rb') as f:
        private_key = RSA.import_key(f.read())
    cipher = PKCS1_OAEP.new(private_key)
    
    with open(input_file, 'rb') as f:
        encrypted_data = f.read()
    
    decrypted_data = cipher.decrypt(encrypted_data)
    
    with open(output_file, 'wb') as f:
        f.write(decrypted_data)
    print(f"File decrypted: {output_file}")

def sign_file(input_file, signature_file, private_key_file):
    """Sign a file using RSA private key."""
    with open(private_key_file, 'rb') as f:
        private_key = RSA.import_key(f.read())
    
    with open(input_file, 'rb') as f:
        data = f.read()
    
    hash_obj = SHA256.new(data)
    signature = pkcs1_15.new(private_key).sign(hash_obj)
    
    with open(signature_file, 'wb') as f:
        f.write(signature)
    print(f"Signature created: {signature_file}")

def verify_signature(input_file, signature_file, public_key_file):
    """Verify a file's signature using RSA public key."""
    with open(public_key_file, 'rb') as f:
        public_key = RSA.import_key(f.read())
    
    with open(input_file, 'rb') as f:
        data = f.read()
    
    with open(signature_file, 'rb') as f:
        signature = f.read()
    
    hash_obj = SHA256.new(data)
    try:
        pkcs1_15.new(public_key).verify(hash_obj, signature)
        print("Signature is valid.")
    except (ValueError, TypeError):
        print("Signature is invalid.")

def main():
    parser = argparse.ArgumentParser(description="RSA Encryption/Decryption and Signing Tool")
    subparsers = parser.add_subparsers(dest='command')
    
    subparsers.add_parser('generate', help='Generate RSA key pair')
    
    parser_encrypt = subparsers.add_parser('encrypt', help='Encrypt a file')
    parser_encrypt.add_argument('input_file', help='Input file to encrypt')
    parser_encrypt.add_argument('output_file', help='Output encrypted file')
    parser_encrypt.add_argument('public_key', help='Public key file')
    
    parser_decrypt = subparsers.add_parser('decrypt', help='Decrypt a file')
    parser_decrypt.add_argument('input_file', help='Input encrypted file')
    parser_decrypt.add_argument('output_file', help='Output decrypted file')
    parser_decrypt.add_argument('private_key', help='Private key file')
    
    parser_sign = subparsers.add_parser('sign', help='Sign a file')
    parser_sign.add_argument('input_file', help='Input file to sign')
    parser_sign.add_argument('signature_file', help='Output signature file')
    parser_sign.add_argument('private_key', help='Private key file')
    
    parser_verify = subparsers.add_parser('verify', help='Verify a file signature')
    parser_verify.add_argument('input_file', help='Input file to verify')
    parser_verify.add_argument('signature_file', help='Signature file')
    parser_verify.add_argument('public_key', help='Public key file')
    
    args = parser.parse_args()
    
    if args.command == 'generate':
        generate_keys()
    elif args.command == 'encrypt':
        encrypt_file(args.input_file, args.output_file, args.public_key)
    elif args.command == 'decrypt':
        decrypt_file(args.input_file, args.output_file, args.private_key)
    elif args.command == 'sign':
        sign_file(args.input_file, args.signature_file, args.private_key)
    elif args.command == 'verify':
        verify_signature(args.input_file, args.signature_file, args.public_key)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()