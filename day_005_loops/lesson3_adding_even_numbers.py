target = int(input("Enter a number between 0 and 1000. "))

# 🚨 Do not change the code above ☝️
# I did change the code above to be interactive and to accommodate for some of these exercises being inherently flawed due to limitations of Auditorium
# Write your code here 👇
sum_of_even = 0

for number in range(0, target + 1, 2):
    sum_of_even += number

print(sum_of_even)