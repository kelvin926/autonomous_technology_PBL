import threading
import time

value_reg = 0

def gpio_a1():
    while True:
        print(value_reg)
        time.sleep(1)

def main():
    global value_reg
    work = threading.Thread(target=gpio_a1)
    work.start()
    value_reg=int(input())

if __name__ == "__main__":
    main()