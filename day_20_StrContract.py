#英文字母的鲁棒输入

s = input()
p = ""
for i in s:
    if ord(i) in range(65,91) or ord(i) in range(97,123):
        p += i
print(p)

#标准答案
alpha = []
for i in range(26):
    alpha.append(chr(ord('a')+i))
    alpha.append(chr(ord('A')+i))
s = input()
for c in s:
    if c in alpha:
        print(c,end="")
