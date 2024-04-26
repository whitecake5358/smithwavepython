# def function
# def greeting(name):
#     print("welcome " + name)

# calling = greeting
# greeting("kelvin")

# def sales(item):
#     good1 = item + 3
#     good2 = 3 + 3
#     return good1 + good2
# felv = sales(60)
# print(felv)

# def convertsec(seconds):
#     hours = seconds // 3600
#     minutes = (seconds - hours * 3600) // 60
#     remainingsec = seconds - hours * 3600 - minutes * 60
#     return hours, minutes, remainingsec

# hours, minutes, seconds = convertsec(5000)
# print(hours, minutes, seconds)



from turtle import *
import colorsys
bgcolor("black")
tracer (500)

def draw():
    h = 0
    for i in range(100):
        c = colorsys.hsv_to_rgb(h,1,1)
        h += 0.5
        up()
        goto(0,0)
        down()
        color("black")
        fillcolor (c)
        begin_fill()
        rt (98)
        circle(i, 12)
        fd(290)
        fd(i)
        lt(29)
        for j in range(129):
            fd(i)
            circle(j, 299, steps=2) 
        end_fill()
draw()
done()  