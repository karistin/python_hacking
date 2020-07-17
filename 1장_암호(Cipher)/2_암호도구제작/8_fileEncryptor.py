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

if __name__=='__main__':
    h=open('1장_암호(Cipher)\\2_암호도구제작\\plain.txt','rt')
    content = h.read()
    h.close

    encbook , decbook = makeCodebook()
    content = encrypt(content , encbook)

    h = open('1장_암호(Cipher)\\2_암호도구제작\\encryption.txt','wt+')
    h.write(content)
    h.close()