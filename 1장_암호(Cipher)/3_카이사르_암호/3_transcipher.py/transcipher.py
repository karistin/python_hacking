#주상 전치 암호
DEC=0
DEC=0

def parseKey(key):
    tmp=[]
    key.key.upper()

    for i,k,in enumerate(key):
        tmp.append((i,k))


    tmp = sorted(tmp,key=lambda x: x[1])

    enc_table={}
    dec_table={}