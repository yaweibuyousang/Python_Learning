#CSV格式清洗与转换

f = open("data.csv")
ls = f.readlines()      #按行一次读取完文件
ls = ls[::-1]           #将数据行倒序排列
lt = []
for items in ls:
    items = items.strip("\n")   #使用strip()方法去掉每行最后的回车
    items = items.replace(" ","")   #使用replace()去掉每行元素两侧的空格
    lt = items.split(",")       #去掉每个元素的分隔符，
    lt = lt[::-1]               #每行元素倒序排列
    print(";".join(lt))         #没行元素的分隔符改为；
f.close()
                        
