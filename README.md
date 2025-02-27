# 2024
---
## Application Analysis

+ decryptPURPLE.py: Decrypt Message with its user_id
+ decryptSessionDB.py: Decrypt Database using AES256_GCM_NoPadding
+ decryptSessionFile.py: Decrypt file with its modernKey and encrypted file path

## Steganography

+ LSBStegano.py: Using LSB steganography, hide and seek message in image
+ steganomaster.py: Enter directory and name of image, then decode steganography that use staganomaster.apk



# 2025
---
## CNG

Studying Cryptography Next Generation in Microsoft

+ CNG_AES_Decrypt.c & CNG_AES_Encrypt.c: Given Key and IV, encrypt and decrypt "FaS 2025 Nice Happy Good~" using AES128_CBC_PKCS#7 Padding
+ CNG_RNG.c: Using CNG, Generate random 48 bytes
* CNG_RSA_Encrypt.c & CNG_RSA_Decrypt.c: With generated N, p, q, e, encrypt and decrypt "FaS 2025 Nice Happy Good~" using RSA 4096

## Ransomware

Make toy ransomware in C/C++

* Decrypt.c: With RSA private key, decrypt .cry file that encrypted by ransomware.exe
* File_test.c: Change extension to .cry, and delete other file -> For testing
* RSA_test.c: Encrypt AES key||IV (48 bytes) and Decrypt them in same code
* jihyun.c: Among the ransomware's functions, RSA encryption and file extension conversion were implemented
* ransomware.exe: Full toy ransomware (Although it is for study purposes, this ransomware actually encrypts files. BE CAREFUL!!)
