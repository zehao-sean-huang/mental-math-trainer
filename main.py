import os
import random
import time

while True:
    first = random.randint(10, 99)
    second = random.randint(10, 99)
    os.system(f'say what is the product of {first} and {second}')
    start_time = time.time()
    user_computed = -1
    attempt = 0
    while attempt < 5 and user_computed != first * second:
        attempt += 1
        user_computed = int(input('Please enter your answer: '))
    if attempt == 5:
        print(f"failed in {time.time() - start_time} seconds! {first} times {second} is {first * second}")
    else:
        print(f"succeeded in {time.time() - start_time} seconds! {first} times {second} is {first * second}")
