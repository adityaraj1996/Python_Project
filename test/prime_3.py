import time
import math
count = 0


def is_prime(n):
    global count
    if n <= 1:
        return False
    if n == 2:
        # print(n)
        return True
        # print(n)
    if n > 2 and n % 2 == 0:
        return False

    for i in range(3, math.floor(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    print(n)
    count += 1


start_time = time.time()

# a = int(input("enter the lower limit").strip())
# b = int(input("enter the upper limit").strip())
for c in range(1, 100):
    is_prime(c)
print(count + 1)
print(str(time.time() - start_time))


