#CustomerLogin.py
try :
    for i in range(3):
        Name = input()
        Password = input()
        if Name == "Kate" and Password == "666666":
            print("登录成功")
except:
    print("3次用户名或密码均有误！退出程序")
        

#标准答案
count = 0
while count < 3:
    name = input()
    password = input()
    if name == 'Kate'and password == '666666':
        print("登录成功！")
        break
    else:
        count += 1
        if count == 3:
            print("3次用户名或者密码均有误！退出程序。")
