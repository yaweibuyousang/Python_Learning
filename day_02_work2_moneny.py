moneny=input()

if moneny[:3]=="RMB":
    num=eval(moneny[3:])/6.78
    print("USD"+str("{:.2f}".format(num)))
elif moneny[:3]=="USD":
    num=eval(moneny[3:])*6.78
    print("RMB"+str("{:.2f}".format(num)))
    
#标准答案：

CurStr=input()
if CurStr[:3]=="RMB":
    print("USD{:.2f}".format(eval(CurStr[3:])/6.78))
elif CurStr[:3] in ['USD']:
    print("RMB{:.2f}".format(eval(CurStr[3:])*6.78))
