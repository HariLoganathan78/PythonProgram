print("1,sphere/n2,cylinder/n3,cone/n4,rect_pri/n5,tri_pri/n")
A=int(input("enter the options given"))

def sphere(pi,r):
    sa=4*pi*r*r
    v=(4*pi*r*r)/3
    print("sphere surface area :  ",sa)
    print("sphere volume :  ",v)
def cylinder(pi,r,h):
    sa=(2*pi*r*r)+(2*pi*r*h)
    v=pi*r*r*h
    print("cylinder surface area :  ",sa)
    print("cylinder volume :  ",v)
def cone(pi,r,s,h):
    sa=(pi*r*s)+(pi*r*r)
    v=(pi*r*r*h)/3
    print("cone surface area :  ",sa)
    print("cone volume :  ",v)
def rect_pri(l,w,h):
    sa=2*(l*w+l*h+w*h)
    v=l*w*h
    print("rect_pri surface area :  ",sa)
    print("rect_pri volume :  ",v)
def tri_pri(b,h,s,l):
    sa=b*h+2*l*s+l*b
    v=(l*b*h)/2
    print("tri_pri surface area :  ",sa)
    print("tri_pri volume :  ",v)

if(A==1):
    B=int(input("enter the radius of the sphere : "))
    sphere(3.14,B)
elif(A==2):
    C=int(input("enter the radius of the cylinder : "))
    D=int(input("enter the height of the cylinder : "))
    cylinder(3.14,C,D)
elif(A==3):
    E=int(input("enter the radius of the cone : "))
    F=int(input("enter the height of the cone : "))
    G=int(input("enter the sur of the cone : "))
    cone(3.14,E,F,G)
elif(A==4):
    H=int(input("enter the height of the rect_pri : "))
    I=int(input("enter the length of the rect_pri : "))
    J=int(input("enter the width of the rect_pri : "))
    rect_pri(3.14,H,I,J)
elif(A==5):
     K=int(input("enter the length of the tri_pri : "))
     L=int(input("enter the bridth of the tri_pri : "))
     M=int(input("enter the heigth of the tri_pri : "))
     N=int(input("enter the sur of the tri_pri : "))
     tri_pri(3.14,K,L,M,N)
