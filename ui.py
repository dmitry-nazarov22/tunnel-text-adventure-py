import time
import textwrap
import os

def print_animated(text, delay=0.01):
    for char in text:
        print(char, end = "", flush = True)
        time.sleep(delay)
    print()

def print_block(text, delay=0.01, width=60):
    wrapped = textwrap.fill(text, width)
    for line in wrapped.split("\n"):
        print_animated(line, delay)
    print()

def print_start():
    os.system('cls' if os.name == 'nt' else 'clear')
    ascii_art = """

 mmmmmmm m    m mm   m mm   m mmmmmm m                          mmmmmmm                 m                      #                         m
    #    #    # #"m  # #"m  # #      #                             #     mmm   m   m  mm#mm          mmm    mmm#  m   m   mmm   m mm   mm#mm  m   m   m mm   mmm
    #    #    # # #m # # #m # #mmmmm #                             #    #*  #   #m#     #           "   #  #" "#  "m m"  #"  #  #"  #    #    #   #   #"  " #"  #
    #    #    # #  # # #  # # #      #            *******          #    #****   m#m     #           m***#  #   #   #m#   #****  #   #    #    #   #   #     #****
    #    *mmmm* #   ## #   ## #mmmmm #mmmmm                        #    "#mm"  m" "m    "mm         "mm"#  "#m##    #    "#mm"  #   #    "mm  "mm"#   #     "#mm"


"""

    desc = "There was once a closed underground line here, built to evacuate the city's leadership. But something went wrong. After the accident, some of the maintenance personnel disappeared, while others remained in the tunnels, but no longer in human form. They hear, but they barely see. The stations were closed and isolated, the documents destroyed, but some records, notes, and torn logs remained. You were unconscious. And now you've come to senses at the collapsed entrance..."

    print_animated(ascii_art, 0.002)

    print_block(desc, 0.002)

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
        print_animated(ascii_art, 0.002)

    elif state["game_msg"] == "blowed_up":
        os.system('cls' if os.name == 'nt' else 'clear')
        ascii_art = """

        mmmmm  m       mmmm m     m mmmmmm mmmm          m    m mmmmm
        #    # #      m"  "m#  #  # #      #   "m        #    # #   "#
        #mmmm" #      #    #" #"# # #mmmmm #    #        #    # #mmm#"
        #    # #      #    # ## ##" #      #    #        #    # #
        #mmmm" #mmmmm  #mm#  #   #  #mmmmm #mmm"         "mmmm" #


        """
        print_animated(ascii_art, 0.002)

    elif state["current"] == "escape_tunnel":
        os.system('cls' if os.name == 'nt' else 'clear')
        ascii_art = """

        mmmmmm  mmmm    mmm    mm   mmmmm  mmmmmm         mmmm  m    m   mmm    mmm  mmmmmm  mmmm  mmmmmm m    m m
        #      #"   " m"   "   ##   #   "# #             #"   " #    # m"   " m"   " #      #"   " #      #    # #
        #mmmmm "#mmm  #       #  #  #mmm#" #mmmmm        "#mmm  #    # #      #      #mmmmm "#mmm  #mmmmm #    # #
        #          "# #       #mm#  #      #                 "# #    # #      #      #          "# #      #    # #
        #mmmmm "mmm#"  "mmm" #    # #      #mmmmm        "mmm#" "mmmm"  "mmm"  "mmm" #mmmmm "mmm#" #      "mmmm" #mmmmm


        """
        print_animated(ascii_art, 0.002)

    print_animated(f'\n\n\nScore:               {state["player"].score}\n\n\n')

