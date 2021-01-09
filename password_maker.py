import random
def generator(string):
    tempList=list(string)
    random.shuffle(tempList)
    return ''.join(tempList)


password=""
for i in range(4):
    password=password+chr(random.randint(55, 90))  + chr (random.randint(38, 57))
password=generator(password)
print(password)