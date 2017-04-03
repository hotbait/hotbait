################################################################################
label break:
    window hide
    show hours 7
    pause(3)
    hide hours 7
    window show

    play movie "bg corridor.ogv" loop

    show char fk panic
    fk "\[\"WHALE\" SOUNDS\]"
    mc "I'm sorry could you repeat that, Kira-chan?"
    show char fk angry
    fk "\[\"WHALE\" SOUNDS\]"
    show char fk neutral
    fk "\[\"WHALE\" SOUNDS\]"
    mc "Oh? A sports? Whatever should I pick?"

menu:
    "Nothing like gliding through the water~~~ Can you jump Kira-chan?":
        $ sl_kira +=1
        $ sl_beluga -=1
        $ sl_bigblue -=1
        show char fk happy
        fk "\[WHALE SOUNDS\]"
        hide char fk happy
        jump break_longjump
    "There’s nowhere else but the pool to have splishy-splashy fun!!!":
        $ sl_beluga -=1
        $ sl_bigblue +=1
        show char fk sad
        fk "\[WHALE SOUNDS\]"
        hide char fk sad
        jump break_swimming
    "Sorry. I don’t swim. ~~~ I fell over on the way to school!!!":
        $ sl_beluga +=1
        $ sl_kira -=1
        show char fk disapproval
        fk "\[WHALE SOUNDS\]"
        hide char fk disapproval
        jump break_dossing

################################################################################
label break_longjump:
    window hide
    show hours 6
    pause(3)
    hide hours 6
    window show

    play movie "bg longjump.ogv" loop

    show char fk panic
    "There’s Kira-chan! They look like they’ll soar through the watair!"

menu:
    "Go talk to Kira-chan. They look so alone!":
        show char fk happy
        $ sl_kira +=1
        jump break_longjump_cont1
    "Avoid Kira-chan. I never know what they are saying! It could be awkward!":
        show char fk sad
        $ sl_kira -=1
        jump break_longjump_cont1        

label break_longjump_cont1:
    fk "\[\"WHALE\" SOUNDS\]"
    show char fk neutral
    fk "\[\"WHALE\" SOUNDS\]"  

menu:
    "\"What was that about bottle-nose diving?\"":
        $ sl_kira -=1
        show char fk panic
        jump break_longjump_cont2
    "\"You'll be fine Kira-chan! I believe in you!\"":
        $ sl_kira +=1
        show char fk love
        jump break_longjump_cont2
    "\"I'll be much worse!\"":
        show char fk disapproval
        jump break_longjump_cont2
    
label break_longjump_cont2:
    fk "\[\"WHALE\" SOUNDS\]"
    show char fk neutral
    fk "\[\"WHALE\" SOUNDS\]"

menu:    
    "\"I wish I had bunked off with Beluga-senpai!\"":
        $ sl_kira -=1
        jump break_longjump_cont3
    "\"At least if we make the effort, J2-sensei will like us!!\"":
        $ sl_kira +=1
        jump break_longjump_cont3
    "\"I’m not worried at all!\"":
        jump break_longjump_cont3
        
label break_longjump_cont3:
    hide char fk neutral with moveoutright
    "..."
    "\[\"WHALE\" SCREAMS\]"
    jump break_cont
                
################################################################################
label break_swimming:
    window hide
    show hours 6
    pause(3)
    hide hours 6
    window show

    play movie "bg swimming.ogv" loop

    "It’s so rare to find a whale school where you can swim! There’s Big Blue!"
    show char bb neutral
    mc "Hey Blue-chan! I never thought you’d be good at swimming!"
    show char bb angry
    bb "\[ANGRY WHALE SOUNDS\]"

menu:
    "\"I guess muscle is more important than streamlining!\"":
        $ sl_bigblue +=1
        jump break_swimming_cont
    "\"I’ll believe it when I see it!\"":
        $ sl_bigblue -=1
        jump break_swimming_cont
    "\"I can’t swim either, Blue-chan!\"":
        jump break_swimming_cont
        
label break_swimming_cont:
    show char bb excited
    "We have to select swimming partners!"

menu:
    "\"Big Blue! Come be my partner!\"":
        jump break_swimming_partner
    "\"I think I’ll swim alone!\"":
        jump break_swimming_nopartner
        
label break_swimming_partner:
    $ sl_bigblue -=1
    show char bb disapproval
    bb "\[WHALE SOUNDS\]"
    show char bb neutral
menu:
    "If only I could tame their rebelliousness and make them mine!":
        jump break_swimming_cont1
    "How disobedient! I could never love such a ruffian!":
        jump break_swimming_cont1


label break_swimming_nopartner:
    $ sl_bigblue +=1
    hide char bb excited
    show char bb happy
    bb "\[WHALE SOUNDS\]"
    hide char bb excited
    show char bb neutral

menu:
    "They respect my need to swim through this life independently!":
        jump break_swimming_cont1
    "Why didn’t blue volunteer to be my partner?!":
        jump break_swimming_cont1

label break_swimming_cont1:
    bb "\[WHALE SOUNDS\]"

menu:
    "\"Thank you Blue-chan!~~ I’ve practiced swimming a lot!!!~~~\"":
        $sl_bigblue +=1
        show char bb love
        bb "..."
        hide char bb love
        jump break_cont
    "\"Well it’s easy right?\"":
        $sl_bigblue -=1
        show char bb angry
        bb "..."
        hide char bb angry
        jump break_cont
    "\"Oh! It’s nothing really!\"":
        show char bb joking
        bb "..."
        hide char bb joking
        jump break_cont
    
################################################################################
label break_dossing:
    window hide
    show hours 6
    pause(3)
    hide hours 6
    window show

    play movie "bg nurse.ogv" loop

    "You pretend you're ill."

    show char nr
    play sound "audio/sfx/nr1.wav" noloop
    nr "\[WHALE SOUNDS\]"
    stop sound
    play sound "audio/sfx/nr2.wav" noloop
    nr "\[WHALE SOUNDS\]"
    stop sound
    show char bs neutral
    bs "\[WHALE SOUNDS\]"
    mc "What are you doing here, Beluga-senpai?"

menu:
    "Sit next to Beluga-senpai":
        jump break_dossing_next
    "Sit opposite Beluga-senpai":
        jump break_dossing_opposite

label break_dossing_next:
    show char bs blush
    bs "..."
    show char bs angry
    bs "\[Whale sounds\]"
    hide char bs angry with moveoutright
    $ sl_beluga += 1
    "Beluga-senpai ran off again..."
    jump break_dossing_cont

label break_dossing_opposite:
    bs "\[Whale sounds\]?"

menu:
    "Nothing!":
        jump break_dossing_opposite_ab
    "I was looking at...your glasses! They’re nice!~":
        jump break_dossing_cont
    "You.":
        jump break_dossing_opposite_flirt

label break_dossing_opposite_flirt:
    bs "\[Whale sounds\]"
    show char bs blush
    $ sl_beluga += 1
    jump break_dossing_cont

label break_dossing_cont:
    show char nr
    play sound "audio/sfx/nr2.wav" noloop
    nr "\[Whale sounds\]"
    stop sound
    play sound "audio/sfx/nr1.wav" noloop
    nr "\[Whale sounds\]"
    stop sound
    
    hide char nr
    jump break_cont    

################################################################################
label break_cont:
    hide char
    jump lunch