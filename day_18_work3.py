import jieba
f = open("沉默的羔羊.txt")
ls = jieba.lcut(f.read())
#ls = f.read().split()
d = {}
for w in ls:
    d[w] = d.get(w,0) + 1
maxc = 0
maxw = ""
for k in d:
    if d[k] > maxc and len(k) >2:
        maxc = d[k]
        maxw = k
    if d[k] = maxc and len(k) >2 and k > maxw:
        maxw = k
print(maxw)
f.close()
