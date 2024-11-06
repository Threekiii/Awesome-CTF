# -*- coding: utf-8 -*-
# @Author  : Threekiii
# @Time    : 2023/12/1 15:03
# @Function: AES Encryption and Decryption

# AES Key lenth: 16 -> Ciphertext length: 128
# AES Key lenth: 32 -> Ciphertext length: 256

from Crypto.Util.Padding import pad
from Crypto.Cipher import AES
import base64

# AES Mode:
# Crypto.Cipher.AES.MODE_ECB= 1
# Crypto.Cipher.AES.MODE_CBC = 2
# Crypto.Cipher.AES.MODE_EAX = 9
# ...

def padding(data):
    # style(string) – Padding algorithm.It can be ‘pkcs7’ (default), ‘iso7816’ or ‘x923’.
    if len(data) % AES.block_size != 0:
        return pad(data, AES.block_size, 'pkcs7')
    else:
        return data

def aes_ecb_encrypt(key, data):
    pad_pkcs7 = padding(data)
    # pad_pkcs7 = pad(data, AES.block_size, style='pkcs7')  # pkcs7 Padding

    key = padding(key)

    aes = AES.new(key, AES.MODE_ECB)
    encrypt_aes = aes.encrypt(pad_pkcs7)
    encrypted_result = base64.b64encode(encrypt_aes)
    return encrypt_aes,encrypted_result

def aes_ecb_decrypt(key, data):
    key = padding(key)

    aes = AES.new(key, AES.MODE_ECB)
    decrypted_text = aes.decrypt(data)
    return decrypted_text

if __name__ == '__main__':
    key = b"db20d905c4635f77"
    data = b"flag{whoami_WHOAMI_12345_Wh0am1}"
    encrypt_aes,encrypted_result = aes_ecb_encrypt(key, data)
    print(encrypted_result)
    decryption_result = aes_ecb_decrypt(key,encrypt_aes)
    print(decryption_result)





