#enctryption.py
string = input()
for i in range(len(string)):
    if 65 <= ord(string[i]) <= 90:
        print(chr(65+(ord(string[i])-62)%26),end="")
    elif 97 <= ord(string[i]) <= 122:
        print(chr(97+(ord(string[i])-94)%26),end="")
    else:
        print(string[i],end="")
