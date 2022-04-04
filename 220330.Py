import random
import threading
import time

def gpio_a1():
    gpio_a1.value = 0
    while True:
        print("gpio_a1.value : ",gpio_a1.value)
        time.sleep(1)

def gpio_a2():
    gpio_a2.value = 0
    while True:
        gpio_a2.value = random.randint(0, 1) # value_reg가 오타로 보여, 변수에 직접 대입.
        print("gpio_a2.value : ",gpio_a2.value)
        time.sleep(1)

def interrupt(pin, edge, isr):
    old_state = pin
    # print("[dev]old_state : ", old_state)
    while True:
        pin = gpio_a2.value # 따라서, pin에 계속 gpio_a2.value 값을 반영.
        if edge == True: # 상승 0 --> 1
            if old_state == 0 and pin == 1:
                old_state = pin # pin = 1
                print("상승")
                isr()
            else: # 하강 1 --> 0
                if old_state == 1 and pin == 0:
                    old_state = pin # pin = 0
                    print("하강")
                    isr()

def new_task(func, *argx):
    work = threading.Thread(target=func, args=argx)
    work.daemon = True
    work.start()

def my_isr():
    print("call my_isr")

def main():
    new_task(gpio_a1)
    new_task(gpio_a2)
    new_task(interrupt, gpio_a2.value, True, my_isr) # pin, edge, isr
    # 여기에서 random값인 gpio_a2.value를 넣어봤자, 스레딩되고 있는 gpio_a2.value값이 반영되지 않는다.
    # 즉, 해당 task가 '시작될 때'의 value가 들어가기 때문에, interrupt가 실행되지 않는다. -> 22번 라인으로.
    
    while True:
        gpio_a1.value = int(input()) # 여기 루프에 빠져서 isr문으로 가지 못함.

if __name__ == "__main__":
    main()