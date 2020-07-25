'python3x'라는 8자로 된 문장을 3DES CBC 모드로 암호화하고, 암호화된 문장을 3DES로 
복호화하는 소스코드입니다.

from Crypto.Cipher import DES3
from Crypto.Hash import SHA256 as SHA256

3DES라이브러리 사용을 위해 Pycryptodome의 필요한 모듈을 import한다.Pycryptodome의
3DES 모듈은 Cyprto.Cipher.DES3입니다.Cyprto.Hash.SHA256 모듈은 3DES의 암호키와 초기화
벡터를 만들 때 활용하기 위함입니다.SHA를 SHA256의 별명으로 사용합니다.

class myDES():

3DES를 위해 myDES라는 이름의 클래스를 정의합니다.이 클래스에는 3DES로 암호화를 수행아는 enc()와 3DES로 복호화를
수행하는 dec() 메소드가 정의되어 있습니다.

def __init__(self,keytext,ivtext): 클래스 생성자 
keytext :클래스 생성 인자. 3DES 암호키 생성을 위한 문자열
ivtext  :초기화 벡터를 위한 문자열
클래스 생성자에서 3DES객체 생성시 사용할 키와 초기화 벡터를 구한다.

keytext='abcdefghijklmnop'처럼 keytext의 길이가 16비트면 3DES의 지원하는 키크기와 같아서 keytext를 바로 
암호키로 활용할 수 있지만 16자나 되는 암호키를 외우기는 힘들다.
따라서 keytext가 무엇이든간에 3DES가 지원하는 길이로 만들어서 이를 3DES키로 활용하면 편리할 겁니다.
SHA256해시는 이런 작업을 수행할 수 있는 아주 훌륭한 도구입니다. 

hash = SHA.new() #SHA256객체 생성후 hash에 할당 
hash.update(keytext.encode('utf-8'))
#hash256 갱신 해시함수는 유니코드를 인식하지 못해 keytext 변환()UTF-8만 인식) 
key=hash.digest()
#key에 저장 
self.key = key[:24]
#pycryptodome에서 제공하는 3DES의 키크기는 16바이트 24바이트여서(아니면 객체생성시 오류 발생)
#그래서 key의 크기 24비트로 슬라이싱 하여 클래스 맴버인 self.key에 할당한다. 
#self.key는 3DES 객체 생성을 위해 인자로 입력되는 키로 사용한다. 


