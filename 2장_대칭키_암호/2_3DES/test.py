from Crypto.Hash import SHA256 as SHA

keytext ='secretKey'
hash=SHA.new()
hash.update(keytext.encode('utf-8'))
key=hash.digest()
print(key)