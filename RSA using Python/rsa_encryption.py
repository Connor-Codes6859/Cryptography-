from math import gcd
import random_prime

# randomly generate prime number with specified bit-length.
p = random_prime.generate_prime_number(6)
q = random_prime.generate_prime_number(6)

n = p * q #calculate our n value
r = (p - 1) * (q - 1) # calculate our phi(n) value

#trial and error a value for e
for i in range(2, r):
        if gcd(i, r) == 1: #if the greatest common devisor of (e, r) == 1, we have found e
            e = i
            break

d = pow(e, -1, r) #modular inverse of (e, r) Python equiv to e^-1 mod(r)

def main():
    msg = input("Enter your message to encrypt: ") #take user input for message to encrypt
    msg_encoded = int.from_bytes(msg.encode('utf-8'), byteorder='big') # encode the message from int to utf-8 so input can handle letters

    # print our values to console
    print("p = ",p)
    print("q = ",q)
    print("n = ",n)
    print("phi(n) = ",r)
    print("e (public) = ", e)
    print("d (private) = ",d)
    print("Mesage (m) = ",msg)
    print("Encoded Message = ",msg_encoded)
    print("\n\n")

    encrypted_msg = encrypt(msg_encoded, e, n) #encrypt our message (in encoded  format)
    decrypted_msg = decrypt(encrypted_msg, d, n) # decrypt our message
    decrypted_msg_encoded = int.to_bytes(decrypted_msg, length=len(msg), byteorder='big').decode('utf-8') #decode the encrypted output to retrieve the original message

    # print our values to console
    print("Encrypted message = ",encrypted_msg)
    print("Encoded Decrypted message = ",decrypted_msg)

# function to run the equation to encrypt with RSA
def encrypt(m, e, n):
    ciphertext = (m**e) % n
    return ciphertext

# function to run the equation to decrypt with RSA
def decrypt(c, d, n):
    plaintext = (c**d) % n
    return plaintext

if __name__ == "__main__":
    main()
