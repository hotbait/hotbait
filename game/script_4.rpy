################################################################################
label classroom2:
    window hide
    show hours 4
    pause(3)
    hide hours 4
    window show
    play movie "bg classroom.ogv" loop

    # Afternoon class
    "Time for biology class!"
    show char tc
    tc "\[WHALE SOUNDS\]"
    tc "\[WHALE SOUNDS\]"
    tc "\[WHALE SOUNDS\]"
    tc "\[WHALE SOUNDS\]"
    show char fk joking
    fk "\[\"WHALE\" SOUNDS\] %(mc_name)s \[\"WHALE\" SOUNDS\]"
    show char tc
    tc "\[WHALE SOUNDS\]"
menu:
    "Orcas go through menopause.":
        jump classroom2_2
    "Short-finned pilot whales?":
        jump classroom2_2
    "I- I don't know.":
        jump classroom2_2

label classroom2_2:
    tc "\[WHALE SOUNDS\]"
    tc "\[WHALE SOUNDS\]"
menu:
    "S- Some of my best friends are killer whales!":
        jump classroom2_3
    "Preliminary studies indicate that humans experience the menopause.":
        jump classroom2_3
    "Erm...seahorses?":
        jump classroom2_3
    
label classroom2_3:
    tc "\[WHALE SOUNDS\]"
    show char fk neutral
    fk "\[\"WHALE\" SOUNDS\]"
    show char tc
    tc "\[WHALE SOUNDS\]"
    tc "\[WHALE SOUNDS\]"
    hide char tc
    jump cleaning

################################################################################
label cleaning:
    window hide
    show hours 3
    pause(3)
    hide hours 3
    window show

    play movie "bg classroom.ogv" loop

    mc "I'm supposed to be cleaning with Big Blue? Where in the sea could they be?"
    my "♪\[WHALE SOUNDS\]♪"
    mc "It's coming from the cupboard..."

    play movie "bg closet.ogv" loop
    
    show char bb happy
    bb "♪\[WHALE SOUNDS\]♪"
    mc "Hello Big Blue! Have you got any plans after we're done cleaning?"
    show char bb thinking
    bb "\[WHALE SOUNDS\]"
    mc "It's mandatory?! What clubs are there?"
    show char bb neutral
    bb "\[WHALE SOUNDS\]"
    jump club