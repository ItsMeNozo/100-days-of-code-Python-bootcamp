"""draw spirograph"""
import turtle as t
import random

tim = t.Turtle()

t.colormode(255)


def rand_color():
    """Return a tuple of rgb"""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b

def draw_spirograph(num_circle):
    tim.hideturtle()
    for _ in range(num_circle):
        tim.speed(0)
        tim.pencolor(rand_color())
        tim.circle(100)
        tim.left(360/num_circle)


"""get colors on image"""
# import colorgram
#
# colors = colorgram.extract('dot-painting.jpg', 30)
# rgb_colors = []
#
# for color in colors:
#     rgb_colors.append((color.rgb.r, color.rgb.g, color.rgb.b))
#
# print(rgb_colors)

color_list = [(249, 248, 248), (233, 244, 241), (237, 240, 245), (249, 244, 247), (8, 18, 35), (151, 86, 54), (49, 32, 23), (234, 208, 86), (31, 98, 148), (195, 139, 122), (94, 5, 19), (151, 65, 96), (205, 97, 74), (162, 160, 45), (97, 162, 202), (23, 93, 62), (164, 135, 161), (143, 16, 39), (121, 202, 180), (2, 63, 140), (142, 39, 31), (49, 113, 77), (7, 57, 40), (179, 87, 121), (143, 217, 227), (209, 177, 215), (121, 220, 218), (61, 157, 82), (56, 73, 36), (57, 133, 200)]


def draw_dot_painting(w, h):
    """draw dot painting with w dots horizontally and h dots vertically"""
    global color_list
    tim.speed("fastest")
    for y in range(0, 50 * h, 50):
        for x in range(0, 50 * w, 50):
            tim.setposition(x, y)
            tim.pencolor(random.choice(color_list))
            tim.down()
            tim.dot(20)
            tim.up()


draw_dot_painting(10, 10)
screen = t.Screen()
screen.exitonclick()

