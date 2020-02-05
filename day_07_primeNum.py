#primeNum.py
sum = 0
count = 0
for i in range(2,100):
    for j in range(1,i):
        if( i % j) == 0:
            count +=1
    if count == 1:
        sum = sum + i
    count = 0
print(sum)


#标准答案：

def is_prime(n):
    for i in range(2,n):
        if n%i == 0:
            return False
    return True

sum = 0
for i in range(2,100):
    if is_prime(i):
        sum += i
print(sum)
