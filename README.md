# 🛡️ Hash Generator v1 & v2 — by IAMTHEROOT

Welcome to the **Hash Generator** developed in Python. This script allows you to **generate**, **recognize**, and **compare** different types of hashes in a simple and quick way.

---

## ⚙️ Available Features

| Option | Feature                         | Description |
|--------|---------------------------------|-------------|
| 1      | **MD5**                         | Generates an MD5 hash |
| 2      | **SHA1**                        | Generates a SHA1 hash |
| 3      | **SHA256**                      | Generates a SHA256 hash |
| 4      | **SHA512**                      | Generates a SHA512 hash |
| 5      | **Hash Recognition**            | Identifies the hash type based on its length |
| 6      | **Hash Comparison**             | Compares two hashes to check if they are equal |

---

## ▶️ How to Use

Run the program:

```bash
python hash_generator.py
```

Welcome menu:

```text
Welcome to HASH GENERATOR BY IAMTHEROOT
1. Md5
2. Sha1
3. Sha256
4. Sha512
5. Hash Recon
6. Hash Comparaison
```

---

## 💡 Examples

### Generate a hash:

```text
Choose an option: 3
Type what you want to hash: hello
SHA256: 2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824
```

### Recognize a hash:

```text
Choose an option: 5
Paste your hash: 5d41402abc4b2a76b9719d911017c592
Result: MD5
```

### Compare two hashes:

```text
Choose an option: 6
Paste the first hash: 5d41402abc4b2a76b9719d911017c592
Paste the second hash: 5d41402abc4b2a76b9719d911017c592
Result: The hashes are equal
```

---

## 🧠 Hash Recognition Logic

| Hash Length | Recognized Type |
|-------------|-----------------|
| 32 characters | MD5            |
| 40 characters | SHA1           |
| 64 characters | SHA256         |
| 128 characters | SHA512         |

---

## 🛠️ Dependencies

- Python 3.x
- No external dependencies — uses the built-in `hashlib` library

---

## 🧩 Function Breakdown

```python
def hashMD5(char)
def hashSha1(char)
def hashSha256(char)
def hashSha512(char)
def hashReconnaissance(char)
def hashComparaison(char, char2)
```

---

## 👤 Author

**IAMTHEROOTx**

---

## 📝 License

This is an open project — feel free to use, modify, or improve it as you see fit.
