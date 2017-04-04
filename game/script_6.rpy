################################################################################
label confession:
    call countdown(1)
    play movie "bg corridor.ogv" loop

    mc "There are so many kawaii whales here! But only one can claim my heart"
    "Who should you confess your love to?"
menu:
    "\"Beluga-senpai! Come with me to Jazz club tomorrow!!\"":
        jump confession_beluga
    "\"Big blue! Squeeze me with your muscles and sing me a song!\"":
        jump confession_bigblue
    "\"Kira-chan! Let’s make inarticulate noises at each other!\"":
        jump confession_falsekiller
    "\"I’d rather be alone than with any of these whales!\"":
        jump confession_lonely

################################################################################
label confession_beluga:
    $ success = (sl_beluga > sl_cutoff)
    if success:
        jump confession_beluga_success
    jump confession_beluga_failure

label confession_beluga_success:
    show char bs blush
    bs "I tolerate you so much, %(mc_name)s -chan!! Let’s go listen to Jazz!"
    hide char bs blush
    "You’ve found that special whale for you, under the waves~~~"
    window hide
    show end bedder with dissolve
    with Pause(0.1)
    show end beluga with dissolve
    with Pause(10000000000)
    jump credits

label confession_beluga_failure:
    show char bs angry
    bs "I dislike you even more than most people"
    hide char bs angry
    "You’re going to die sad and alone, under the waves~~~"
    window hide
    show end bad beluga with dissolve
    with Pause(10000000000)
    jump credits

################################################################################
label confession_bigblue:
    $ success = (sl_bigblue > sl_cutoff)
    if success:
        jump confession_bigblue_success
    jump confession_bigblue_failure

label confession_bigblue_success:
    show char bb love
    bb "You have tamed my rebellious heart, %(mc_name)s -chan!!"
    hide char bb love
    "You’ve found that special whale for you, under the waves~~~"
    window hide
    show end bigblue with dissolve
    with Pause(10000000000)
    jump credits

label confession_bigblue_failure:
    show char bb angry
    bb "Go away! Square!"
    hide char bb angry
    "You’re going to die sad and alone, under the waves~~~"
    window hide
    show end bad bigblue with dissolve
    with Pause(10000000000)
    jump credits

################################################################################
label confession_falsekiller:
    $ success = (sl_kira > sl_cutoff)
    if success:
        jump confession_falsekiller_success
    jump confession_falsekiller_failure

label confession_falsekiller_success:
    show char fk love
    fk "%(mc_name)s -chan! I’m not a whale, but I whaley love you!!1!~~~~"
    hide char fk love
    "You’ve found that special whale for you, under the waves~~~"
    window hide
    show end kira with dissolve
    with Pause(10000000000)
    jump credits

label confession_falsekiller_failure:
    show char fk angry
    fk "We are species apart, %(mc_name)s -chan!"
    hide char fk angry
    "You’re going to die sad and alone, under the waves~~~"
    window hide
    show end bad kira with dissolve
    with Pause(10000000000)
    jump credits

################################################################################
label confession_lonely:
    play movie "bg sadalone.ogv" loop

    "You’re going to die sad and alone, under the waves~~~"
    window hide
    show end bad with dissolve
    with Pause(10000000000)
    jump credits
