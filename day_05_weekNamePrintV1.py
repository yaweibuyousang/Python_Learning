#weekNamePrintV1.py
weekStr="星期一星期二星期三星期四星期五星期六星期日"
weekId=eval(input("请输入星期数字（1-7）："))
pos=(weekId-1)*3
print(weekStr[pos:pos+3])

#weekNamePrintV2.py
weekStr="一二三四五六日"
weekId=eval(input("请输入星期数字（1-7）："))
print("星期"+weekStr[weekId-1])

'''字符串处理函数
len(x)长度，返回字符串x的长度  eg:len("一二三456")=6
str(x)任意类型x所对应的字符串形式  eg:str(1.23)结果为"1.23" str([1,2])结果为"[1.,2]"
hex(x)或oct(x)整数x的十六进制或八进制小写形式字符串  eg:hex(425)="0x1a9",oct(425)="0o651"

chr(u）x为Unicode编码，返回其对应的字符
ord(x) x为字符，返回其对应的Unicode编码

"1+1=2"+chr(10004)
'1+1=2 √’

"这个字符♉的Unicode值是："+str(ord("♉"))
'这个字符♉的Unicode值是：9801'

'''
for i in range(12):
    print(chr(9800+i),end="")


#字符串处理方法
'''
str.lower()或str.upper() 返回字符串的副本，全部字符小写/大写
eg:"AbCdEfGh".lower()  = "abcdefgh"
str.split(sep=None) 返回一个列表，由str根据sep被分隔的部分组成
eg:"A,B,C".split(",")  = ['A','B','C']
str.count(sub)返回子串sub在str中出现的次数
"an apple a day".count("a")结果为4
str.replace(old,new)  返回字符串str副本，所有old子串被替换为new
eg:"python".replace("n","n123.io") => "python123.io"
str.center(width[,fillchar])字符串str根据宽度width居中，fillchar可选
"python".center(20,"=") => '=======python======='
str.strip(chars)从str去掉在其左侧和右侧chars中列出的字符
"= python= ".strip(" =np") =>"ytho"
str.join(iter)在iter变量除最后元素外每个元素后增加一个str，主要用于字符串分隔
",".join("12345") => "1,2,3,4,5"

'''

#字符串类型的格式化(槽)   ****注意：当字符串长度超过输出宽度时，以字符串长度显示
'''
"{ }:计算机{ }的CPU占用率为{ }%".format("2018-10-10","C",10)
  0         1               2                  0      1   2
    字符串中槽{}的默认顺序                 format()中参数的顺序

字符串中槽的顺序可调调换 eg：
"{1}:计算机{0}的CPU占用率为{2}%".format("2018-10-10","C",10)
  1         0               2                  0      1   2
    字符串中槽{}的顺序                 format()中参数的顺序

'C:计算机2018-10-10的CPU占用率为10%'

format()方法的合适控制：
{<参数序号>:<格式控制标记>}
:   |   <填充> | <对齐> |<宽度>  |   <,>  |<.精度>   | <类型>
引导|用于填充的|<左对齐 |槽设定的|数字的千|浮点数小数|整数类型
符号|单个字符  |>右对齐 |输出宽度|位分隔符|精度或字符|b,c,d,o,x,
                ^居中对齐                  串最大输出 浮点数类型
                                            长度      e,E,f,%
eg:
>>>"{0=:^20}".format("PYTHON")
'=======PYTHON======='

>>>"{0:*>20}".format("BIT")
******************BIT'

>>>"{:10}",format("BIT")
'BIT       '

>>>"{0:,.2f}".format(12345.6789)
'12,345.68'

>>>"{0:b},{0:c},{0:d},{0:x},{0:X}".format(425)
'110101001,Σ,425,651,1a9,1A9'
#c输出为字符形式，d输出为10进制表示形式，x为16进制（小写），X为16进制（大写）

>>>"{0:e},{0:E},{0:f},{0:%}".format(3.14)
'3.140000e+00,3.140000E+00,3.140000,314.000000%'
'''
