# # Extracting colors from an art image and creating rgb colors inside an empty list.
# import colorgram

# rgb_colors = []
# colors = colorgram.extract('image.jpg',30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color =(r,g,b)
#     rgb_colors.append(new_color)

#all extracted colors that we want to use inside a new list called color_list in the format we need.
color_list = [(134, 167, 191), (211, 156, 106), (197, 143, 166), (29, 110, 168), (234, 214, 86), (127, 74, 92), (187, 178, 19), (26, 136, 66), (55, 18, 26), (142, 20, 40), (38, 175, 113), (225, 170, 
196), (116, 188, 144), (231, 77, 50), (172, 70, 46), (238, 218, 5), (37, 17, 16), (186, 91, 110), (9, 102, 52), (34, 167, 189), (20, 20, 28), (183, 185, 213), (234, 171, 159), (154, 215, 172), (142, 20, 16), (89, 124, 182)]

from turtle import Screen, Turtle
import turtle as t
import random 

p = Turtle()
t.colormode(255)
p.speed("fastest")
p.hideturtle()
p.width(20)

x_cord = -280
y_cord = -280

def random_color():
    random_colors = random.choice(color_list)
    return random_colors

def X_line():
    for X_dot in range(10):
        p.pencolor(random_color())
        p.dot()
        p.penup()
        p.forward(60)
        p.pendown

def Y_line():
    global y_cord
    for _ in range(2):
        new_y_coord = int(y_cord + 30)
        print(new_y_coord)
        p.penup()
        p.goto(x_cord, new_y_coord)
        y_cord = new_y_coord
        p.pendown

for item in range(8):
    p.penup()
    p.goto(-280,0)
    p.pendown
    Y_line()
    X_line()

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()
