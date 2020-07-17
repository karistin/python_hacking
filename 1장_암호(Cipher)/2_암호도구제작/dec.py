import enc 
def decryption():
    print('Decrption')

if __name__=='__main__':
    print('dec.py가 메인이다.')
    enc.encryption()
    decryption()
else:
    print('dec.py가 다른 모듈에서 임포트되어 사용됨')