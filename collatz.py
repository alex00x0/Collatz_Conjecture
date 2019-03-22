#times it runs
run = 10**2
#successful times
y=0

for i in range(2,run):
    x=i
    while x != 1:
        #print(x)
        if x % 2 == 0:
            x = int(x / 2)
        else:
            x = int(3 * x + 1)
    else:
        y = int(y+1)
print(y)
