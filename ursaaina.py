from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController


app= Ursina()
player = FirstPersonController()

def input(key):
    if key == 'escape':
        app.quit()


for i in range(10):
    i = Entity(
        model = 'cube',
        scale = 2,
        position = (2*i,2*i,2*i),
        color = color.gray,
        collider = 'mesh'

    )



cube = Entity(
    model = 'cube',
    scale = 2,
    color = color.red,
    position = (5,5,5)
)

cube2 = Entity(
    model = 'cube',
    position = (10,10,5),
    scale = 2,
    color = color.green
)


ground = Entity(
    model = 'plane',
    scale = 100,
    position = (0, 0, -10),
    color = color.gold,
    collider = 'mesh'
)



map =[
    [1,2,3,4,5,0,7,8,9,10],
    [1,2,3,4,5,0,7,8,9,10],
    [1,2,3,4,5,0,7,8,9,10],
    [1,2,3,4,5,6,7,8,9,10],
    [1,2,3,4,5,6,7,8,9,10],
    [1,2,3,4,5,6,7,8,9,10],
    [1,2,3,4,5,6,7,8,9,10],
    [1,2,3,4,5,6,7,8,9,10],
    [1,2,3,4,5,6,7,8,9,10],
    [1,2,3,4,5,6,7,8,9,10],
    [1,2,3,4,5,6,7,8,9,10],
    [1,2,3,4,5,6,7,8,9,10]    
]





def update():
    #cube.rotation_x = cube.rotation_x + 0.5
    cube.rotation_x += 0.5
    cube.rotation_y += 0.5

    cube2.rotation_x += 0.5
    cube2.rotation_y += 0.5
    

app.run()

