객체 지향 프로그래밍 하면 떠오르는 것이 바로 클래스 입니다.클래스는 프로그래머가 지정한 이름으로 
만든 하나의 독립된 공간입니다. 이를 'name space' 우리말로 '이름 공간'이라 부른다.
클래스는 클래스 공간에서 정의되어 함수와 동일한 역활을 하는 메소드와 변수 역활을 하는 맴버로 
구성된다. 메소드나 맴버는 이름만 다를 뿐이지 일반적인 함수나 변수와 동일합니다.

클래스 정의

class 클래스 이름(부모 클래스 이름):
    메소드 정의
    맴버 정의

클래스는 상속이 가능한 이름 공간입니다. 상속을 받는 클래스를 자식 클래스, 상속을 하는 클래스를
부모 클래스라고 부릅니다. 상속하는 부모 클래스가 없으면 클래스 정의에서 괄호 속의 부모 클래스
이름을 생략합니다.

class parent():
    def add(self,a,b)
        return  a+b

class child(parent):
    def multiply(self,a,b)
        return a*b

이러면 child가 add 라는 메소드 사용가능하다.


맴버 정의
클래스 맴버는 self.맴버이름으로 정의합니다.파이썬 에서 'self'는 클래스 자신을 지시합니다.
클래스 맴버는 클래스 내에서 전역변수와 같이 사용합니다.

class myClass():
    self.name='samsjang' #맴버 self.name 정의


메소드 정의
클래스 메소드는 일반 함수와 같은 방법으로 정의하되 첫 번째 인자는 반드시 'self'여야 한다.

class myClass():
    def minus(self,a,b):
        return a-b

정의된 메소드를 클래스 안에서 호출하는 경우는 self.메소드와 같이 self를 메소드 이름 앞에
붙여서 호출합니다.


class myClass():
    def minus(self,a,b):
        return a-b

    def result(self,a,b):
        ret = self.minus(a,b)
        return ret +10   

클래스 인스턴스 객체 생성 
정의된 클래스를 실제로 활용하려면 이 클래스를 인스턴스화하여 객체로 생성해야한다.

class myClass():
    def add(self,a,b):
        return  a+b

obj=myClass()
obj.add(1,3)
#4


클래스 생성자와 소멸자
클래스가 생성될때 자동적으로 실행되는 클래스 메소드이며, 클래스 소멸자는 이 클래스의 
인스턴스 객체가 소멸될 때 자동적으로 실행되는 클래스 

클래스 생성자
def __init__(self,인자,인자,...):
    초기화 로직

클래스 소멸자
def __del__(self):
    객체 소멸 시 수행할 로직 