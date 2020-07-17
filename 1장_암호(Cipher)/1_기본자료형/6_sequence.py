
문자열은 문자들의 순서를 가지고 나열하고 있는 것입니다. 'I love python' 이라면 I__l_o_v_e__p_y_t_h_o_n 으로 13글자다(공백포함)
방금 본 문자열 처럼 어떤 객체가 순서를 가지고 나열되어 있는 자료형을 시퀀스 자료형 이라 한다. 시퀀스 자료형은 문자열 리스트 튜플이 있다. 



str = 'I love python'
list = [1,2,3]
tuple = (100,200,300)

파이썬의 시퀀스 자료형은 다음과 같은 공통 특성을 가지고 있습니다.

인덱싱  인덱스를 통해 해당 값에 접근할수 있음 인덱스는 0부터 시작 

슬라이싱 특정구간 취하기 

연결  +

반복 * 

맴버확인 in

길이 정보 len() 



인덱싱 

    ___    apple
    양수    01234
    음수    54321    

    str='I love python'

    print(str[0])
    I
    print(str[-1])
    n
    print(str[12])
    n
    print(str[-13])
    I

슬라이싱

    seqdata[시작인덱스 : 끝인덱스 : 스텝]


    str='I love python'

    str[0:3] 0이상 3미만   I L
    str[3:] 3이상          ove python 
    str[:6] 0이상 6미만    I love
    str[:-3] 0부터 끝에서 3번째 I love pyt
    str[-5:] 끝에서 5번째이상  yton

    str[::2]  Ilv yhn
    str[::-1] nohtp evol i

in
    'O' in str  true 

    dictdata => key로 확인 가능

len()

    길이

