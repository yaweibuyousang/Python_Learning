#PythonDraw.py
#import为保留字，turtle 为绘图库，最小单位为像素

'''Python计算生态=标准库+第三方库
    标准库：随解释器直接安装到操作系统中的功能模块
    第三方库：需要经过安装才能使用的功能模块
    库Library，包Package，模块Module，统称为模块

    turtle空间坐标系：
        绝对坐标：窗口初始打开时，turtle位于窗口中心位置，中心点为原点（0,0），
        turtle运行方向为向右（X轴），向上为（Y轴）
        
    turtle.goto(x,y) goto至窗口中任意一位置

    turtle自身的坐标：turtle的运动方向为前进方向，反方向为后退方向，
    运行方向左侧为左侧方向，运行方向右侧为右侧方向
    turtle.fd(d)向turtle的正前方向运动d
    turtle.bk(d)向turtle的反方向运动d
    turtle.circle(r,angle)沿turtle左侧的某一点做圆运动

    turtle的角度坐标体系
    X轴方向为0/360°，Y轴方向为90/-270°
    turtle.seth(angle)设置turtle的方向角度
    seth()改变turtle行进方向，但只改方向不行进，angle为绝对角度
     
    turtle.left(angle) turtle.right(angle)向左或右改变turtle的方向
    
    RGB色彩体系：红绿蓝，覆盖视力所能感知的所有颜色，每色取值范围为0-255整数或0-1小数
    eg：
        white    255,255,255  1,1,1          白色
        yellow   255,255,0    1,1,0          黄色
        magenta  255,0,255    1,0,1          洋红
        cyan     0,255,255    0,1,1          青色
        blue     0,0,255      0,0,1          蓝色
        black    0,0,0        0,0,0          黑色
        seashell 255,245,238  1,0.96,0.93    海贝色
        gold     255,215,0    1,0.84,0       金色
        pink     255,192,203  1,0.75,0.80    粉红色
        brown    165,42,42    0.65,0.16,0.16 棕色
        purple   160,32,240   0.63,0.13,0.94 紫色
        tomato   255,99,71    1,0.39,0.28    番茄色

    turtle RGB默认采用小数值 可切换为整数值
    turtle.colormode(mode)    1.0:RGB小数值  255：RGB整数值


import

    库引用：
    扩充Python程序功能的方式
    使用import保留字完成，采用<a>.<b>()编码风格
    ①import<库名>
    <库名>.<函数名>(<函数参数>)

    import更多用法：
    使用from和import保留字共同完成
    ②from<库名>import<函数名>
    from<库名>import *
    <函数名>(<函数参数>)

    compare
    import <库名>
    <库名>.<函数名>(<函数参数>)
    该调用为对应库的库函数的调用

    from <库名> import *
    <函数名>(<函数参数>)
    该调用为程序中独立的函数

    第一种方法不会出现函数重名问题
    第二种易出现库中函数与程序中自定义函数重名

    ③import <库名> as <库别名>
    <库别名>.<函数名>(<函数参数>)

    
turtle的画笔控制函数
    penup(),pendown()成对出现
    penup()画笔抬起，turtle在窗口上飞，可进行画笔的移动
    pendown()画笔落下，turtle在窗口上爬。可进行画笔的绘画
    pensize(),pencolor()*画笔的设置一直有效，直至下次重新设置*
    pensize(width)==width(width)
    画笔宽度，即turtle的腰围
    pencolor(color)color为颜色字符串或rgb值 
    画笔颜色，turtle在涂装
    color参数有三种形式：1)"相应的颜色英语单词"，eg:("purple");2)rgb的小数值.eg:(0.63,0.13,0.94);3)RGB的元组值((0.63,0.13,0.94))


turtle运动控制函数
    fd()==forward() -d：行进距离，可为负数
    向前行进，turtle走直线
    
    circle(r,extent=none)
    根据半径r绘制extent角度的弧度
    -r：默认圆心在turtle左侧r距离的位置，可为负数
    -extent：绘制角度，默认为360°整圆


turtle方向控制函数（绝对角度&turtle角度）
    setheading(angle)==seth(angle)
    改变行进方向，turtle走角度（当前turtle的角度，即绝对角度）

    left(angle),right(angle)turtle在当前行进方向上向左/右旋转angle°（相对角度）

循环结构：
    for i in xxx

range()函数
range(N)产生0到N-1的整数序列，共N个
range(M,N)产生M到N-1的整数序列，共N-M个
        
'''
#method1
import turtle
#turtle.setup(width,height,startx,starty),后两个参数为可选项
turtle.setup(650,350,200,200)
turtle.penup()
turtle.fd(-250)
turtle.pendown()
turtle.pensize(25)
turtle.pencolor("purple")
turtle.seth(-40)
for i in range(4):
    turtle.circle(40,80)
    turtle.circle(-40,80)
turtle.circle(40,80/2)
turtle.fd(40)
turtle.circle(16,180)
turtle.fd(40*2/3)
#运行至done后，程序不会主动退出，需手动关闭窗口
turtle.done()

#method2
from turtle import *
setup(650,350,200,200)
penup()
fd(-250)
pendown()
pensize(25)
pencolor("purple")
seth(-40)
for i in range(4):
    circle(40,80)
    circle(-40,80)
circle(40,80/2)
fd(40)
circle(16,180)
fd(40*2/3)
done()


import turtle as t
t.setup(650,350,200,200)

