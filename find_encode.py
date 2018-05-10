import re

def statistice(file_path):
    f = open(file_path,'r').read()
    f = re.findall(r'[\w\-\_\.\']+',f)
    print f
    print len(f)

if __name__=="__main__":
    filepath = 'C:\Users\LH\PycharmProjects\untitled\english.txt'
    statistice(filepath)