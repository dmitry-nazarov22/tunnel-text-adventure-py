import time
import textwrap
import os

def print_animated(text):
    for char in text:
        print(char, end = "", flush = True)
        time.sleep(0.005)
    print()
    time.sleep(0.1)

def print_block(text, width=60):
    wrapped = textwrap.fill(text, width)
    for line in wrapped.split("\n"):
        print_animated(line)
    print()

def slow_print(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def print_game_over(state):
    if state["player"].energy <= 0:
        os.system('cls' if os.name == 'nt' else 'clear')
        ascii_art = """

        mmmmmm mm   m mmmmmm mmmmm    mmm m     m        mmmm   mmmmm    mm   mmmmm  mm   m mmmmmm mmmm
        #      #"m  # #      #   "# m"   " "m m"         #   "m #   "#   ##     #    #"m  # #      #   "m
        #mmmmm # #m # #mmmmm #mmmm" #   mm  "#"          #    # #mmmm"  #  #    #    # #m # #mmmmm #    #
        #      #  # # #      #   "m #    #   #           #    # #   "m  #mm#    #    #  # # #      #    #
        #mmmmm #   ## #mmmmm #    "  "mmm"   #           #mmm"  #    " #    # mm#mm  #   ## #mmmmm #mmm"


        """
        slow_print(ascii_art, 0.002)

    elif state["game_msg"] == "blowed_up":
        os.system('cls' if os.name == 'nt' else 'clear')
        ascii_art = """

        mmmmm  m       mmmm m     m mmmmmm mmmm          m    m mmmmm
        #    # #      m"  "m#  #  # #      #   "m        #    # #   "#
        #mmmm" #      #    #" #"# # #mmmmm #    #        #    # #mmm#"
        #    # #      #    # ## ##" #      #    #        #    # #
        #mmmm" #mmmmm  #mm#  #   #  #mmmmm #mmm"         "mmmm" #


        """
        slow_print(ascii_art, 0.002)

    elif state["current"] == "escape_tunnel":
        os.system('cls' if os.name == 'nt' else 'clear')
        ascii_art = """

        mmmmmm  mmmm    mmm    mm   mmmmm  mmmmmm         mmmm  m    m   mmm    mmm  mmmmmm  mmmm  mmmmmm m    m m
        #      #"   " m"   "   ##   #   "# #             #"   " #    # m"   " m"   " #      #"   " #      #    # #
        #mmmmm "#mmm  #       #  #  #mmm#" #mmmmm        "#mmm  #    # #      #      #mmmmm "#mmm  #mmmmm #    # #
        #          "# #       #mm#  #      #                 "# #    # #      #      #          "# #      #    # #
        #mmmmm "mmm#"  "mmm" #    # #      #mmmmm        "mmm#" "mmmm"  "mmm"  "mmm" #mmmmm "mmm#" #      "mmmm" #mmmmm


        """
        slow_print(ascii_art, 0.002)

    print_animated(f'\n\n\n        SCORE:               {state["player"].score}\n\n\n')

