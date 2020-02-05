def getNum():
    s = input()
    ls = list(eval(s))
    return ls

def mean(numbers):
    s = 0.0
    for i in numbers:
        s += i
    return s/len(numbers)

def dev(numbers,mean):
    sdev = 0.0
    for num in numbers:
        sdev = sdev + (num - mean)**2
    return pow(sdev / (len(numbers)-1),0.5)

def median(numbers):
    numbers.sort()
    size = len(numbers)
    if size % 2 == 0:
        med = (numbers[size//2-1]+numbers[size//2])/2
    else:
        med = numbers[size//2]

    return med

n = getNum()
m = mean(n)
print("平均值:{:.2f},标准差:{:.2f},中位数:{}".format(m,dev(n,m),median(n)))
