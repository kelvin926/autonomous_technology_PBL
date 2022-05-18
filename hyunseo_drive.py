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
    
    def close():
        lidar.stopMotor()
    Lidar.close = close

    def _inner(): # lidar scan data
        return lidar.getVectors()
    
    return _inner # data return


def on_lidar(car, lidar): # lidar data organize
    on_lidar.is_stop = False

    while not on_lidar.is_stop:
        V = lidar() # V에 lidar Raw data 입력.
        print(V)
        
        for v in V:
            if v[0] >= 360 - 15 or v[0] <= 15:
                if v[1] <= 500:
                    Thread(target=car.alarm, args=(4, 8, 1/4)).start()
                print(v[1])

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


def on_cmd():
    while True:
        on_drive.cmd = int(input())

        if on_drive.cmd > 6:
            on_drive.is_stop = True
            break


def main():  
    car = Pilot.AutoCar()

    Thread(target=on_drive, args=(car, )).start()
    Thread(target=on_cmd).start()
    
    # lidar
    lidar = Lidar()
    t = Thread(target=on_lidar, args=(car, lidar))
    t.daemon = True
    t.start()
    # input()
    # on_lidar.is_stop = True
    # Lidar.close()


if __name__ == "__main__":
    main()