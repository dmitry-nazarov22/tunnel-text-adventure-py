import time

def print_animated(text):
    for char in text:
        print(char, end = "", flush = True)
        time.sleep(0.001)
    print()
    time.sleep(0.1)