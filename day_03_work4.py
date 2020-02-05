import turtle as t
#风车
t.setup(650,600,0,0)
t.pensize(2)
for i in range(4):
    t.seth(-90*i)
    t.fd(150)
    t.right(90)
    t.circle(-150,45)
    t.right(90)
    t.fd(150)

#风车(standard)
t.pensize(2)
for i in range(4):
    t.seth(-90*i)   #seth设置turtle的绝对坐标（相对0,0）
    t.fd(150)   
    t.right(90)     #right(),left()设置turtle的相对坐标
    t.circle(-150,45)
    t.goto(0,0)

#飞镖
t.setup(650,600,0,0)
t.pensize(2)
for i in range(4):
    t.seth(-90*i)
    t.fd(150)
    t.right(-90)
    t.circle(-150,45)
    t.right(-90)
    t.fd(150)
