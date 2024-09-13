

num=[3,4,7,10,11,13]
sum=0
if(num>1):
    for i in range(2,int(num**0.5)+1):
        if(num%i==0):
            print()
        else:
            print(num)
        sum+=num