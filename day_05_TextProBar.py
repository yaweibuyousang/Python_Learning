#TextProBarV1.py
import time
scale = 10
print("------执行开始------")
for i in range(scale+1):
    a='*'*i
    b='.'*(scale-i)
    c=(i/scale)*100
    print("{:^3.0f}%[{}->{}]".format(c,a,b))
    time.sleep(0.1)
print("------执行结束------")

#进度条单行刷新：  \r
#刷新的本质：用之后打印的字符覆盖之前的字符
#不能换行：print()需要被控制
#要能回退：打印后光标退回到之前的位置\r

#TextProBarV2.py
import time
for i in range(101):
    print("\r{:3}%".format(i),end="")
    time.sleep(0.1)
    

