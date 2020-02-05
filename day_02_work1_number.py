template="零一二三四五六七八九"

s = input()

for c in s:
    #print中增加end=""参数表示输出后不增加换行，多个print可以连续输出
    print(template[eval(c)],end="")
    
