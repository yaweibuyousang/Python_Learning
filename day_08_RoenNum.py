#RoenNum.py
for i in range(100,1000):
    s = str(i)
    if i == (pow(eval(s[0]),3)+pow(eval(s[1]),3)+pow(eval(s[2]),3)):
        print(i,end=",")

#标准答案1
s = ""
for i in range(100, 1000):
    t = str(i)
    if pow(eval(t[0]),3) + pow(eval(t[1]),3) + pow(eval(t[2]),3) == i :
        s += "{},".format(i)
print(s[:-1])
'''
#标准答案2(待修正)
t = ""
for i in range(100,1000):
    s = str(i)
    if i == (pow(eval(s[0]),3)+pow(eval(s[1]),3)+pow(eval(s[2]),3)):
        t += "{}".format(i)
        print(",".join(t))
'''

