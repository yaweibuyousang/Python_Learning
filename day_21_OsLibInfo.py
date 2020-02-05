#OS库基本介绍
'''
os库提供通用的，基本的操作系统交互功能
os库是Python标准库，包含几百个函数
常用路径操作，进程管理，环境参数等几类

路径操作：os.path子库，处理文件路径及信息
进程管理：启动系统中其他程序
环境参数：获得系统软硬件信息等环境参数

路径操作：
os.path子库以path为入口，用于操作和处理文件路径
import os.path
或
import os.path as op

os.path.abspath(path) 返回path在当前系统中的绝对路径
>>>os.path.abspath("file.txt")
'C:\\Users\\Tian Song\\Python36-32\\file.txt'

os.path.normpath(path) 归一化path的表示形式，统一用\\分隔路径
>>>os.path.normpath("D://PYE//file.txt")
'D:\\PYE\\file.txt'

os.path.relpath(path) 返回当前程序与文件之间的相对路径(relative path)
>>>os.path.relpath("C://PYE//file.txt")
'..\\..\\..\\..\\..\\..\\PYE\\file.txt'

os.path.dirname(path) 返回path中的目录名称
>>>os.path.dirname("D://PYE//file.txt")
'D://PYE//file.txt'

os.path.basename(path) 返回path中最后的文件名称
>>>os.path.basename("D://PYE//file.txt")
'file.txt'

os.path.join(path,*paths) 组合path与paths，返回一个路径字符串
>>>os.path.join("D:/","PYE/file.txt")
'D:/PYE/file.txt'

os.path.exists(path) 判断path对应文件或目录是否存在，返回True或False
>>>os.path.exists("D://PYE//file.txt")
False

os.path.isfile(path) 判断path所对应是否为已存在的文件，返回True或False
>>>os.path.isfile("D://PYE//file.txt")
True

os.path.isdir(path) 判断path所对应是否为已存在的目录，返回True或False
>>>os.path.isdir("D://PYE//file.txt")
False

os.path.getatime(path) 返回path对应文件或目录上一次的访问时间
>>>os.path.getatime("D://PYE//file.txt")
1518356633.7551725

os.path.getsize(path) 返回path对应文件的大小，以字节为单位
>>>os.path.getsize("D:/PYE/file.txt")
180768
'''
