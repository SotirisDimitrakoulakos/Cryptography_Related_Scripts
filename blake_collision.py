from hashlib import blake2b
import sys

def H(x):
	return blake2b(x).digest()[:2]


# SOLUTION #

if not len(sys.argv) == 2 or not sys.argv[1]:
    input1 = input('Enter first input (did not receive a singular argument): ').encode()
else:
    input1 = (sys.argv[1]).encode()

input2 = b''

h = H(input1)
for byte1 in range(256):
    for byte2 in range(256):
        temp = (chr(byte1) + chr(byte2)).encode()
        if H(temp) == h:
            input2 = temp
            break

# SOLUTION #

assert H(input1) == H(input2), exit("Oops. The inputs have different hashes!")

print(f'What?! How did you find a collision to my hash function? Congrats! 🔥')