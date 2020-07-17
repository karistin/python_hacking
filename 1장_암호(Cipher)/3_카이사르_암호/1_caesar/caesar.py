#카이사르 암호
#전역변수
ENC =0#암호화
DEC =1#복호화

def makeDisk(key):
    keytable=list(map(lambda x: (chr(x+65) , x) , range(26)))#list() 필요 
    #keytable =[('A',0),('B',1),('C',2),.....,('Z',25)] 
    key2index ={}
    #key2index={'A':0,'B':1,'C':2,...,'Z':25},
    for t in keytable:
        alphabet , index = t[0] ,t[1] #t[0] = A , t[1]=0 ,t=('A',0)
        key2index[alphabet] = index #dictonary
    if key in key2index:
        k=key2index[key] #암호키 인덱스(문자를 앞으로 땅긴 횟수)
    else:
        return None,None #어떤 변수도 없는 상태로 반환
    #암호키를 찾음 
    enc_disk={}#암호화
    dec_disk={}#복호화

    for i in range(26):
        enc_i = (i+k)%26 #바뀐 문장의 인덱스 
        enc_ascii =enc_i+65 #문자로 변환 / 아스키 코드
        enc_disk[chr(i+65)] = chr(enc_ascii)
        dec_disk[chr(enc_ascii)]=chr(i+65)
    return enc_disk,dec_disk

def caesar(msg,key,mode):
    ret=''
      #결과를 위한 빈 문자열 
    msg=msg.upper()#대문자로 변환 
    enc_disk,dec_disk=makeDisk(key)

    if enc_disk is None:
        return ret
    #makeDisk(key)를 호출하고, 결과가 None이면 빈 문자열 ret을 리턴합니다.
    if mode is ENC:
        disk = enc_disk 
    if mode is DEC:
        disk = dec_disk
    #mode가 ENC이면 enc_disk를, DEC이면 dec_disk를 변수 disk에 할당합니다.
    for c in msg:
        if c in disk:
            ret +=disk[c]
        else:
            ret +=c
    #msg의 각 문자 c가 disk의 키로 존재하면 c가 키인 값을 ret에 추가하고, 
    #키로 존재하지 않으면 c를 ret에 추가합니다. 
    return ret
def main():
    #plaintext='ABCDEFGHIJKLMNOPQRSTUWXYZ'

    h=open('1장_암호(Cipher)\\3_카이사르_암호\\1_caesar\\plain.txt','rt')
    plaintext =h.read()
    h.close  

    key ='F'
    #암호키 F로 복호화

    #print('Original:\t%s' %plaintext.upper())

    ciphertext = caesar(plaintext,key,ENC)
    #print('Caesar Cipher:\t%s' %ciphertext)

    h=open('1장_암호(Cipher)\\3_카이사르_암호\\1_caesar\\caesar_enc.txt','wt+')
    h.write(ciphertext)
    h.close
    
    code='ABCDEFGHIJKLMNOPQRSTUWXYZ'
    for key in code:
        if key == 'A':
            h=open('1장_암호(Cipher)\\3_카이사르_암호\\1_caesar\\caesar_dec.txt','wt+')
        else:
            h=open('1장_암호(Cipher)\\3_카이사르_암호\\1_caesar\\caesar_dec.txt','at')
        deciphertext=caesar(ciphertext,key,DEC)
        #print('Deciphered:\t%s' %deciphertext)
        h.write(key)
        h.write('\n============================================\n')
        h.write(deciphertext)
        h.write('\n============================================\n')
        h.close

if __name__ =='__main__':
    main()