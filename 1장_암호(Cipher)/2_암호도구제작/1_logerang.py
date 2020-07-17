def makeCodebook():
    decbook={'5':'a','2':'b','#':'d','8':'e','1':'f','3':'g','4':'h','6':'i','0':'l','9':'m',\
        '*':'n','%':'o','=':'p','(':'r', ')':'s',';':'t','?':'u','@':'v',':':'y','7':' '}
    encbook = {}
    for k in decbook:   # k는 decbook의 key값들 
        val = decbook[k] # val은 deckbook[k]의 value값들 
        encbook[val] = k  #값을 키를 val로 값을 k로 저장 

    return encbook , decbook

def encrypt(msg , encbook):  #암호화 하다 
    for c in msg:
        if c in encbook:
            msg = msg.replace(c,encbook[c])

    return msg

def decrypt(msg, decbook):  #복호화 하다 
    for c in msg:
        if c in decbook:
            msg = msg.replace(c,decbook[c])
    return msg

'''
str = "This is python"

book = makeCodebook()

encbook=book[0]
decbook=book[1]

str = encrypt(str ,encbook )

print("암호문은 :"+str)

str = decrypt(str , decbook)

print("평문은  :"+str)
'''

if __name__=='__main__': #main 영역 
    plaintext = 'I love you with all my heart'

    encbook ,decbook = makeCodebook()
    ciphertext = encrypt(plaintext,encbook)
    print(ciphertext)

    deciphertext = decrypt(ciphertext ,decbook)
    print(deciphertext)
