caesar(msg,key,mode)는 인자로 입력된 msg를 암호키 key롤 암호문을 만들거나, 암호문을 
평문으로 만듭니다. mode는 암호화 할 것인지, 복호화 할 것인지 나타내는 플래그임니다.



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
        disk=dec_disk
    #mode가 ENC이면 enc_disk를, DEC이면 dec_disk를 변수 disk에 할당합니다.
    for c in msg:
        if c in disk:
            ret +=disk[c]
        else:
            ret +=c
    #msg의 각 문자 c가 disk의 키로 존재하면 c가 키인 값을 ret에 추가하고, 
    #키로 존재하지 않으면 c를 ret에 추가합니다. 
    return ret


lambda 함수는  함수 이름 없이 한 줄로 구성하는 함수입니다.
정의
lambda 인자,인자,...:식

f=lambda x: x*x
f(2)
#4

f=lambda x: (chr(x+65),x)
f(0)
#('A',0)
f(25)
#('Z',25)

map함수는 함수와 반복가능한 자료형을 인자로 받습니다. map()은 반복 가능한 자료형에 있는 모든 맴버를 순차적으로 뽑아내고 이를 인자로 입력된 함수의 인자로 입력하여 얻은 결과를 
묶어서 map 객체로 리턴 
map(함수, 반복 가능한 자료)

def temp(x):
    return x*x

result= map(temp,[0,1,2,3])
print(list(result))
#[0,1,4,9]

#print(result)
#<map object at 0x0060FFD0>

여기서 list()는 반복가능한 자료를 리스트로 변환하는 함수 list()에 사전 자료를 인자로 입력시 키 값만 가지는 리스트 완성
dictdata={'a':97,'b':98}
list(dictdata)
#['a','b']

문자열 포멧팅
%s 문자열
%c 문자 1개
%f 실수
%d 정수 
%% %라는 문자

\n      줄 바꾸기
\t      탭
\(enter)줄 계속(다음 줄도 계속되는 줄이라는 표시)
\\      \문자 자체
\"      "문자 자체 