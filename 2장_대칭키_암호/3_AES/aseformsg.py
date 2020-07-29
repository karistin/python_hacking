from Crypto.Cipher import AES
from Crypto.Hash import SHA256 as SHA

class myAES():
    def __init__(self,keytext,ivtext):
        hash =SHA.new()
        hash.update(keytext.encode('utf-8'))
        key=hash.digest()
        self.key=key[:16]
        #AES는 192(24) 256(32)비트들도 지원 지금은 128bit
        hash.update(ivtext.encode('utf-8'))
        iv=hash.digest()
        self.iv=iv[:16]

    def makeEnabled(self,plaintext):
        fillersize=0
        textsize=len(plaintext)
        if textsize%16 !=0:
            fillersize=16-textsize%16

        filler = '0'*fillersize
        header = '%d'%(fillersize)
        #int를 str형으로 대입
        gap=16-len(header)

        header +='#'*gap
        #header 생성 및 패딩 설정 
        return header+plaintext+filler

    def enc(self,plaintext):
        plaintext = self.makeEnabled(plaintext)
        aes=AES.new(self.key,AES.MODE_CBC,self.iv)
        encmsg = aes.encrypt(plaintext.encode())
        return encmsg

    def dec(self,ciphertext):
        aes = AES.new(self.key,AES.MODE_CBC,self.iv)
        decmsg = aes.decrypt(ciphertext)

        header=decmsg[:16].decode()
        fillersize=int(header.split('#')[0])
        # #분리하고 첫번째 수 저장  
        if fillersize !=0:
            decmsg = decmsg[16: -fillersize]
            #16부터 총길이 -fillersize만큼 
        else:
            decmsg = decmsg[16:]
        return decmsg

def main():
    keytext='samsjang'
    ivtext='1234'
    msg = 'Hello World, This is python. Please insert your name.'

    myCipher =myAES(keytext,ivtext)
    ciphered = myCipher.enc(msg)
    deciphered =myCipher.dec(ciphered)
    
    print('ORIGINAL : \t%s' %msg)
    print('CIPHERED : \t%s' %ciphered)
    print('DECIPHERED : \t%s' %deciphered)



main()