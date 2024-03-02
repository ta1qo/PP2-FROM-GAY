import time, math

def root_after_ms(num, ms):
    time.sleep(ms / 1000)
    return math.sqrt(num)

num = 25100
ms = 2123
print(f"Square root of {num} after {ms} miliseconds is {root_after_ms(num, ms)}")
