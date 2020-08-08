from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
#PKCS1_OAEP 모듈과 RSA 모듈을 import한다. 

PKCS는 Public Key Cryptodome Standard의 약자로 공개키 암호 표준으로 RSA Security라는
회사에소 정한 공개키 암호의 사용 방식에 대한 표준 프로토콜이다.
PKCS는 그 기능이나 특성에 따라 PKCS#1에서 PKCS#15까지로 구분된다. 일반적이 공개키 
암호표준이라 하면 PKCS#1을 의미한다. 

OAEP는 Optimal asymmetric encryption padding의 약자로 RSA와 함께 사용되며 암호화를
하기 전 메세지에 패딩(padding)이라 부르는 랜덤값을 추가하여 RSA 암호화를 수행 

private_key = RSA.generate(1024)
public_key=private_key.publickey()

1024 비트의 개인키와 공개키를 만든다.

다만 RSA.py 는 실용적이지 못하다. 개인키와 공개키를 생성했지만 프로그램을 종료하면 삭제
된다. 그래서 공개키는 잃어버려도 개인키로 부활 시킬수 있으니 개인키만 파일로 잘 저장
해두면 된다. 