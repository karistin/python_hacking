#List

listdata = [1 , 'a' , 'I love Python' , [0,1,2]]
print(listdata[3][0])
#0

listdata = [1,2,3]
listdata.append(4)

print(listdata)
#[1, 2, 3, 4]

listdata.remove(2)

print(listdata)
#[1, 3, 4]

del listdata[0]
print(listdata)
#[3, 4]

del listdata
# 삭제 
