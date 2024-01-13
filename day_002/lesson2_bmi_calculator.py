# 1st input: enter height in meters e.g: 1.65
height = 1.65
# 2nd input: enter weight in kilograms e.g: 72
weight = 73
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
height_squared = float(height) ** 2

bmi = int(weight) / height_squared

bmi_as_int = int(bmi)

print(bmi_as_int)    
