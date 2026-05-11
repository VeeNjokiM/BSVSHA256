import hashlib
m = input("Enter the string to hash: ")
sha3_256 = hashlib.sha3_256()
sha3_256.update(m.encode('utf-8'))  
print("SHA3-256 hash:", sha3_256.hexdigest())