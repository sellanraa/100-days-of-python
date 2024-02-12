from turtle import Screen
import turtle as t
import random

timmy = t.Turtle()
timmy.shape("turtle")
timmy.color("orange")
timmy.width("2")

# # Draw a square:
# timmy = Turtle()
# timmy.shape("turtle")
# timmy.color("orange")

# for _ in range(4):
#     timmy.forward(100)
#     timmy.left(90)

# # Aliasing example:
# import turtle as t

# # Draw a dashed line

# for _ in range(4):
#     for _ in range(15):
#         timmy.forward(5)
#         timmy.penup()
#         timmy.forward(5)
#         timmy.pendown()
#     timmy.left(90)

# # Draw different shapes
# colors = ["aquamarine4", "blue4", "CadetBlue", "cornsilk4", "DarkOrange", "DarkSlateGrey", "ForestGreen", "gray40", "IndianRed", "LightBlue1", "LightGreen"]

# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         timmy.forward(100)
#         timmy.right(angle)

# for shape_side_n in range(3, 11):
#     timmy.color(random.choice(colors))
#     draw_shape(shape_side_n)

# # Random walk - later adding random colors rather than named from a list

# # colors = ["aquamarine4", "blue4", "CadetBlue", "cornsilk4", "DarkOrange", "DarkSlateGrey", "ForestGreen", "gray40", "IndianRed", "LightBlue1", "LightGreen"]

# # Tuples are immutable...
# # colors_tuple = ("aquamarine4", "blue4", "CadetBlue", "cornsilk4", "DarkOrange", "DarkSlateGrey", "ForestGreen", "gray40", "IndianRed", "LightBlue1", "LightGreen")

# t.colormode(255)

# def random_color():
#     r = random.randint(0,255)
#     g = random.randint(0,255)
#     b = random.randint(0,255)
#     random_color = (r, g, b)
#     return random_color

# directions = [0, 90, 180, 270]

# timmy.speed(0)

# for i in range(200):
#     # timmy.color(random.choice(colors_tuple))
#     timmy.color(random_color())
#     steps = int(random.randrange(1, 6) * 10)
#     timmy.setheading(random.choice(directions))
#     timmy.forward(steps)

# # Draw a spirograph
# t.colormode(255)
# timmy.speed(0)

# def color():
#     r = random.randint(0,255)
#     g = random.randint(0,255)
#     b = random.randint(0,255)
#     color = (r, g, b)
#     return color

# for _ in range(120):
#     timmy.color(color())
#     timmy.circle(100)
#     timmy.setheading(timmy.heading() + 3)


screen = Screen()
screen.exitonclick()