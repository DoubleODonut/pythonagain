from graphics import *
import time
import random

text_file = open("data.txt", "r")
data = text_file.read().split('\n')
list=[]
for word in data:
    list.append(int(word))


text_file.close()

print list
for word in data:
    print(word)
window = GraphWin("visual", 200, 600)

while True:
    for word in list:
        x = 100
        y = 850 +word * -8
        loadImages = [Image(Point(x,y), "catface1.gif"), Image(Point(x,y), "catface2.gif"), Image(Point(x,y), "catface3.gif"), Image(Point(x,y), "catface4.gif")]
        if word <= 50:
            loadImages[0].draw(window)
        elif word > 50 and word <= 60:
            loadImages[1].draw(window)
        elif word > 60 and word <= 70:
            loadImages[2].draw(window)
        elif word > 70 and word <=100:
            loadImages[3].draw(window)
        

        backdrop = Rectangle(Point(0,0),Point(205,100))
        backdrop.setFill(color_rgb(255,255,255))
        backdrop.draw(window)
        mark = Text(Point(100,50), word)
        mark.setSize(28)
        mark.setStyle('bold')
        mark.draw(window)
        time.sleep(1)
