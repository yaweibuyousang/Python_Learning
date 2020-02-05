def prime(m):
    count = 0
    for i in range(2,m):
        if( m%i) == 0:
            count +=1
    if count == 0:
        return True
    else:
        return False

n = eval(input())
num = round(n)+1
j = 5
Output = ""
while j>0:
    if prime(num):
        j -= 1
        Output += "{},".format(num)
    num += 1
print(Output[:-1])


#标准答案
def prime(m):
    for i in range(2,m):
        if m % i == 0:
            return False
    return True

n = eval(input())
n_ = int(n)
n_ = n_+1 if n_ < n else n_
count = 5

while count > 0:
    if prime(n_):
        if count > 1:
            print(n_, end=",")
        else:
            print(n_, end="")
        count -= 1 
    n_ += 1
