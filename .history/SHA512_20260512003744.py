import hashlib
m = input("Enter the string to hash: ")
sha512 = hashlib.sha512()
sha512.update(m.encode('utf-8'))  
print( sha512.hexdigest() )