################################################################################
label splashscreen:
    scene black
    show disclaimer with dissolve
    with Pause(4)
    hide disclaimer with dissolve
    show intro with dissolve
    show ship with moveinright
    hide ship with moveoutleft
    with Pause(4)
    hide intro with dissolve
    with Pause(1)
    return

################################################################################
label start:
    scene black
    stop music fadeout 2.0
    # The "sl" stands for "social links". This makes me happy.
    $ sl_cutoff = 3
    $ sl_beluga = 0
    $ sl_bigblue = 0
    $ sl_kira = 0
    $ mc_name = renpy.input("Please enter your name", default="名前")
    jump ribbon

################################################################################
label credits:
    play music "audio/bensound-memories.mp3"
    stop movie
    scene black
    hide movie
    hide end
    $ renpy.pause(0.1) # Eugh, hacky
    show credit text at creditspan with Pause(45)
    $ renpy.pause(45, hard=True)
    stop music fadeout 2.0
    hide credit text with dissolve
    $ renpy.quit()

################################################################################
label countdown(remaining):
    $ moon_im_name = "moon %s.jpg" % remaining
    image moon = "[moon_im_name]"
    window hide
    show moon
    play sound "audio/moon_1.wav" noloop
    pause(5)
    stop sound fadeout 5
    hide hours 10
    window show
    return
# For the rest of the scenes, look in the following locations:
#
#  script_1 -> ribbon
#           -> arrival
#           -> classroom1
#  script_2 -> break (+ longjump, swimming, dossing)
#  script_3 -> lunch (+ beluga, bigblue, kira)
#  script_4 -> classroom2
#           -> cleaning
#  script_5 -> club (+ comedy, anime, choir)
#  script_6 -> confession (+ beluga, bigblue, falsekiller, lonely)