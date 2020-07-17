#makeDisk(key)는 함호키 'key'를 입력 받아 카이사르 암호디스크를 구성
#암호화 enc_disk 복호화 dec_disk

chr(65)
#a
chr(90)
#z

chr(x+65)
#65~90 :a b c ... z

ord('A')
#65

ord('Z')
#90


keytable =[('A',0),('B',1),('C',2),.....,('Z',25)] 

key2index={'A':0,'B':1,'C':2,...,'Z':25},


enc_disk ={'평문문자' : 암호문자}#암호화
dec_disk ={'암호문자' : 평문문자}#복호화

enc_i = (i+k)%26 #바뀐 문장의 인덱스]

if k=2
    A=>C 
    B=>D 
    ....
enc_i = 2,3,4,5,6,7,8,9,10,...,0,1

enc_disk[char(i+65)] = chr(enc_ascii)
    key=char(i+65)  value = chr(enc_ascii)
    key = A B C D E F ...Z
  value = C D E F G H ...B

dec_disk[chr(enc_ascii)]=chr(i+65)
    key=chr(enc_ascii)  value = =char(i+65) 
    key = C D E F G H ...B
  value = A B C D E F ...Z