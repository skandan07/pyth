x = "110"
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
