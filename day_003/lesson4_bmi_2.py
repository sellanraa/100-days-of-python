# Enter your height in meters e.g., 1.55
height = float(input("What is your heihgt in meters? "))
# Enter your weight in kilograms e.g., 72
weight = int(input("What is your weight in kilograms? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
height_squared = float(height) ** 2

bmi = int(weight) / height_squared

if bmi <= 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 35:
    print(f"Your BMI is {bmi}, you are obese.")
else:
    print(f"Your BMI is {bmi}, you are clinically obese.")
