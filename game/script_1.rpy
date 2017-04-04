################################################################################
label ribbon:
    call countdown(10)
    show bg home
    mc "My first day at St. Edmunds Academy for Talented Whales!"
    mc "I hope I get on with the other students."
    mc "Which ribbon should I wear today? Better make it extra special!"
menu:
    "Forest Green":
        $ ribbon_hex = "#228B22"
        $ ribbon = "FOREST GREEN"
        jump ribbon_cont
    "Sunflower Yellow":
        $ ribbon_hex = "#E8DE2A"
        $ ribbon = "SUNFLOWER YELLOW"
        jump ribbon_cont
    "Poppy Red":
        $ ribbon_hex = "#E42F0C"
        $ ribbon = "POPPY RED"
        jump ribbon_cont
    "Bubblegum Blue":
        $ ribbon_hex = "#95FFFE"
        $ ribbon = "BUBBLEGUM BLUE"
        jump ribbon_cont
label ribbon_cont:
    mc "I love my {color=%(ribbon_hex)s}\[%(ribbon)s\]{/color} ribbon!"
    mc "I better get going!"
    hide bg
    jump arrival

################################################################################
label arrival:
    call countdown(9)
    show movie
    play movie "bg longjump.ogv" loop
    show movie

    mc "Oh no, it's already 9:00! I'm going to be late on my first day!"
    play movie "bg corridor.ogv" loop
    mc "I think the classroom is around this corner..."
    play sound "audio/sfx/bump.wav" noloop
    mc "Argh!" with vpunch
    stop sound
    show char bs angry with moveinbottom
    "You appear to have run head-first into an annoyed looking Beluga."
    my_bs "\[ANGRY WHALE SOUNDS\]"
    show char bs neutral
    my_bs "\[WHALE SOUNDS\]"
menu:
    "I'm so sorry! Let me help you up!":
        jump arrival_cont
    "You should watch where you're going next time.":
        jump arrival_cont
label arrival_cont:
    show char bs angry
    my_bs "\[WHALE SOUNDS\]"
    hide char bs neutral with moveoutright
    "They stormed off..."
    jump classroom1

################################################################################
label classroom1:
    call countdown(8)
    play movie "bg classroom.ogv" loop
    
    "Morning classes"
    "You take your seat just as the teacher is about to start."
    show char tc
    tc "\[INTRODUCTORY WHALE SOUNDS\]"
    show char fk happy
    fk "\[SMUG \"WHALE\" SOUNDS\]"
    mc "I don't understand Kira-chan, it's like you aren't speaking whale at all!"
    show char fk sad
    fk "..."
    show char bs neutral
    bs "\[WHALE SOUNDS\]"
    show char bs happy
    bs "\[JOKING WHALE SOUNDS\]"
    bs "\[PUNCHLINE WHALE SOUNDS\]"
    ".{w=0.8}.{w=0.8}.{w=0.8}"
    show char bs joking
    "\*Crickets\*"
    show char bs sad
    ".{w=0.8}.{w=0.8}.{w=0.8}"
    show char tc
    tc ".{w=0.3}.{w=0.3}.{w=0.3}"
    tc "\[WHALE SOUNDS\]"
    show char tc flip
    tc "\[WHALE SOUNDS\]"
    show char tc
    tc "\[MORE WHALE SOUNDS\]"
    show char bb neutral at slowmovein
    $ renpy.pause(20, hard=True)
    "You notice a blue whale creeping into the back of the classroom."
    show char tc
    tc "\[ANNOYED WHALE SOUNDS\]"
    tc "\[MORE ANNOYED WHALE SOUNDS\]"
    show char bb neutral
    "The new entry to the class just takes their seat, and starts twiddling their thumbs."
    "Despite receiving a stern telling-off from J2-sensei, the blue whale doesn't seem to care."
    show char tc
    tc "*sigh*"
    tc "\[WHALE SOUNDS\]"
    tc "\[WHALE SOUNDS\] [mc_name] \[MORE WHALE SOUNDS\]?"
menu:
    "I would prefer to use Monte Carlo Kelp Search for this problem!":
        $ sl_beluga +=1
        $ sl_bigblue -= 1
        tc "\[WHALE SOUNDS!\]"
    "\*Look around classroom for help\*":
        $ sl_bigblue +=1
        $ sl_kira -= 1
        tc "\[WHALE SOUNDS\]"
    "The answer is 42, J2-sensei!":
        $ sl_kira +=1
        $ sl_beluga -= 1
        tc "*sigh*"
label classroom1_cont:
    tc "\[WHALE SOUNDS\]"
    hide char tc
    "The rest of the morning class continues as normal."
    jump break
