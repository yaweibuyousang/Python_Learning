#数字鲁棒输出

s = input()
try:
    if complex(s) == complex(eval(s)):
        print(eval(s)**2)
except:
    print("输入有误")



#注意：不能直接使用eval()，否则，用户可以通过输入表达式（如100**2）输入数字，与要求不同，在实际应用中带来安全隐患
