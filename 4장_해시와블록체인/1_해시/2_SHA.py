from hashlib import sha256
from hashlib import sha3_256
msg='I love Python'
sha=sha256()
sha.update(msg.encode('utf-8'))
ret = sha.hexdigest()
print('SHA-2 SHA-256: ',ret)

#SHA-3

msg='I love Python'
sha=sha3_256()
sha.update(msg.encode('utf-8'))
ret = sha.hexdigest()
print('SHA-3 SHA-256: ',ret)
