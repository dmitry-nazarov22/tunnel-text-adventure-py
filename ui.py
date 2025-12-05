import time

def print_animated(text):
    for char in text:
        print(char, end = "", flush = True)
        time.sleep(0.015)
    print()
    time.sleep(0.1)