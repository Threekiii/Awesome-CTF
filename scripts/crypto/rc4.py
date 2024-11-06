# -*- coding: utf-8 -*-
# @Author  : Threekiii
# @Time    : 2023/5/12 15:32
# @Function: RC4 Decryption

import base64
def rc4_main(key = "init_key", message = "init_message"):
    s_box = rc4_init_sbox(key)
    crypt = rc4_excrypt(message, s_box)
    return crypt

def rc4_init_sbox(key):
    s_box = list(range(256))
    print("[Initial S-Box]: {}".format(s_box))
    j = 0
    for i in range(256):
        j = (j + s_box[i] + ord(key[i % len(key)])) % 256
        s_box[i], s_box[j] = s_box[j], s_box[i]
    print("[Random S-Box]: {}".format(s_box))
    return s_box
def rc4_excrypt(plain, box):
    plain = base64.b64decode(plain.encode('utf-8'))
    plain = bytes.decode(plain)
    res = []
    i = j = 0
    for s in plain:
        i = (i + 1) % 256
        j = (j + box[i]) % 256
        box[i], box[j] = box[j], box[i]
        t = (box[i] + box[j]) % 256
        k = box[t]
        res.append(chr(ord(s) ^ k))
    cipher = "".join(res)
    return cipher

if __name__ == "__main__":
    input=[188, 197, 18, 125, 133, 35, 132, 113, 123, 57, 40, 2, 211, 81, 243, 44, 137, 43, 166, 44, 175, 9]    #Cipher
    key='12345678abcdefghijklmnopqrspxyz'
    s=''
    for i in input:
        s+=chr(i)
    s=str(base64.b64encode(s.encode('utf-8')), 'utf-8')
    result = rc4_main(key, s)
    print("*"*100)
    print("[Cipher]: {}".format(input))
    print("[Key]: {}".format(key))
    print("[Plain Text Result]: {}".format(result))