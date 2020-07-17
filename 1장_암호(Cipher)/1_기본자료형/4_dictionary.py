
#dictonary

dictdata = { 'star' : 'Sun' , 'planet' : 'Earth' }
print(dictdata['star'])
#Sun

del dictdata['star']

print(dictdata)


print(dictdata.keys())
#key만 모아 리스트로 리턴 

print(dictdata.values())
#value만 모아 리스트로 리턴 

print(dictdata.items())
#키:값 쌍을 맴버로 하는 리스트 제작

del dictdata
#삭제 
