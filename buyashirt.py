fr,fd,fs=1000,50,50
sr,sd,ss=900,50,70
ar,ad,ash=800,10,200
tf=fr-((fd/100)*fr)+fs   #if we take % shows remainder
ts=sr-((sd/100)*sr)+ss
ta=ar-((ad/100)*ar)+ash
print(tf)
print(ts)
print(ta)
if(tf<ts and tf<ta):
    print("choose flipkart")
elif(ts<tf and ts<ta):
    print("choose snapdeal")
elif(ta<tf and ta<ts):
    print("choose amazon")
else:
    print()


