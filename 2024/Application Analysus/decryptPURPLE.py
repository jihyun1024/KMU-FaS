import base64
from Crypto.Cipher import AES
from Crypto.Hash import SHA256

def decrypt_message(user_id, encrypted_message):
    # Step 1: Generate AES key using SHA256 hash of session_user_id
    aes_key = SHA256.new(user_id.encode()).digest()

    # Step 2: Initialize IV (Initialization Vector)
    iv = bytes([0] * 16)  # Use all zeros for IV

    # Step 3: Decode the Base64-encoded encrypted message
    decoded_message = base64.b64decode(encrypted_message)

    # Step 4: Decrypt the message using AES-256
    cipher = AES.new(aes_key, AES.MODE_CBC, iv)
    decrypted_message = cipher.decrypt(decoded_message).decode()

    # Step 5: Return the decrypted message
    return decrypted_message

# Example usage
if __name__ == "__main__":
    user_id = 'ACA8485E-4B34-49AE-A18D-A09B8C4503E0'

    while True:
        encrypted_message = input('Enter encrypted message: ')
        decrypted_result = decrypt_message(user_id, encrypted_message)
        print("Decrypted Message:", decrypted_result)

        conti = input('Continue? (if exit, enter x. Or enter anything.): ')
        if conti == 'x':
            print('\nYou calcelled the operation!')
            break

