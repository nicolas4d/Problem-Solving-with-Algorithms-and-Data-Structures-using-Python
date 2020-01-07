def reverseStr(str):
    if len(str) <= 1 :
        return str
    else :
        return reverseStr(str[1:]) + str[0]

print("hello", reverseStr("hello"))
print(reverseStr("l"))
print(reverseStr("follow"))
print(reverseStr(""))
