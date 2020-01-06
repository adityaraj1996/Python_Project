count = 0
def is_prime(n):
    global count
    # for i in range(a, b + 1):
    if n > 1:
        for i in range(2, n//2 + 1):
            if n % i == 0:
                return
        count += 1

def is_prime2(n):
    global count
    # for i in range(a, b + 1):
    if n > 1:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return
        print(n)
        count += 1

a = int(input("enter the lower limit"))
b = int(input("enter the upper limit"))
import time
starttime = time.time()
for c in range(a, b + 1):
    is_prime2(c)
print(count)
print(str(time.time() - starttime))
