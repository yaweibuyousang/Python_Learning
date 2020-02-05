#4bitRoseNum.py
for i in range(1000,10000):
    s = str(i)
    num=(pow(eval(s[0]),4)+pow(eval(s[1]),4)+pow(eval(s[2]),4)+pow(eval(s[3]),4))
    if i == num:
        print(i)

    else:
        continue
