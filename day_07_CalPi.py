#CalPiV1.py
'''
计算圆周率
                          0
圆周率的近似计算公式:Π = ∑[1/16^k(4/(8k+1)-2/(8k+4)-1/(8k+5)-1/(8k+6))]
                          ∞
问题分析：
蒙特卡罗方法（N个点落在单位矩形中，到原点的距离小于1的点比大于1的点即为圆周率）

'''
#v1.py(公式法)
pi = 0
N = 100
for k in range(N) :
    pi += 1/pow(16,k)*( \
       4/(8*k+1) - 2/(8*k+4) - \
       1/(8*k+5) - 1/(8*k+6))
print("圆周率值是：{}".format(pi))

#v2.py(蒙特卡罗法)
from random import random
from time import perf_counter
DARTS = 1000*1000
hits = 0.0
start = perf_counter()
for i in range(1,DARTS+1):
    x, y = random(),random()
    dist = pow(x**2+y**2,0.5)
    if dist <= 1.0:
        hits = hits + 1

pi = 4 * (hits/DARTS)
print("圆周率值是:{}".format(pi))
print("运行时间是:{:.5f}s".format(perf_counter()-start))
