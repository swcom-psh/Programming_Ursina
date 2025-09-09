from ursina import *


app = Ursina()

EditorCamera()

class object(Entity):
    def __init__(self, model, x, z):
        super().__init__(
            model = model,
            color = "#8d6d8d",
            scale = (1,1,1),
            position = (x,0,z),
            collider = 'box',
            parent=pivot
        )
    
    def update(self):
        self.rotation_y += 10 * time.dt
        if self.intersects():
            print('충돌함')

pivot = Entity()
a = object('sphere',0,0)
b = object('cube',5,5)
c = object('cube', 10,10)

def update():
    pivot.rotation_y += 20 * time.dt


app.run()