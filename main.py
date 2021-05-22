print("The number of time steps is")

#taking in number of time steps
n=int(input())
z=n
a1=[]
a=[]
#taking in input of cars every time
for i in range (0,z):
    a1 = list(map(int, input().split()))
    for j in range(0,8):
        a[j]=a[j+1]+a1[j]

    b=max(a)
    c=a.index(b)
    flag=1
    def switch1(c):
        s1={
            0:AS(),
            1:AR(),
            2:BS(),
            3:BR(),
            4:CS(),
            5:CR(),
            6:DS(),
            7:DR(),
        }
        s1.get(c)
    def AS(c1):
        print("A straight")
        a[0]=a[0]-1
        if flag==2:
            a[c1]=a[c1]-1
            def switch2(c1):
                s2={
                    1:"A: Right",
                    2:"B: Straight",
                    7:"D: Right"
                }
                s2.get(c1)
        continue

    def AR(c1):
        print("A Right")
        a[1] = a[1] - 1
        if flag == 2:
            a[c1] = a[c1] - 1
            def switch3(c1):
                s3 = {
                    3: "B: Right",
                    4: "C: Straight",
                }
                s3.get(c1)
        continue
    def BS(c1):
        print("B straight")
        a[2]=a[2]-1
        if flag == 2:
            a[c1] = a[c1] - 1
            def switch4(c1):
                s4 = {
                    3: "B: Right",
                    0: "A: Straight",
                    5: "C: Right",
                }
                s4.get(c1)
        continue
    def BR(c1):
        print("B Right")
        a[3]=a[3]-1
        if flag == 2:
            a[c1] = a[c1] - 1
            def switch5(c1):
                s5 = {
                    2: "B: Straight",
                    1: "A: Right",
                    6: "D: Straight",
                }
                s5.get(c1)
        continue
    def CS(c1):
        print("C straight")
        a[4]=a[4]-1
        if flag == 2:
            a[c1] = a[c1] - 1
            def switch6(c1):
                s6 = {
                    3: "B: Right",
                    0: "A: Straight",
                    5: "C: Right",
                }
                s6.get(c1)
        continue
    def CR(c1):
        print("C Right")
        a[5]=a[5]-1
        if flag == 2:
            a[c1] = a[c1] - 1
            def switch7(c1):
                s7 = {
                    4: "C: Straight",
                    7: "D: Right",
                    2: "B: Straight",
                }
                s7.get(c1)
        continue
    def DS(c1):
        print("D straight")
        a[6]=a[6]-1
        if flag == 2:
            a[c1] = a[c1] - 1
            def switch8(c1):
                s8 = {
                    3: "B: Right",
                    7: "D: Right",
                    4: "C: Straight",
                }
                s8.get(c1)
        continue
    def DR(c1):
        print("D Right")
        a[7]=a[7]-1
        if flag == 2:
            a[c1] = a[c1] - 1
            def switch9(c1):
                s9 = {
                    6: "D: Straight",
                    0: "A: Straight",
                    5: "C: Right",
                }
                s9.get(c1)
        continue
    b1=max(a)
    c1=a.index(b1)

    def switch(c1):
        s = {
            0:AS(c1),flag++
            1:AR(c1),flag++
            2:BS(c1),flag++
            3:BR(c1),flag++
            4:CS(c1),flag++
            5:CR(c1),flag++
            6:DS(c1),flag++
            7:DR(c1),flag++
        }
        s.get(c1)
    flag=1
    if i==(z-1):
        for k in range(0,8):
            if a[k]>0:
                z=z+1
                break





