transposition(msg,key,mode)는 인자로 입력된 문자열 msg를 암호키 key롤 암호화 하거나
복호화 하는 함수입니다. mode는 암호화 또는 복호화를 위한 플래그 

msgsize 문장의 길이 
keysize 암호키의 길이 
ret     결과물 
filler  문장의 길이가 암호키의 길이로 나누어 떨어져야 되기 때문에 없는 부분에 0을 채워넣음 

if msgsize%keysize !=0:
    나머지가 0이 아니면 
    나머지 만큼 filler 에 0이 입력됨 

msg=msg.upper()
msg += filler
msg 대문자화 및 0추가 (없으면 추가 않함)



if mode==ENC:
    #암호화 
    buf=['']*keysize
    buf 는 keysize의 배수배만큼의 칸 
    예시는 ['', '', '', '', '']
    
    for i,c in enumerate(msg):
        col=i%keysize
        #index mod keysize
        index = table[col]
        #enc_table 의  키가 col의 value 값 을  index에 저장 
        buf[index]+=c
        #buf의 index번째에 c를 저장 
        #['EESITNFOHARUE', 'TUXRAHETRSYYO', 'ABBEWDENEWOR0', 'SOUDOREOAAMH0', 'RRIRTUDTTTFOM']

    for text in buf:
        #text는 buf[0],buf[1],buf[2]....
        ret += text


else:
    #복호화
    blocksize = int(msgsize/keysize)

    buf =['']*keysize

    pos=0

    for i in range(keysize):
        text=msg[pos:pos+blocksize]
        #pos부터 pos+blocksize 까지 msg 절단 
        index = table[i]
        #옮길 위치 만들기 buf의 몇번째에 들어가는지 
        buf[index] +=text
        #buf에 입력 
        pos +=blocksize
        #자르는 기준 수정 

    for i in range(blocksize):
        #buf블록 크기만큼 진행 buf[0][i]..
         for j in range(keysize):
             #buf에서 다음 블록으로 건너감 
            if buf[j][i] !='0':
                #buf가  0이 아닌 경우 
                 ret+=buf[j][i]
                 #ret에 값 추가 
return ret 
                