from hashlib import sha256 as sha

def hashcash(msg,diffculty):
    nonce=0
    print('++++ Start')
    while True:
        target='%s%d' %(msg,nonce)
        ret = sha(target.encode()).hexdigest()

        if ret[:diffculty] == '0'*diffculty:
            print('++++ Bingo')
            print('--->',ret)
            print('---> NONCE=%d' %nonce)
            break

        nonce +=1

def main():
    msg='Attack at 9PM!'
    difficulty=3
    #문제의 난이도 설정 
    hashcash(msg,difficulty)

main()