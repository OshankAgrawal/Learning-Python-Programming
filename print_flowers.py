from turtle import *
import colorsys
bgcolor("black")
tracer(1000)
def draw ():
    h=0
    for i in range (122):
        c = colorsys.hsv_to_rgb(h,1,1)
        h+=0.1
        up()
        goto(0,0)
        down()
        color("black")
        fillcolor(c)
        begin_fill()
        rt(9)
        circle(i,12)
        fd(290)
        lt(29)
        for j in range (129):
            fd(i)
            circle(j,299,steps=2)
        end_fill()
draw()
done()