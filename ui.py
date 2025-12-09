import time
import textwrap

def print_animated(text):
    for char in text:
        print(char, end = "", flush = True)
        time.sleep(0.02)
    print()
    time.sleep(0.1)

def print_block(text, width=60):
    wrapped = textwrap.fill(text, width)
    for line in wrapped.split("\n"):
        print(line)
    print()