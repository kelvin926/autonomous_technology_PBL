'''
1. 기본적으로 전방으로 감
2. Lidar On, 
'''

from pop import Pilot
from pop import LiDAR
from threading import Thread
import time

# lidar
def Lidar():
    lidar = LiDAR.Rplidar()
    lidar.connect()
    lidar.startMotor()
    
    def _inner(): # lidar scan data
        return lidar.getVectors()
    
    return _inner # data return

def lidar_drive():
    if lidar_analysis.Analysis_data[0] <= 500 # 전방 감지


def lidar_analysis():
    for v in (on_lidar.Raw_Data):
        if v[0] >= 335 or v[0] <= 25: # 전방 50도 한정
            Front_raw = 90000 #debug
            for i in v[0]:
                if i <= Front_raw: #최소값 구함
                    Front_raw = i 

        if v[0] > 25 and v[0] <= 90: # 우측 전방 한정
            R_front_raw = 90000 #debug
            for i in v[0]:
                if i <= R_front_raw: #최소값 구함
                    R_front_raw = i

        if v[0] > 90 and v[0] <= 155: # 우측 후방
            R_rear_raw = 90000 #debug
            for i in v[0]:
                if i <= R_rear_raw: #최소값 구함
                    R_rear_raw = i 

        if v[0] > 155 and v[0] <= 205: # 후방
            Rear_raw = 90000 #debug
            for i in v[0]:
                if i <= Rear_raw: #최소값 구함
                    Rear_raw = i 

        if v[0] > 205 and v[0] <= 270: # 좌측 후방
            L_rear_raw = 90000 #debug
            for i in v[0]:
                if i <= L_rear_raw: #최소값 구함
                    L_rear_raw = i 

        if v[0] >= 270 and v[0] <= 335: # 좌측 전방
            L_front_raw = 90000 #debug
            for i in v[0]:
                if i <= L_front_raw: #최소값 구함
                    L_front_raw = i 
        
        Analysis_data = [Front_raw, R_front_raw, R_rear_raw, Rear_raw, L_front_raw, L_rear_raw]
        lidar_drive()

def on_lidar(car, lidar): # lidar data organize
    on_lidar.is_stop = False

    while not on_lidar.is_stop:
        Raw_Data = lidar() # V에 lidar Raw data 입력.
        lidar_analysis()
        time.sleep(0.1)
# lidar end



def on_drive(car):
    on_drive.is_stop = False
    on_drive.cmd = 0

    steering = 0
    speed = 50

    car.steering = steering
    car.setSpeed(speed)

    while not on_drive.is_stop:
        if on_drive.cmd == 1:
            car.forward()
        elif on_drive.cmd == 2:
            car.backward()
        elif on_drive.cmd == 3:
            steering -= 0.1
            steering = -1.0 if steering < -1.0 else steering
            car.steering = steering
        elif on_drive.cmd == 4:
            steering += 0.1
            steering = 1.0 if steering > 1.0 else steering
            car.steering = steering
        elif on_drive.cmd == 5:
            speed += 5
            speed = 99 if speed >= 99 else speed
            car.setSpeed(speed)
        elif on_drive.cmd == 6:
            speed -= 5
            speed = 20 if speed < 20 else speed
            car.setSpeed(speed)
        
        print(steering, speed)

        on_drive.cmd = 0
        time.sleep(0.1)
    
    car.steering = 0
    car.stop()





def main():  
    car = Pilot.AutoCar()
    Thread(target=on_drive, args=(car, )).start()

    # lidar
    lidar = Lidar()
    t = Thread(target=on_lidar, args=(car, lidar))
    t.daemon = True
    t.start()



if __name__ == "__main__":
    main()