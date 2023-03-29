import turtle
import colorsys

t = turtle.Turtle()
s = turtle.Screen()
t.speed(100)
n = 50
h = 0
s.bgcolor("black")
for i in range(1000):
    '''c = colorsys.hsv_to_rgb(h,1,0.8)
    h += 1/n
    t.color(c)
    t.forward(i*3)
    t.left(145)
    '''
    t.color("blue")
    t.circle(i)
    t.left(5)
    
