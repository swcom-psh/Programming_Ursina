from ursina import *
import random, math

app = Ursina()

EditorCamera()
window.color = color.black

# 은하 파라미터
num_stars = 500       # 은하 별 개수
galaxy_radius = 100
arms = 4
arm_spread = 0.3

# 별 색상 팔레트 (청백, 황백, 적색 계열)
star_colors = [
    color.rgb(180, 200, 255),   # 푸른별
    color.rgb(255, 255, 255),   # 흰별
    color.rgb(255, 240, 200),   # 노란별
    color.rgb(255, 200, 150),   # 주황별
    color.rgb(255, 180, 180)    # 붉은별
]

stars = []

for i in range(num_stars):
    # 반경과 각도
    r = random.uniform(2, galaxy_radius)
    angle = (r * 0.25) + (i % arms) * (2*math.pi/arms)
    angle += random.uniform(-arm_spread, arm_spread)
    
    x = math.cos(angle) * r
    z = math.sin(angle) * r
    y = random.uniform(-3, 3)
    
    star = Entity(
        model='sphere',
        scale=random.uniform(0.05, 0.2),              # 크기 다양화
        color=random.choice(star_colors),             # 색상 랜덤
        position=(x,y,z)
    )
    stars.append(star)

# 은하 중심 (초대질량 블랙홀 영역)
core = Entity(model='sphere', color=color.yellow, scale=4, position=(0,0,0))

# 은하 회전
rotation_speed = 5

def update():
    for s in stars:
        s.parent = core
    core.rotation_y += rotation_speed * time.dt

# --- 배경 별 무작위 배치 ---
for _ in range(300):
    bx = random.uniform(-300, 300)
    by = random.uniform(-300, 300)
    bz = random.uniform(-300, 300)
    Entity(model='sphere',
           scale=random.uniform(0.05, 0.15),
           color=color.rgb(200,200,255),
           position=(bx,by,bz))

app.run()
