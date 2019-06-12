'''
    Simple Encryption and Decryption Program
'''


def encrypt(s):
    return ''.join([chr(ord(i)+1) for i in s])


def decrypt(s):
    return ''.join([chr(ord(i)-1) for i in s])


def main():
    user_string = input("Enter your string:")

    enc_string = encrypt(user_string)
    print("Encrypted to: " + enc_string)

    print("Decrypted to: " + decrypt(enc_string))

if __name__ == "__main__":
    main()
