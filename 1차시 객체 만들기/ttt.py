from ursina import *
import random

app = Ursina()
EditorCamera()

# -------- 파라미터 설정 --------
num_people = 20
speed = 2

people = []

# -------- 사람 엔티티 생성 --------
for i in range(num_people):
    pos = (random.uniform(-5, 5), 0, random.uniform(-5, 5))
    color_choice = color.blue   # 기본은 건강(파란색)

    # 첫 번째 사람은 감염자 (빨간색)
    if i == 0:
        color_choice = color.red

    p = Entity(
        model='sphere',
        color=color_choice,
        scale=0.7,
        position=pos,
        collider='sphere'
    )

    # 무작위 이동 방향 부여
    p.direction = Vec3(random.uniform(-1, 1), 0, random.uniform(-1, 1)).normalized()
    people.append(p)


# -------- 업데이트 함수 --------
def update():
    for person in people:
        # 이동
        person.position += person.direction * speed * time.dt

        # 벽에 닿으면 반사
        if abs(person.x) > 7:
            person.direction.x *= -1
        if abs(person.z) > 7:
            person.direction.z *= -1

        # 다른 사람들과 충돌 체크
        for other in people:
            if person == other:
                continue

            if person.intersects(other).hit:
                # 감염 규칙: 둘 중 하나가 감염자면 다른 쪽도 감염됨
                if person.color == color.red or other.color == color.red:
                    person.color = color.red
                    other.color = color.red


app.run()
