from ursina import *
import random

app = Ursina()
EditorCamera()


objects = 30
speed = 5
somethings = []


for i in range(objects):
    pos = (random.uniform(-10,10), random.uniform(-10,10), random.uniform(-10,10))
    

    a = Entity(model='sphere', color=color.random_color(), scale=2, position=pos, collider='box')    
    a.dis = Vec3(random.uniform(-10,10), random.uniform(-10,10), random.uniform(-10,10))
    somethings.append(a)


def update():
    for a in somethings:
        a.position = a.position + a.dis * speed * time.dt

        if abs(a.x) > 100:
            a.dis.x *= -1
        if abs(a.z) > 100:
            a.dis.z *= -1 
        if abs(a.y) > 100:
            a.dis.y *= -1

        for b in somethings:
            if a == b:
                continue

            if a.intersects(b).hit:
                a.dis *= -1
                b.dis *= -1



app.run()