d=742
b=[]
while d!=0:
    if d%2==1:
        b.append("1")
    else:
        b.append("0")
    d//2

b.reverse()
print(b)
x="".join(b)
print(x)
l=len(x)
s=0
s_max=0
for i in range(0,l):
    if x[i]=="1":
        s=s+1
    elif x[i]=="0":
        s=0
    if s>s_max:
        s_max=s

print(s_max)
