from ursina import *


app = Ursina()

EditorCamera()

ex = Entity(
    name = '철수',
    model = 'cube',
    scale = 5,
    position = (0, 0, 0),
    alpha = 120,
    color = '7fffd4'

)
a =0
b =0
c = 0
i =0
def update():
    ex.position = (a + i, b, c)
    i =+1

app.run()

'''


| 속성명               | 설명                                            
| ----------------- | -------------------------------------------      
| name            | 엔티티 이름                                         
| enabled         | 활성화 여부 (True면 작동)                                                  
| position        | 위치 (Vec3)                                        
| rotation        | 회전 (Vec3)                                         
| scale           | 크기 (Vec3 또는 float)                              
| model           | 모델 이름(str) 또는 NodePath 객체                     
| origin          | 모델 기준점(Vec3), 회전축 등에 영향                    
| shader          | 쉐이더                                              
| texture         | 텍스처 이름(str) 또는 Texture 객체                                               
| color           | 색상 (기본 'color.white')                           
| collider        | 충돌체 유형 ('box', 'sphere', 'capsule', 'mesh' 등) 
| collision       | 충돌 활성화 여부                                    
| parent          | 상위 엔티티                                        
| visible         | 보이는지 여부                                      
| render_queue    | 렌더 우선순위                                      
| always_on_top   | 항상 맨 위에 렌더링                                 
| scripts         | 스크립트 리스트                                     
| material        | 여러 시각 요소 일괄 설정용 dict                      
| tileset_size    | 타일셋 텍스처의 가로, 세로 타일 수                  
| tile_coordinate | 사용할 타일 좌표 (Vec2 또는 튜플)                   
| alpha           | 투명도 (0~~1 또는 0~~255)                          
| unlit           | 조명 무시 여부                                      
| billboard       | 카메라를 향하게 렌더링                                  
| wireframe       | 와이어프레임 모드 표시                                 
| flipped_faces   | 모델 앞뒤 반전 여부                                  
| reflection_map  | 반사맵 (sphere/cube map 생성 시 사용)              
'''