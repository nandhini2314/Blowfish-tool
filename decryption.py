modVal = 1

P = [
    "243f6a88",
    "85a308d3",
    "13198a2e",
    "03707344",
    "a4093822",
    "299f31d0",
    "082efa98",
    "ec4e6c89",
    "452821e6",
    "38d01377",
    "be5466cf",
    "34e90c6c",
    "c0ac29b7",
    "c97c50dd",
    "3f84d5b5",
    "b5470917",
    "9216d5d9",
    "8979fb1b",
]


def keyGenerate(key):
    j = 0
    for i in range(len(P)):
        P[i] = XOR(P[i], key[j, j + 8])
        print("SubKey: ", (i + 1), ":", P[i])
        j = (j + 1) % len(key)


def decrypt(plainText):
    for i in range(17, 1, -1):
        plainText = round(i, plainText)
    right = plainText[0, 8]
    left = plainText[8, 16]
    right = XOR(right, P[1])
    left = XOR(left, P[0])
    return right + left


def decryption():
    global modVal
    for _ in range(0, 32):
        modVal = modVal << 1
    cipherText = "d748ec383d3405f7"
    key = "aabb09182736ccdd"
    keyGenerate(key)
    print("\t\tDecryption")
    plainText = decrypt(cipherText)
    print("\t\tPlain Text:", plainText)


decryption()
