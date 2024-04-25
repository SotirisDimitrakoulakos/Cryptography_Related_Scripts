
from math import gcd


class RSA:
    def __init__(self, c1, c2, n, e1, e2):
        self.c1 = c1
        self.c2 = c2
        self.n = n
        self.e1 = e1
        self.e2 = e2

    def decrypt(self):
        gcd_e1e2 = gcd(self.e1, self.e2)
        if gcd_e1e2 != 1 or gcd(self.c2, self.n) != 1:
            print("Unable to decrypt using the Common Modulo Attack.")
            exit()
        s1 = inverse_modulo(self.e1, self.e2)
        s2 = (gcd_e1e2 - self.e1 * s1) // self.e2
        temp = inverse_modulo(self.c2, self.n)
        m1 = pow(self.c1, s1, self.n)
        m2 = pow(temp, -s2, self.n)
        return (m1 * m2) % self.n


def inverse_modulo(v, p):
    return pow(v, -1, p)



def main():
    n = 0x7ae7ea74e879ade8ff34d6955a2979743cabf0ac72052f96b60d3bccbf22d5e8b1dcde63acb9b731d012752565bcf5f008d1ad61c27a2574d12bdd168977652603d5bb04a49bad34a1933f8fca54ad672498ed88514e45d5e0db0000ce882016e96d8e108fab9ebdb63c2f74f4b6c5bb0df53c7dad3d25700e74fa7309b658eb
    e1 = 0xb27b
    e2 = 0xaae7
    c1 = 0x5bded1cdcd47d0f5a739653da21a2b0324f02bcfd57dc92c02945a2aa471347ea338015278dfa6e03bab3f88286824fd5256d06af8e582eb4c2c6ff1a95382e36d6637c4eceaf32171cd7e0aedeab93fb53eea105c8e97422cd15c0b2ea768108337cd3498c0a0f75fd38e9037e93954c0ff7dbcfaa669bb29177768d9c463ed
    c2 = 0x1fba0e2aad60f6aebba93d3df01fdc15340d7852f9d8bcc77e7610a644218607754551f3e6f8b39b9a3508ef8a243cb2bd5a959e9cbbfa6f0a749cbcc9aec7e7aa195459b7dbc7740fc72042dd7d400fb45f5de6247232dabb462ccf57ab1701077f151206cb0d9cfebb30b1b1d33d096a1c29dc8bc986b94531f7871f92ac3

    rsa = RSA(c1, c2, n, e1, e2)
    m = rsa.decrypt()
    final_m = (int.to_bytes(m, (m.bit_length()+7) // 8, byteorder="big")).decode("ascii")
    print("FLAG: " + str(final_m))


main()

"""
FLAG = b'UNIPI{???????????????????????????}'

rsa = RSA(1024)

m = bytes_to_long(FLAG)

c1 = rsa.encrypt(m, (rsa.e1, rsa.n))
c2 = rsa.encrypt(m, (rsa.e2, rsa.n))

print(f'n = 0x{rsa.n:x}')
print(f'e1 = 0x{rsa.e1:x}')
print(f'e2 = 0x{rsa.e2:x}')
print(f'c1 = 0x{c1:x}')
print(f'c2 = 0x{c2:x}')

"""

# n = 0x7ae7ea74e879ade8ff34d6955a2979743cabf0ac72052f96b60d3bccbf22d5e8b1dcde63acb9b731d012752565bcf5f008d1ad61c27a2574d12bdd168977652603d5bb04a49bad34a1933f8fca54ad672498ed88514e45d5e0db0000ce882016e96d8e108fab9ebdb63c2f74f4b6c5bb0df53c7dad3d25700e74fa7309b658eb
# e1 = 0xb27b
# e2 = 0xaae7
# c1 = 0x5bded1cdcd47d0f5a739653da21a2b0324f02bcfd57dc92c02945a2aa471347ea338015278dfa6e03bab3f88286824fd5256d06af8e582eb4c2c6ff1a95382e36d6637c4eceaf32171cd7e0aedeab93fb53eea105c8e97422cd15c0b2ea768108337cd3498c0a0f75fd38e9037e93954c0ff7dbcfaa669bb29177768d9c463ed
# c2 = 0x1fba0e2aad60f6aebba93d3df01fdc15340d7852f9d8bcc77e7610a644218607754551f3e6f8b39b9a3508ef8a243cb2bd5a959e9cbbfa6f0a749cbcc9aec7e7aa195459b7dbc7740fc72042dd7d400fb45f5de6247232dabb462ccf57ab1701077f151206cb0d9cfebb30b1b1d33d096a1c29dc8bc986b94531f7871f92ac3