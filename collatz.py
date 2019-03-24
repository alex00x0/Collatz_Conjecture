from timeit import default_timer as timer

start = timer()
#times it runs
run = 10**2 + 1
#successful times
y=0
steps = 0

for i in range(2,run):
    x=i
    print("x value:", x)
    while x != 1:
        if x % 2 == 0:
            x = int(x // 2)
            steps = steps +1
        else:
            x = int(3 * x + 1)
            steps = steps +1
    else:
        print("steps: ", steps)

end = timer()
print(end - start)
