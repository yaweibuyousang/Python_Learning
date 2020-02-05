#equilateral triangle 星号三角形

getNum=eval(input())

for i in range(getNum//2+1):
    star=(i*2+1)*'*'
    blank=' '*(getNum//2-i)
    print("{:<}{}{}".format(blank,star,blank))
