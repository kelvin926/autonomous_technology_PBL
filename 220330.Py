import random
import threading
import time

def gpio_a1():
    gpio_a1.value = 0
    while True:
        print(gpio_a1.value)
        time.sleep(1)

def gpio_a2():
    gpio_a2.value = 0
    while True:
        value_reg2 = random.randint(0, 1)
        time.sleep(1)

def interrupt(pin, edge, isr):
    old_state = pin
    while True:
        if edge == True: #상승 0 --> 1
            if old_state == 0 and pin == 1:
                old_state = pin
                isr()
            else: #하강 1 --> 0
                if old_state == 1 and pin == 0:
                    old_state = pin
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
    new_task(interrupt, gpio_a2.value, True, my_isr)
    
    while True:
        gpio_a1.value = int(input())

if __name__ == "__main__":
    main()