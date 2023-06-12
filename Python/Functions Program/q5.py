def power(b,p):
    res=1
    for i in range(p):
        res *= b
    return res
print(power(5,2))
