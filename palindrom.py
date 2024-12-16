def pall(st):
    if len(st)==0 or len(st)==1:
        return "true"
    elif st[0] == st[-1]:
        return pall(st[1: -1])
    else:
        return "false"
a = str(input())
print(pall(a))