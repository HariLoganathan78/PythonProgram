string=input("enter the string:")
a=len(string)
if a%5==0:
    b=string[::-1]
    c=b.upper()
    print(c)
else:
    print("the length of the string is not multiple of 5")
