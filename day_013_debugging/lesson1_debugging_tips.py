############DEBUGGING#####################

# # Describe Problem
# # Problem - range won't reach 20, only 19, expand range by 1 or print at 19 depending on needs
# def my_function():
#   for i in range(1, 20):
#     if i == 20:
#       print("You got it")
# my_function()

# # Reproduce the Bug
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6)
# # print(dice_num)
# # Printing out dice_num allows us to see that randint(1, 6) should be (0, 5) to properly match the range of the list.
# print(dice_imgs[dice_num])

# # Play Computer
# year = int(input("What's your year of birth? "))
# if year > 1980 and year < 1994:
#   print("You are a millenial. ")
# elif year > 1994:
#   print("You are a Gen Z. ")
# # The bug is in the year 1994 - and probably if you enter a year older than 1980 too, but she didn't mention that. It seems either GenZ print or millenial print needs to be =1994 - so that year is assigned to one generation or the other.

# # Fix the Errors
# age = input("How old are you?")
# if age > 18:
# print("You can drive at age {age}.")
# # This is goofy - print is an issue as it isn't indented. But also, the age input needs to be converted to an int and an f string on the print.

# # Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: "))
# # == above rather than = is the issue...
# total_words = pages * word_per_page
# print(total_words)

# # Use a Debugger
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#   b_list.append(new_item)
#   # Needs to be indented within the for loop
#   print(b_list)

# mutate([1,2,3,5,8,13])