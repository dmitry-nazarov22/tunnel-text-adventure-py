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

def print_help():
    f = open('data/help.txt', 'r')
    file_contents = f.read()
    print_animated(file_contents, 0.001)
    f.close()


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
    if state["current"] == "quit":
        return

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
        print_animated(f'Score:   {state["player"].score}\n')

    elif state["current"] == "blowed_up":
        os.system('cls' if os.name == 'nt' else 'clear')
        ascii_art = """

        mmmmm  m       mmmm m     m mmmmmm mmmm          m    m mmmmm
        #    # #      m"  "m#  #  # #      #   "m        #    # #   "#
        #mmmm" #      #    #" #"# # #mmmmm #    #        #    # #mmm#"
        #    # #      #    # ## ##" #      #    #        #    # #
        #mmmm" #mmmmm  #mm#  #   #  #mmmmm #mmm"         "mmmm" #


        """
        print_animated(ascii_art, 0.002)
        print_animated(f'Score:               {state["player"].score}\n')
        return

    elif state["current"] == "escape_tunnel":
        state["current"] = "cleared_game"

        os.system('cls' if os.name == 'nt' else 'clear')
        ascii_art = """

        mmmmmm  mmmm    mmm    mm   mmmmm  mmmmmm         mmmm  m    m   mmm    mmm  mmmmmm  mmmm  mmmmmm m    m m
        #      #"   " m"   "   ##   #   "# #             #"   " #    # m"   " m"   " #      #"   " #      #    # #
        #mmmmm "#mmm  #       #  #  #mmm#" #mmmmm        "#mmm  #    # #      #      #mmmmm "#mmm  #mmmmm #    # #
        #          "# #       #mm#  #      #                 "# #    # #      #      #          "# #      #    # #
        #mmmmm "mmm#"  "mmm" #    # #      #mmmmm        "mmm#" "mmmm"  "mmm"  "mmm" #mmmmm "mmm#" #      "mmmm" #mmmmm


        """
        print_animated(ascii_art, 0.002)
        print_animated(f'Score:               {state["player"].score}\n')


    if state["player"].score >= 800 and state["mechanist_quest"] == True and state["lost_worker_quest"] == True and state["current"] == "cleared_game":
        print_block("The air seemed to tear the fabric of the tunnel. When the door clanged open, light burst in, not the cold, artificial glow of lamps, but real, wide, and beautiful. You stand in the ruins, and the world around you seems exposed, nothing is hidden. I'm tired but finally calm. From the radio mechanic gave me comes faint human speech: coordinates, a promise of evacuation. You look outside, where the sky is absurdly bright, and realize that the exit is not only physical.")
    elif state["player"].score >= 500 and state["mechanist_quest"] == True and state["current"] == "cleared_game":
        print_block("The platform greets you with the same emptiness. You decided to return... Feeling fresh air running through ventilations that are humming calmly. Seeing the wasteland and nothing else on the surface, you understood everything... This is the end. You hadn't chosen the most convenient path, but it worked: the generator hummed intermittently, and some doors were open. Around you are those who managed to survive alone, figures who don't smile, but don't run to hide. You walk into the light, but feel an emptiness in your chest. This isn't freedom, it's a compromise: you were alive.")
    elif state["player"].score >= 125 and state["current"] == "cleared_game":
        print_block("You got out. But at what price...  Blowed out the main entrance leaving all the people behind. After seeing the wasteland above you don't even know where you could go. Returning back underground isn't an option. So you try to wander around to find something...")
    else:
        print_block("The doors remain motionless, and the light a rare mirage. You wander the familiar corridors, but they no longer return their promise. The echo follows your steps for too long, reflecting not only the sound but also the emptiness of the decisions you made (or didn't make). You find old signs, warnings, but it's too late—the air has cooled, and the place where you could have escaped is blocked forever.")
