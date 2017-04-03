################################################################################
label lunch:
    window hide
    show hours 5
    pause(3)
    hide hours 5
    window show
    
    play movie "bg lunch.ogv" loop
    mc "The cafeteria is so crowded! I don't recognise many people..."
    "I can see Kira-chan and Beluga-senpai. Big Blue is smoking outside."
    "Who should I sit with?"
menu:
    "Beluga-senpai":
        jump lunch_beluga
    "Big Blue":
        jump lunch_bigblue
    "Kira-chan":
        jump lunch_falsekiller

################################################################################
label lunch_beluga:
    show char bs neutral
    "You sit down next to Beluga-senpai."
    "They appear to be reading a paper about MCKS."
    bs "..."
    show char bs happy
    bs "\[WHALE SOUNDS\]"
    show char bs angry
    bs "\[WHALE SOUNDS\]"
    show char bs disapproval
    bs "\[WHALE SOUNDS\]?"
menu:
    "Kira-chan is great! Everyone here is so nice~!":
        jump lunch_beluga_neg
    "Kira-chan? They're nice, but we're just friends.":
        jump lunch_beluga_pos
    "I- I don't know what you're talking about!":
        jump lunch_beluga_neg

label lunch_beluga_neg:
    $ sl_beluga -= 1
    bs "\[WHALE SOUNDS\]"
    show char bs angry
    bs "\[WHALE SOUNDS\]"
    bs "\[WHALE SOUNDS\]"
    hide char bs angry
    jump lunch_cont

label lunch_beluga_pos:
    $ sl_beluga += 1
    show char bs neutral
    bs "\[WHALE SOUNDS\]"
    bs "\[WHALE SOUNDS\]"
    show char bs happy
    bs "\[WHALE SOUNDS\] {color=%(ribbon_hex)s}\[%(ribbon)s\]{/color} \[WHALE SOUNDS\]"
    show char bs panic
    bs "\[WHALE SOUNDS\]"
    show char bs joking
    bs "\[WHALE SOUNDS\]"
    hide char bs joking with moveoutright
    "Beluga-senpai ran off again..."
    jump lunch_cont

################################################################################
label lunch_bigblue:
    play movie "bg longjump.ogv" loop

    mc "Big Blue!"
    show char bb neutral
    mc "I don't smoke but can I join you Big Blue?"
    show char bb angry
    bb "\[WHALE SOUNDS\]"   
menu:
    "Oh, of course, vaping is much better for your lungs!":
        $ sl_bigblue += 1
        jump lunch_bigblue_vape
    "You could spend more money on protein if you quit vaping!":
        $ sl_bigblue -= 1
        jump lunch_bigblue_quit
    "Is it krill flavoured?":
        jump lunch_bigblue_flavour

label lunch_bigblue_vape:
    show char bb happy
    bb "\[WHALE SOUNDS\]"
    show char bb neutral
menu:
    "You are looking large today, Big Blue!~":
        jump lunch_bigblue_end
    "I saw Kira-chan lift a really heavy box earlier!":
        $ sl_bigblue -= 1
        jump lunch_bigblue_badend

label lunch_bigblue_quit:
    bb "\[WHALE SOUNDS\]"
    bb "\[WHALE SOUNDS\]"
menu:
    "You're so big, Blue-chan! I was only concerned about your intake!":
        $ sl_bigblue += 1
        jump lunch_bigblue_end
    "You are looking a bit small, Blue-chan!":
        $ sl_bigblue -= 1
        jump lunch_bigblue_badend

label lunch_bigblue_flavour:
    show char bb panic
    bb "\[WHALE SOUNDS\]"
    show char bb joking
    bb "\[WHALE SOUNDS\]"
    bb "\[WHALE SOUNDS\]"
menu:
    "It's nice that a big strong whale will admit to liking that flavour, Blue-chan!":
        $ sl_bigblue += 1
        jump lunch_bigblue_goodend
    "That's an...unusual flavour":
        $ sl_bigblue -= 1
        jump lunch_bigblue_badend

label lunch_bigblue_goodend:
    play movie "bg longjump.ogv" loop
    show char bb happy
    bb "\[WHALE SOUNDS\]"
    jump lunch_bigblue_end

label lunch_bigblue_end:
    bb "\[WHALE SOUNDS\]"
    bb "\[WHALE SOUNDS\]"
    hide char bb
    jump lunch_cont

label lunch_bigblue_badend:
    show char bb neutral
    bb "\[WHALE SOUNDS\]"
    show char bb sad
    bb "\[WHALE SOUNDS\]"
    hide char bb sad at slowmoveout
    jump lunch_cont

################################################################################
label lunch_falsekiller:
    "Kira-chan looks awkward as they are sitting alone."
    mc "Hello, Kira-chan! Your blowhole looks cute today!"
    show char fk love
    fk "\[\"WHALE\" SOUNDS\] {color=%(ribbon_hex)s}\[%(ribbon)s\]{/color} \[\"WHALE\" SOUNDS\]"
    show char fk neutral
    fk "\[\"WHALE\" SOUNDS\]"
menu:
    "I don't like the cafeteria decor either, Kira-chan!!":
        jump lunch_falsekiller_2
    "Yes! {color=%(ribbon_hex)s}\[%(ribbon)s\]{/color} is my favourite colour! Thank you for noticing~~~":
        $ sl_kira += 1
        jump lunch_falsekiller_2
    "Mitochondria IS the powerhouse of the cell!!":
        $ sl_kira -= 1
        jump lunch_falsekiller_2

label lunch_falsekiller_2:
    fk "\[\"WHALE\" SOUNDS\]"
    fk "\[\"WHALE\" SOUNDS\]"
    show char fk excited
    fk "\[\"WHALE\" SOUNDS\]"
    show char fk neutral
    fk "\[\"WHALE\" SOUNDS\]"
menu:
    "I am also a fan of Luigi's fine krill products":
        $ sl_kira += 1
        jump lunch_falsekiller_3
    "Anchovies? That's immoral!":
        $ sl_kira -= 1
        jump lunch_falsekiller_3
    "I think me might be on steroids too!!!~~~":
        jump lunch_falsekiller_3

label lunch_falsekiller_3:
    fk "\[\"WHALE\" SOUNDS\]"
    show char fk joking
    fk "\[\"WHALE\" SOUNDS\]"
menu:
    "Anime? I've never heard of it!~":
        jump lunch_falsekiller_4
    "Er...sure?":
        jump lunch_falsekiller_4
    "I'm sure you don't associate with that kind of sealife!":
        $ sl_kira -= 1
        jump lunch_falsekiller_4

label lunch_falsekiller_4:
    fk "\[\"WHALE\" SOUNDS\]"
    fk "\[\"WHALE\" SOUNDS\]"
    jump lunch_cont

################################################################################
label lunch_cont:
    hide char
    jump classroom2