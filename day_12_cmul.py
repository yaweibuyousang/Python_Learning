def cmul(a, *b):
    m = a
    print(type(a)) #int
    print(type(b))  #元组(tuple)
    print(b)    #s[1:]
    for i in b:
        print(type(i))
        m *= i
    return m

print(eval("cmul({})".format(input())))
