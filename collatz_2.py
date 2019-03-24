from timeit import default_timer as timer
import sys
#print(sys.float_info.max)
#print(sys.int_info)

start = timer()

def collatz():
    x = 10**1000000000
    steps = 0

    while x != 1:
        #print(x, end=' ')
        if x % 2 == 0:
            #// returns int instead of a float (allowing for larger numbers)
            x = int(x // 2)
            steps = steps +1
        else:
            x = int(3 * x + 1)
            steps = steps +1
    else:
        #print(x)
        print("steps: ", steps)

collatz()
#print(end='')
end = timer()
print('time:', end - start)
