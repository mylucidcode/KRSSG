print("The number of time steps is")

#taking in number of time steps
n=int(input())
z=n
a1=[]
t=0
i=1
flag=1
l=True
a=[0,0,0,0,0,0,0,0]
#taking in input of cars every time
while l==True:
    if(i<=n):
        a1 = list(map(int, input().strip().split()))
        i+=1
    for j in range(8):
        a[j] = a[j] + a1[j]

    print(f"time step is {flag}")
    def AS(c1):
        print("A: straight")
        a[0]=a[0]-1
        b1 = max(a)
        c1 = a.index(b1)

        if c1 == 1:
            print("A: Right")
            a[c1] = a[c1] - 1
        if c1 == 2:
            print("B:Straight")
            a[c1] = a[c1] - 1
        if c1 == 7:
            print("D:Right")
            a[c1] = a[c1] - 1

    def AR(c1):
        print("A: Right")
        a[1] = a[1] - 1
        b1 = max(a)
        c1 = a.index(b1)

        if c1 == 3:
            print("B:Right")
            a[c1] = a[c1] - 1
        if c1 == 4:
            print("C:Straight")
            a[c1] = a[c1] - 1

    def BS(c1):
        print("B: straight")
        a[2]=a[2]-1
        b1 = max(a)
        c1 = a.index(b1)

        if (c1 == 3):
            print("B: Right")
            a[c1] = a[c1] - 1
        if (c1 == 0):
            print("A: Straight")
            a[c1] = a[c1] - 1
        if (c1 == 5):
            print("C:Right")
            a[c1] = a[c1] - 1


    def BR(c1):
        print("B: Right")
        a[3]=a[3]-1
        b1 = max(a)
        c1 = a.index(b1)

        if (c1 == 2):
            print("B:Straight")
            a[c1] = a[c1] - 1
        if (c1 == 1):
            print("A:Right")
            a[c1] = a[c1] - 1
        if (c1 == 6):
            print("D:Straight")
            a[c1] = a[c1] - 1


    def CS(c1):
        print("C: straight")
        a[4]=a[4]-1
        b1 = max(a)
        c1 = a.index(b1)

        if (c1 == 3):
            print("B:Right")
            a[c1] = a[c1] - 1
        if (c1 == 0):
            print("A:Straight")
            a[c1] = a[c1] - 1
        if (c1 == 5):
            print("C:Right")
            a[c1] = a[c1] - 1


    def CR(c1):
        print("C: Right")
        a[5]=a[5]-1
        b1 = max(a)
        c1 = a.index(b1)

        if (c1 == 4):
            print("C: Straight")
            a[c1] = a[c1] - 1
        if (c1 == 7):
            print("D: Right")
            a[c1] = a[c1] - 1
        if (c1 == 2):
            print("B: Straight")
            a[c1] = a[c1] - 1


    def DS(c1):
        print("D: straight")
        a[6]=a[6]-1
        b1 = max(a)
        c1 = a.index(b1)

        if (c1 == 3):
            print("B: Right")
            a[c1] = a[c1] - 1
        if (c1 == 7):
            print("D: Right")
            a[c1] = a[c1] - 1
        if (c1 == 4):
            print("C: Straight")
            a[c1] = a[c1] - 1


    def DR(c1):
        print("D: Right")
        a[7]=a[7]-1
        b1 = max(a)
        c1 = a.index(b1)

        if (c1 == 6):
            print("D: Straight")
            a[c1] = a[c1] - 1
        if (c1 == 0):
            print("A: Straight")
            a[c1] = a[c1] - 1
        if (c1 == 5):
            print("C: Right")
            a[c1] = a[c1] - 1


    b = max(a)
    c = a.index(b)
    if c == 0:
        AS(c)


    if c == 1:
        AR(c)

    if c == 2:
        BS(c)

    if c == 3:
        BR(c)

    if c == 4:
        CS(c)

    if c == 5:
        CR(c)

    if c == 6:
        DS(c)

    if c == 7:
        DR(c)
    print(a)
    print("\n")

    for p in range(8):
        if(a[p]>0):
            t+=1
    if(t==0):
        l=False
    t=0;
    flag+=1
















