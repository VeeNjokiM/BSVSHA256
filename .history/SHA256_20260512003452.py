import hashlib
m= hashlib.sha256()
m.update("Victoriagenerate".encode('utf-8'))
print(m.hexdigest())