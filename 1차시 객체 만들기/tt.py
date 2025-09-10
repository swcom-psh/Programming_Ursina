from ursina import *
app = Ursina()

EditorCamera()
window.color = color.black

# --- 중앙 태양 ---
sun = Entity(model='sphere', color=color.yellow, scale=2)

# --- 지구 공전: 피벗(parent)을 중심에 두고 회전시키기 ---
earth_pivot = Entity()                         # (0,0,0) 중심에서 회전
earth = Entity(model='sphere', color=color.azure, scale=0.7,
               parent=earth_pivot, position=(6, 0, 0))   # 반지름=6에 배치

# --- 달 공전도 동일: 피벗을 지구 위치에 두고 그 주위를 회전 ---
moon_pivot = Entity(parent=earth)              # 지구 중심을 기준으로 회전
moon = Entity(model='sphere', color=color.gray, scale=0.25,
              parent=moon_pivot, position=(1.5, 0, 0))   # 지구 반경 1.5

# --- 화성도 추가해보기 ---
mars_pivot = Entity()
mars = Entity(model='sphere', color=color.red, scale=0.5,
              parent=mars_pivot, position=(9, 0, 0))

# 공전 각속도 (도/초)
omega_earth = 30     # 지구 공전 속도
omega_moon  = 180    # 달 공전 속도(지구 주위)
omega_mars  = 24

def update():  
    # time.dt(델타타임) 기반으로 피벗을 회전시키면 자식이 원 궤도로 공전
    earth_pivot.rotation_y += omega_earth * time.dt
    moon_pivot.rotation_y  += omega_moon  * time.dt
    mars_pivot.rotation_y  += omega_mars  * time.dt

# UI 라벨
Text("Sun",  position=(-.47,.43), scale=1, color=color.yellow)
Text("Earth", parent=camera.ui, position=(-.47,.38), scale=1, color=color.azure)
Text("Mars",  parent=camera.ui, position=(-.47,.33), scale=1, color=color.red)

app.run()
