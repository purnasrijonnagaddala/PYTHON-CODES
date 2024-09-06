

n1=int(input())
n2=int(input())
count=0
for i in range(n1,n2+1):
    if i>1:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            print(i,end=" ")
