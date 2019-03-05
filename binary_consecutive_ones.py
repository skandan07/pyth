#x = 463
#b = bin(x)
# print (b)
#c = str(b)
# print (c)
#d = c[2::]
#print(d)
d="10111101110"
l = len(d)
s = 0
s_max=0
p=1

for i in range(0, l-1):
    if d[i] == "1":
        while True:
            if d[i+1] == "1":
                s= s+1
                if s > s_max:
                    s_max=s
                s=0
                break
            elif d[i+1] == "0":
                break


print(s, s_max)
