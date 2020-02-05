#平方根格式化
#不完全版
num = input()
sqnum=pow(eval(num),0.5,3)
#result=round(sqnum,3)
if len(str(result))<=30:
    print("{:+>30}".format(result))
else:
    print(result)


#标准答案：
a = eval(input())
print("{:+>30.3f}".format(pow(a,0.5)))

        
