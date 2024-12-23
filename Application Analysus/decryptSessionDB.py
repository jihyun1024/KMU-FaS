from Crypto.Cipher import AES
import base64

encrypted_data = base64.b64decode('Pi1ZSQa4/YwrzQHNvDJLrYoV3eAPiOTgQMvhTldmz/ocblkszIEGt/1RRcPP//tU'.encode())
encrypted_iv = base64.b64decode("1btcRRMUZUJkrPej".encode())

key = b'\x73\xba\x7c\x7e\x28\xed\x55\x27\xf3\x92\x18\x71\x6a\xd9\x70\xad'
data = encrypted_data[:32]

decrypt_key = AES.new(key, AES.MODE_GCM, encrypted_iv).decrypt(data).hex()
print(decrypt_key)