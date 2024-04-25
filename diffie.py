from random import randint
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from sympy import primefactors, mod_inverse


""""
FLAG = b'UNIPI{?????????????????????????????????}'

p = 270240672270762705063730574510166919388679291730697533023435816363819495490544398799
g = 7

a = randint(1, p)
b = randint(1, p)

A = pow(g, a, p)
B = pow(g, b, p)

s = pow(B, a, p)

assert s == pow(A, b, p)

key = str(s).encode()

cipher = AES.new(key[:16], AES.MODE_ECB)

ct = cipher.encrypt(pad(FLAG, 16)).hex()

print(f'{A = }')
print(f'{B = }')
print(f'{ct = }')

"""""
p = 270240672270762705063730574510166919388679291730697533023435816363819495490544398799
g = 7
order = 270240672270762705063730574510166919388679291730697533023435816363819495490544398798 #p is a prime number so: order = p-1

A = 132900358234735034249317237435649175215079000129033326958065863238280096109600116393
B = 66237009707363688516841862830226845310451942948101229843794107291024783961925800283
ct = '192e576d00a1be0d9e4dcd13f4bbbd18aa74ecae8c822963e7848b883b7080193f56b3725d8e8cbaecc924c98eac0250'

ct_b = bytes.fromhex(ct)


def sqm(a, b, n):
    res = 1
    binarray = [int(x) for x in bin(int(b))[2:]]
    for i in binarray:
        if i == 1:
            res = (res * res * a) % n
        else:
            res = (res * res) % n
    return res


def find_prime_factors(j):
    factors = []
    n = 2
    while n <= j:
        if j % n == 0:
            factors += [n]
            j //= n
        else:
            n += 1
    return factors


def calculate_subgrp_congruences(pub, pi):
    gi = sqm(g, order // pi, p)
    hi = sqm(B, order // pi, p)
    c = 1
    while c < p:
        if sqm(gi, c, p) % p == hi % p:
            return c
        c += 1
    return -1


def solve_crt(dlogs, factors):
    n = 1
    for i in factors:
        n *= i
    x = 0
    for i in range(len(dlogs)):
        yi = n // factors[i]
        zi = mod_inverse(yi, factors[i])
        x += dlogs[i] * yi * zi
    return x % n



factors = find_prime_factors(order)
dlogs = []
for factor in factors:
    dlogs.append(calculate_subgrp_congruences(B, factor))
key = solve_crt(dlogs, factors)



shared_secret = pow(A, key, p)
print("The Key is {}.".format(shared_secret))

final_key = str(shared_secret).encode()
cipher = AES.new(final_key[:16], AES.MODE_ECB)


pt = unpad(cipher.decrypt(ct_b), 16)
pt_final = pt.decode('utf-8')


print("\nFlag: "+ str(pt))