from timeit import default_timer as timer
import sys
#print(sys.float_info.max)
#print(sys.int_info)

start = timer()

def collatz():
    #x = int(10**308.254715559916)
    x = 1844674407370955161
    print(x)
    steps = 0

    while x != 1:
        print(x, end=' ')
        if x % 2 == 0:
            x = int(x / 2)
            steps = steps +1
            print(x)
        else:
            x = int(3 * x + 1)
            steps = steps +1
            print(x)
    else:
        #print(x)
        print("steps: ", steps)

collatz()
#print(end='')
end = timer()
print('time:', end - start)

