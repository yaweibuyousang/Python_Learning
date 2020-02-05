#字符串分段组合(标准答案)
string=input()
newstr=string.split("-")
print("{}+{}".format(newstr[0],newstr[-1]))
