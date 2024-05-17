l = [1,0,1]
val = 0
for i in range(len(l)):
    val += l[i]*10**(len(l)-i-1)

print(val)
