parseKey(key)는 암호키를 분석하여 enc_table과 dec_table을 구성하고 이를 리턴하는 함수




enumerate()

key='ABC'
for index, value in enumerate(key):
    print(index,value)

#0 A
#1 B
#2 C




파이썬 내장 함수인 sorted()는 시퀀스 자료를 인자로 입력받아 정렬 

tmp = [ 5,1,3,7,2]
sorted(tmp)
#[1,2,3,5,7]

tmp=[(0,'B'),(1,'R'),(2,'A'),(3,'I'),(4,'N')]
sorted(tmp,key=lambda x:x[1])

key는 정렬하고자 하는 기준 만드시 sorted()의 key 인자는 반드시 함수!!
이 기준으로 정렬 

lambda x:x[1] 는 (0,'B')에서 뒤의 문자를 의미함 

#[(2, 'A'), (0, 'B'), (3, 'I'), (4, 'N'), (1, 'R')]

그렇다면 사전형 자료는 ???


key 인자를 지정하지 않은 경우 사전자료의 키를 기준으로 정렬 
tmp = {'Mary':1998,'Anna':2001,'Suji':788,'Kelly':4009}
sorted(tmp)

#['Anna', 'Kelly', 'Mary', 'Suji']


키 기준  (키,값)으로 정렬 하고 싶으면 
tmp = {'Mary':1998,'Anna':2001,'Suji':788,'Kelly':4009}
sorted(tmp,key=lambda x: x[1])


#[('Suji', 788), ('Mary', 1998), ('Anna', 2001), ('Kelly', 4009)]

값 기준  (키,값)으로 정렬 하고 싶으면 
tmp = {'Mary':1998,'Anna':2001,'Suji':788,'Kelly':4009}
sorted(tmp,key=lambda x: x[0])

#[('Anna', 2001), ('Kelly', 4009), ('Mary', 1998), ('Suji', 788)]


반대로 정렬할때는 reverse = True로 설정 
tmp = {'Mary':1998,'Anna':2001,'Suji':788,'Kelly':4009}
print(sorted(tmp.items(),key=lambda x: x[0],reverse=True))

#[('Suji', 788), ('Mary', 1998), ('Kelly', 4009), ('Anna', 2001)]




enc_table =
[
    20341
    01234
]

dec_table
[
    01234
    20341
]