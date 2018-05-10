import uuid

num=100
codes=[]
for i in range (num):
    code = str(uuid.uuid1())
    code=code.replace('-','')
    codes.append(code)

for i in codes:
    print i
