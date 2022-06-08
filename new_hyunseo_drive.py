from pop import Pilot
from pop import LiDAR

import math
import random

class Lidar:
    def __init__(self, width, directions):
        self.autocar_width = width
        self.degrees = list(range(0, 360, 360 // directions)) # 0 ~ 360도를 directions 개수로 쪼개서 list 만듦.

        self.lidar = LiDAR.Rplidar() # 라이다 게시
        self.lidar.connect()
        self.lidar.startMotor()

    def __del__(self):
        self.lidar.stopMotor() # 클래스 끝날 때 모터 정지.

    def calcAngle(self, length):
        tan = (self.autocar_width / 2) / length
        angle = math.atan(tan) * (180 / math.pi)
        return angle # 차가 턴할 수 있는 최적 각도 구함

    def collisonDetect(self, length):
        detect = [0] * len(self.degrees) # 감지 방향에 따른 2차 배열 준비.
        angle = self.calcAngle(length) # 턴 가능 각도 
        ret = self.lidar.getVectors() # Raw Data
        for degree, distance, _ in ret: # 각도, 거리, 감도
            for i, detect_direction in enumerate(self.degrees): # 각도별 리스트 넣음.
                min_degree = (detect_direction - angle) % 360 # 해당 구역의 최소 앵글부터
                if (degree + (360 - min_degree)) % 360 <= (angle * 2): # 해당 구역의 최대 앵글까지 반복
                    if distance < length:
                        detect[i] = 1 # 해당 구역에 object 있음
                        break
        return detect
print("Start AutoCar!!!")

def main():
    autocar_width = 300
    direction_count = 8
    speed = 50

    car = Pilot.AutoCar()
    lidar = Lidar(autocar_width, direction_count) # 자동차 너비, 감지 방향의 수 (8방향 등등) Class Create
    current_direction = 0 # 진행 방향 숫자 기본 0.
    flag = True

    while flag:
        try:
            # if lidar.collisonDetect(300)[current_direction]: # [진행 방향에서 너무 가까운 경우]
            #     car.stop()
            #     continue

            detect = lidar.collisonDetect(800) # detect 리스트에 거리에 따른 장애물 유무 대입
            new_detect = [detect[0],detect[1],detect[7]] # 전, 우전, 좌전
            
            if sum(detect) == direction_count: # [모든 방향이 막혔을 때]
                car.stop()
                continue
            
            if new_detect[current_direction]: # [해당 방향에 장애물이 있을 때]
                open_directions = [i for i, val in enumerate(new_detect) if not val] # 열린(장애물 없는) 부분 방향 리스트 제작
                if 0 in open_directions:
                    current_direction = 0
                elif (1 in open_directions)|(7 in open_directions):
                    current_direction = random.choice([1,7])
                else:
                    current_direction = 0
            
            speed = 50
            car.setSpeed(speed)
            if current_direction == 0:
                car.steering = 0
                car.forward()
            elif current_direction == 1:
                car.forward()
                car.steering -= 0.2
                car.steering = - 1.0 if car.steering < -1.0 else car.steering
            elif current_direction == 7:
                car.forward()
                car.steering += 0.2
                car.steering = 1.0 if car.steering > 1.0 else car.steering
            else:
                if ((detect[0] == 1) & (detect[1] == 1) & (detect[7] == 1)):
                    car.backward()
                    car.steering -= 0.2
                    car.steering = - 1.0 if car.steering < -1.0 else car.steering
                else:
                    car.forward()
            
            
            print(detect) # 장애물 감지 리스트 출력
            print(current_direction) # 진행방향 출력

        except (KeyboardInterrupt, SystemError): # 컨트롤C나 시스템 오류가 발생할 때, Flag를 False로 변경하여 무한반복 벗어남.
            flag = False
    
    car.stop()
    print('Stopped AutoCar!!!')

if __name__ == '__main__':
    main()
