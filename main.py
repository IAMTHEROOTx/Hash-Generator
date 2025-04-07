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

def choice():
    print("Welcome in HASH GENERATOR BY IAMTHEROOT")
    print("1. md5")
    print("2. sha1")
    print("3. sha256")
    print("4. sha512")

choice = choice()
modChoice = int(input("Quelles modes de hachages choisissez vous:"))

if modChoice == 1:
    char = input("Que voulez vous hacher: ")
    hash_resultat = hashMD5(char)
    print(hash_resultat)
elif modChoice == 2:
    char = input("Que voulez vous hacher: ")
    hash_resultat = hashSha1(char)
    print(hash_resultat)
elif modChoice == 3:
    char = input("Que voulez vous hacher: ")
    hash_resultat = hashSha256(char)
    print(hash_resultat)
elif modChoice == 4:
    char = input("Que voulez vous hacher: ")
    hash_resultat = hashSha512(char)
    print(hash_resultat)
else:
    print("bye...")
