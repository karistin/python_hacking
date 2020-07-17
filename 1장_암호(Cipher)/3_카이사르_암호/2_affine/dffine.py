#아핀암호
#전역변수
ENC =0#암호화
DEC =1#복호화

def makeDisk(k1,k2):

    enc_disk={}#암호화
    dec_disk={}#복호화

    for i in range(26):
        enc_i = (k1*i+k2)%26 
        enc_ascii =enc_i+65 
        enc_disk[chr(i+65)] = chr(enc_ascii)
        #            key         value
        dec_disk[chr(enc_ascii)]=chr(i+65)
    return enc_disk,dec_disk

def affine(msg,key1,key2,mode):
    ret=''
      #결과를 위한 빈 문자열 
    msg=msg.upper()#대문자로 변환 
    enc_disk,dec_disk=makeDisk(key1,key2)
    
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
    k1,k2=3,5
    msg='abcdefghijklmnopqrstuvwxyz'
    print('Original:\t%s' %msg.upper())

    msg = affine(msg,k1,k2,ENC)
    print('Affine Cipher:\t%s' %msg)

    msg=affine(msg,k1,k2,DEC)
    print('Deciphered:\t%s' %msg)

if __name__ =='__main__':
    main()
