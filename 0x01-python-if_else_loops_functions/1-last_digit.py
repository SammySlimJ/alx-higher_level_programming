#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10
number_stats_message = f"Last digit of {number} is {last_digit} and is"
if last_digit > 5:
    print(f"{number_stats_message} greater than 5")
elif last_digit == 0:
    print(f"{number_stats_message} 0")
else:
    print(f"{number_stats_message} less than 6 and not 0")
