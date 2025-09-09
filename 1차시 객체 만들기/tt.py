from ursina import *

app = Ursina()

# 화면에 글자 출력
message = Text(text='Hello Ursina!', scale=2, color=color.yellow, position=(0,0))

# 3D 공간에도 배치 가능 (parent를 scene으로 설정)
label = Text(text='이건 3D 공간', world_z=2, parent=scene, color=color.red)

EditorCamera()
app.run()
