import threading
import time
import random

value_reg = 0

def gpio_a1():
    gpio_a1.value_reg = 0
    while True:
        print(value_reg)
        time.sleep(1)

def gpio_a2():
    gpio_a2.value_rng = random.randint(0,1)
    time.sleep(1)

def new_thread(gpio_pin):
    work = threading.Thread(target=gpio_pin)
    work.daemon = True
    work.start()

def main():
    new_thread(gpio_a1)
    new_thread(gpio_a2)

    while(True):
        value_reg = int(input())
        
        if gpio_a2.value_reg == 1:
            print("on")
        elif gpio_a2.val_reg == 0:
            print("off")
        else:
            raise ValueError("randint()")

if __name__ == "__main__":
    main()