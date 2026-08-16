import subprocess
import ctypes

libcrypt = ctypes.CDLL("libcrypt.so.1")
libcrypt.crypt.argtypes = [ctypes.c_char_p, ctypes.c_char_p]
libcrypt.crypt.restype = ctypes.c_char_p

shadow = subprocess.check_output("cat /etc/shadow", shell=True).decode()
passwd_list = shadow.split("\n")

with open("python/unix_passwords.txt", "r") as f:
    passwords = [line.strip() for line in f if line.strip()]

target_hash = ""
for line in passwd_list:
    if line.startswith("kali:"):
        target_hash = line.split(":")[1]
        break

print(f"[+] Target Hash: {target_hash}")

if target_hash:
    target_hash_bytes = target_hash.encode("utf-8")
    for word in passwords:
        hashed = libcrypt.crypt(word.encode("utf-8"), target_hash_bytes)
        if hashed and hashed.decode("utf-8") == target_hash:
            print(f"[+] Password Found: {word}")
            break