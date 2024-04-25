from pwn import xor

c1 = bytes.fromhex('144cafb119223b72cf7c3913a216351dd50c356759589c4c9fe7206fe314c6576c34557986b5ca24d98fc556')  # c1 = key ^ m1
c2 = bytes.fromhex('184abcb110357e37d879234ae60d341ac113745a0d589207c6ae077ee4108e55777b583b84a1d040c9849001')  # c2 = key ^ m2
c3 = bytes.fromhex('096d91c1312b3d20df711357b4183b14db5d72711b4b940d92fd1167b60fda5f47605d768c9fce65c49de527')  # c3 = key ^ m3

k1 = "UNIPI{"
k2 = ""
k3 = ""

k = "k1"
while True:
    print("\n")
    print(xor(bytes(globals()[k], 'utf-8'), c1, c2))
    print(xor(bytes(globals()[k], 'utf-8'), c1, c3))
    print(xor(bytes(globals()[k], 'utf-8'), c3, c2))
    print("\n\nk1: ", k1)
    print("k2: ", k2)
    print("k3: ", k3)
    print("\n")
    k = input("Choose key: ")
    if k == "exit":
        break
    chrs = input("Add characters: ")
    globals()[k] += chrs

m1 = k1
m2 = k2
m3 = k3

print("Message 1: "+k1+"\nMessage 2: "+k2+"\nMessage 3: "+k3)