import random
import threading
import time

value_reg1 = 0
value_reg2 = 0

def gpio_a1():
    while True:
        print(value_reg)
        time.sleep(1)

def gpio_a2():
    global value_reg2
    while True:
        value_reg2 = random.randint(0, 1)
        time.sleep(1)

def interrupt(pin, efge, isr):
    while True:
        pass

def new_task(func):
    work = threading.Thread(target=func)
    work.daemon = True
    work.start()

def main():
    global value_reg1

    new_task(gpio_a1)
    new_task(gpio_a2)

    while True:
        value_reg1 = int(input())
        if value_reg2 == 1:
            break

if __name__ == "__main__":
    main()