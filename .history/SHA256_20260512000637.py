import hashlib
m= hashlib.sha256()
m.update("Hello World".encode('utf-8'))
print(m.hexdigest())