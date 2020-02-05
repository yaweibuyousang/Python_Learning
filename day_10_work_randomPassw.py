#randomPassword.py
import random
def genpwd(length):
    return random.randint(pow(10,length-1),pow(10,length)-1)
length = eval(input())
random.seed(17)
for i in range(3):
    print(genpwd(length))
