import random,string

forsSelect = string.ascii_letters+"0123456789"

def generate (filename,count,length):
    f = open(filename,'a')
    for i in range (count):
        for m in range (length):
            f.write(random.choice(forsSelect))
        f.write('\n')

    for x in range(count):
        Re = ""
        for y in range (length):
            Re+=random.choice(forsSelect)
        print (Re)

if __name__ == "__main__":
    filename = 'active_code.txt'
    digit = 20
    num = 200
    generate(filename,num,digit)