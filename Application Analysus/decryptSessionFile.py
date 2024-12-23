import os
from Crypto.Cipher import AES
from Crypto.Hash import HMAC, SHA256
from Crypto.Util import Counter

def generate_AES_key(modernKey, data_random):
    # Generate AES Key using HMAC_SHA256
    h = HMAC.new(modernKey.encode(), data_random.encode(), digestmod=SHA256)
    
    return h.digest()


def decrypt_file(AES_Key, encrypted_file, iv):
    # Decrypt the file using AES256 CTR NoPadding method
    cipher = AES.new(AES_Key, AES.MODE_CTR, nonce=iv)
    dec_data = cipher.decrypt(encrypted_file)

    return dec_data

def main():
    modernkey = "2e8f9184c81de9b96baccfa34adabecd77bb0f6e1208c339c014d8e1c49ba4a6"
    data_random_name = input('Enter data_random name: ')
    enc_file_path = input('Enter encrypted_file_path (Extension: mms): ')
    iv = Counter.new(128, initial_value=0)

    with open(data_random_name, 'rb') as f:
        data_random = f.read()
        
    with open(enc_file_path, 'rb') as f:
        enc_file = f.read()

    AES_key = generate_AES_key(modernkey, data_random)
    dec_data = decrypt_file(AES_key, enc_file, iv)

    # Create a new folder
    os.makedirs('decrypted_file_folder', exist_ok=True)

    # Save the decrypted file in the 'decrypted_file_folder'
    with open('decrypted_file_folder/decrypted_file.txt', 'wb') as f:
        f.write(dec_data)

if __name__ == '__main__':
    main()