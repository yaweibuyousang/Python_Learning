steps = 0
def hanoi(src, des, mid, n):
    global steps
    if n == 1:
        steps += 1
        print("[STEP{:>4}] {}->{},n=1".format(steps, src, des))
        print(src,des,mid)
    else:
        hanoi(src, mid, des, n-1)
        print(n)
        print(src,des,mid)
        steps += 1
        print("[STEP{:>4}] {}->{},n!=1".format(steps, src, des))        
        hanoi(mid, des, src, n-1)
        print(src,des,mid)
N = eval(input())
hanoi("A", "C", "B", N)
