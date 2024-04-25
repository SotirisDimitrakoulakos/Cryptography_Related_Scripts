from Crypto.Cipher import AES
import os
from Crypto.Util.Padding import pad


'''
You are given:
  1. CTR nonce
  2. AES key
  3. the ciphertext produced by CTR mode

TASK:
  Decrypt the message using ONLY ECB mode!
'''

# CTR nonce = bc5fccb24e91fa92684fa3f6a6d0d6
# AES key = 00542446326e7779c04c0122a2fe29bb
# CTR ciphertext = b117ade0a04527642111da7c9b14591986e566118cb5f3d39862acc01d371d87e17934051693fc0e97c854c600c502ef8b80bbed6013197b6ee7e21b4f050e4368319a6c31d3d30efeb9c98a91176953


# SOLUTION #

nonce = bytes.fromhex('bc5fccb24e91fa92684fa3f6a6d0d6')
key = bytes.fromhex('00542446326e7779c04c0122a2fe29bb')
ciphertext = bytes.fromhex('b117ade0a04527642111da7c9b14591986e566118cb5f3d39862acc01d371d87e17934051693fc0e97c854c600c502ef8b80bbed6013197b6ee7e21b4f050e4368319a6c31d3d30efeb9c98a91176953')


ct_blocks = [ciphertext[i:i+16] for i in range(0, len(ciphertext), 16)]

plaintext = b''
counter = 0

for i in range(0, len(ct_blocks)):
    to_enc = nonce + bytes([counter])
    cipher = AES.new(key, AES.MODE_ECB)
    BCE = cipher.encrypt(to_enc)
    pt_block = xor(BCE, ct_blocks[i])
    plaintext = plaintext + pt_block
    counter+=1

plaintext = str(plaintext)
print("\n\nPlaintext: " + plaintext)
print("\nFlag: "+plaintext[2:67])


# SOLUTION #
