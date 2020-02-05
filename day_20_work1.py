#ColumnMeans.py
f = open("latex.log")
s,c = 0,0
for line in f:
    lines = line.split("\n")
    if len(lines)>0:
        s += len(lines)
        c += 1
print(round(s/c))
f.close()


f = open("latex.log")
s,c = 0,0
for line in f:
    lines = line.split("\n")
    if lines == "":
        continue
    s += len(lines)
    c += 1
print(round(s/c))
