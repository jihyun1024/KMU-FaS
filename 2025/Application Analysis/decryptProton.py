from Crypto.Cipher import AES
import base64

# pass.key 복호화
with open('pass.key', 'rb') as f:
    data = f.read()

iv = data[:12]
ciphertext = data[12:]

masterkey = bytes.fromhex("9CE131042C30EB4A46D70E746D6C028018CEA0809A55DC4885FC421DA0AD4B53")

cipher = AES.new(masterkey, AES.MODE_GCM, nonce=iv)
dec_passkey = cipher.decrypt(ciphertext)
print("Decrypted pass.key:", dec_passkey)

# 암호화된 아티팩트 복호화
key = dec_passkey[:32]
encrypted_title = base64.b64decode('gBBgNYcmxkLJNeDmJXXnnpWLPlYp4TZlYlBEPo1lSuHqAyHC9zgD')
encrypted_note = base64.b64decode('5+4USFm6LIZ3c0ftYjrOr7v30vpvbGS1t8pV9CfFILwgDyRESi3E1QZuuqUJ232Fiv9hGg==')

# iv, ciphertext, tag 분리
iv_title = encrypted_title[:12] 
ciphertext_title = encrypted_title[12:-16]
tag_title = encrypted_title[-16:]

iv_note = encrypted_note[:12]
ciphertext_note = encrypted_note[12:-16]
tag_note = encrypted_note[-16:]

# 복호화
cipher_title = AES.new(key, AES.MODE_GCM, nonce=iv_title)
dec_title = cipher_title.decrypt(ciphertext_title)

cipher_note = AES.new(key, AES.MODE_GCM, nonce=iv_note)
dec_note = cipher_note.decrypt(ciphertext_note)

print("Decrypted Title:", dec_title.decode('utf-8'))
print("Decrypted Note:", dec_note.decode('utf-8'))
