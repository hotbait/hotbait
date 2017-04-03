label club:
menu:
    "Comedy will help fill the sadness inside of me.":
        bb "\[WHALE SOUNDS\]"
        hide char bb
        $ sl_beluga += 1
        $ sl_kira -= 1
        jump club_comedy
    "I hear all whale kids love the animes!":
        bb "\[WHALE SOUNDS\]"
        hide char bb
        $ sl_kira += 1
        $ sl_bigblue -= 1
        jump club_anime
    "I sing really well! Take me to whurch (whale church)!":
        show char bb happy
        bb "\[WHALE SOUNDS\]"
        hide char bb
        $ sl_bigblue += 1
        $ sl_beluga -= 1
        
        jump club_choir

################################################################################
label club_comedy:
    window hide
    show hours 2
    pause(3)
    hide hours 2
    window show

    play movie "bg corridor.ogv" loop

    mc "Hmm, I hope this is the right room for the comedy club..."
    my_bs "\[WHALE SOUNDS\]"
    mc "Is that...?"

    play movie "bg comedy.ogv" loop

    show char bs neutral
    bs "\[WHALE SOUNDS\]"
    show char bs excited
    bs "\[WHALE SOUNDS\]"
    show char bs thinking
    bs "\[WHALE SOUNDS\]"
    show char bs joking
    bs "\[WHALE SOUNDS\]"
    hide char bs joking
    "..."
    show char bs neutral
    "Beluga-senpai is looking around the room."
    "No one is laughing."
menu:
    "Cheer for Beluga-senpai":
        jump club_comedy_neg
    "Wave at Beluga-senpai":
        jump club_comedy_pos
    "Do nothing":
        jump club_comedy_neg

label club_comedy_neg:
    $ sl_beluga -= 1
    jump club_comedy_cont

label club_comedy_pos:
    $ sl_beluga += 1
    jump club_comedy_cont

label club_comedy_cont:
    bs "\[WHALE SOUNDS\]"
    "What will you do?"
menu:
    "Talk to Beluga-senpai":
        jump club_comedy_cont_2
    "Talk to the other students":
        jump club_comedy_cont_2

label club_comedy_cont_2:
    hide char beluga neutral
    my "Hey - it's your turn!"
    "You're pushed towards the stage."
    "Everyone is watching you."
    "Beluga-senpai catches your eye."
menu:
    "\"It's so nice to {b}SEA{/b} so many of you here!\"":
        jump club_comedy_joke1
    "\"Hey comedy club, what's the {b}KRAKEN?{/b}\"":
        jump club_comedy_joke1
    "\"Thanks Beluga-chan! You really {b}KRILLED{/b} it!\"":
        $ sl_beluga -= 1
        jump club_comedy_joke1

label club_comedy_joke1:
    "There are some giggles from the audience."
menu:
    "\"I don't know about you, but I'm having a {b}WHALE{/b} of a time!\"":
        jump club_comedy_joke2
    "\"This is my first time here - can I get a little {b}KELP{/b}?\"":
        jump club_comedy_joke2
    "\"I won't {b}BELUGA{/b} the point - I love comedy club!\"":
        $ sl_beluga -= 1
        jump club_comedy_joke2

label club_comedy_joke2:
    "You're doing well. Keep it up!"
menu:
    "\"I never thought I was all that {b}FINNY{/b}..!\"":
        $ sl_beluga -= 1
        jump club_comedy_joke3
    "\"I {b}SHELL{/b} take my leave!\"":
        jump club_comedy_joke3
    "\"Thank you! {b}WATER{/b} wonderful crowd!\"":
        jump club_comedy_joke3

label club_comedy_joke3:
    "The audience loves you! You're really {b}making waves{/b}."
    $ success = (sl_beluga > sl_cutoff)
    if success:
        show char bs blush
        bs "..."
        hide char bs blush
    else:
        "You look around the room, but can't see Beluga-senpai..."
    "What a roller-coaster of emotion."
    jump club_cont

################################################################################
label club_anime:
    window hide
    show hours 2
    pause(3)
    hide hours 2
    window show

    play movie "bg anime.ogv" loop

    "You arrive at the anime clubroom."
    "It looks like Kira-chan arrived before you."
    show char fk neutral
    fk "\[\"WHALE\" SOUNDS\]"
    mc "Kira-chan~!"
    "Kira-chan seems to have ignored you."
menu:
    "\*Make random noises\*":
        show char fk happy
        fk "\[\"WHALE\" SOUNDS\]"
        $ sl_kira += 1
        jump club_anime_1
    "\"KIRA-CHAAAA~N!\"":
        show char fk scared
        fk "\[\"WHALE\" SOUNDS\]"
        jump club_anime_1

label club_anime_1:
    show char fk neutral
    fk "\[\"WHALE\" SOUNDS\]"
menu:
    "\"I love both Shojou and Shonen anime~!\"":
        $ sl_kira += 1
        show char fk happy
        jump club_anime_2
    "\"...in this economy?\"":
        show char fk joking
        jump club_anime_2
    "\"Er, b-bananas?\"":
        $ sl_kira -= 1
        show char fk disapproval
        jump club_anime_2

label club_anime_2:
    show char fk thinking
    fk "\[\"WHALE\" SOUNDS\]"
menu:
    "\"White hair? Better get too attached to them!\"":
        $ sl_kira += 1
        show char fk excited
        jump club_anime_3
    "\"That's not fiscally responsible...\"":
        $ sl_kira -= 1
        show char fk sad
        jump club_anime_3
    "\"Yeah, yeah! ...Potassium.\"":
        show char fk joking
        jump club_anime_3

label club_anime_3:
    show char fk neutral
    fk "\[\"WHALE\" SOUNDS\]"
menu:
    "\"Death Note is totally my favourite too!\"":
        $ sl_kira += 1
        show char fk panic
        jump club_anime_4
    "\"I just think that's a bit spiteful.\"":
        $ sl_kira -= 1
        show char fk disapproval
        jump club_anime_4
    "\"It's good for you, Kira-chan.\"":
        show char fk scared
        jump club_anime_4

label club_anime_4:
    hide char fk
    "The rest of anime club passes enjoyably."
    $ success = (sl_kira > sl_cutoff)
    if success:
        show char fk happy
        fk "\[\"WHALE\" SOUNDS\]"
        hide char fk happy
    else:
        "Kira-chan heads off quickly afterward."
    "What a roller-coaster of emotion."
    jump club_cont

################################################################################
label club_choir:
    window hide
    show hours 2
    pause(3)
    hide hours 2
    window show

    play movie "bg choir.ogv" loop

    show char bb neutral
    mc "Big Blue! I didn't know you could sing!"
    show char bb joking
    bb "\[WHALE SOUNDS\]"
    show char bb panic
    bb "\[PANICKED WHALE SOUNDS\]"
menu:
    "\"Blue-chan! I promise I won't tell a soul!\"":
        $ sl_bigblue += 1
        show char bb happy
        jump club_choir_2
    "\"You should share your talents with the whole school~!\"":
        show char bb thinking
        jump club_choir_2
    "\"Are you kidding? I'm totally telling the whole swim team!\"":
        $ sl_bigblue -= 1
        show char bb scared
        jump club_choir_2
label club_choir_2:
    hide char bb
    show char bb neutral
    "Big Blue moves to the front and starts singing."
    mc "He has the voice of a wangel (whale angel)..!"
    "Big Blue hits all the notes beautifully."
    hide char bb neutral
    show char bb happy
    "The song comes to an end."
menu:
    "\"Let's sing a duet together, Big Blue!\"":
        hide char bb happy
        show char bb excited
        jump club_choir_3
    "\"Your form is wonderful, Big Blue!\"":
        $ sl_bigblue += 1
        hide char bb happy
        show char bb love
        jump club_choir_3

label club_choir_3:
    "You feel like your singing has improved."       
    $ success = (sl_bigblue > sl_cutoff)
    if success:
        show char bb love
        bb "\[IMPRESSED WHALE SOUNDS\]"
        hide char bb love
    else:
        show char bb panic
        "You sing horribly off-key."
    "What a roller-coaster of emotion."
    jump club_cont

################################################################################
label club_cont:
    hide char
    jump confession
