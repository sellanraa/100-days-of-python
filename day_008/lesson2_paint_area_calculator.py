# Write your code below this line 👇

import math

def paint_calc(height, width, cover):
    num_cans_rounded_up = int(math.ceil((height * width) / cover))
    print(f"You'll need {num_cans_rounded_up} cans of paint.")

# Write your code above this line 👆
# Define a function called paint_calc() so the code below works.   

# 🚨 Don't change the code below 👇
test_h = int(input("What is the height of the wall in meters? ")) # Height of wall (m)
test_w = int(input("What is the width of the wall in meters? ")) # Width of wall (m)
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
