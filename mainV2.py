import hashlib

def hashSha256(char):
    h = hashlib.sha256()
    h.update(char.encode('utf-8'))
    return h.hexdigest()

def hashSha1(char):
    h = hashlib.sha1()
    h.update(char.encode('utf-8'))
    return h.hexdigest()

def hashMD5(char):
    h = hashlib.md5()
    h.update(char.encode('utf-8'))
    return h.hexdigest()

def hashSha512(char):
    h = hashlib.sha512()
    h.update(char.encode('utf-8'))
    return h.hexdigest()

def hashReconnaissance(char):
    if len(char) == 32:
        print(f"{char} is MD5")
    elif len(char) == 40:
        print(f"{char} is sha1")
    elif len(char) == 64:
        print(f"{char} is sha256")
    elif len(char) == 128:
        print(f"{char} is sha512")
    else:
        print("bye...")

def hashComparaison(char, char2):
    if char == char2:
        print(f"{char} is equal to {char2}")
    else:
        print(f"{char} is not equal to {char2}")

def choice():
    print("Welcome in HASH GENERATOR BY IAMTHEROOT")
    print("1. Md5")
    print("2. Sha1")
    print("3. Sha256")
    print("4. Sha512")
    print("5. Hash Recon")
    print("6. Hash Comparaison")

choice = choice()
modChoice = int(input("Choose an option:"))

if modChoice == 1:
    char = input("Type what you want ot hash: ")
    hash_resultat = hashMD5(char)
    print(hash_resultat)
elif modChoice == 2:
    char = input("Type what you want ot hash: ")
    hash_resultat = hashSha1(char)
    print(hash_resultat)
elif modChoice == 3:
    char = input("Type what you want ot hash: ")
    hash_resultat = hashSha256(char)
    print(hash_resultat)
elif modChoice == 4:
    char = input("Type what you want ot hash: ")
    hash_resultat = hashSha512(char)
    print(hash_resultat)
elif modChoice == 5:
    char = input("Paste your hash: ")
    recon = hashReconnaissance(char)
elif modChoice == 6:
    char = input("Paste the first hash: ")
    char2 = input("Paste the second hash: ")
    compararaison = hashComparaison(char, char2)
else:
    print("bye...")
