from pop import Pilot
from pop import LiDAR

import math
import random

class Lidar:
    def __init__(self, width, directions):
        self.autocar_width = width
        self.degrees = list(range(0, 360, 360 // directions))

        self.lidar = LiDAR.Rplidar()
        self.lidar.connect()
        self.lidar.startMotor()

    def __del__(self):
        self.lidar.stopMotor()

    def calcAngle(self, length):
        tan = (self.autocar_width / 2) / length
        angle = math.atan(tan) * (180 / math.pi)
        return angle

    def collisonDetect(self, length):
        detect = [0] * len(self.degrees)
        angle = self.calcAngle(length)
        ret = self.lidar.getVectors() # Raw Data
        for degree, distance, _ in ret: # 각도, 거리, 감도
            for i, detect_direction in enumerate(self.degrees):
                min_degree = (detect_direction - angle) % 360
                if (degree + (360 - min_degree)) % 360 <= (angle * 2):
                    if distance < length:
                        detect[i] = 1
                        break
        return detect

print("Start AutoCar!!!")

def main():
    autocar_width = 300
    direction_count = 8
    speed = 50

    car = Pilot.AutoCar()
    lidar = Lidar(autocar_width, direction_count) # 자동차 너비, 감지 방향의 수 (8방향 등등) Class Create
    current_direction = 0
    flag = True

    while flag:
        try:
            if lidar.collisonDetect(300)[current_direction]:
                car.stop()
                continue

            detect = lidar.collisonDetect(800)

            if sum(detect) == direction_count:
                car.stop()
                continue
            
            if detect[current_direction]:
                open_directions = [i for i, val in enumerate(detect) if not val]
                current_direction = random.choice(open_directions)

            """TODO
                car.steering = ? current_direction
            """
            print(detect)

        except (KeyboardInterrupt, SystemError):
            flag = False
    
    car.stop()
    print('Stopped AutoCar!!!')

if __name__ == '__main__':
    main()