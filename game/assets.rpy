image movie = Movie(size=(800, 600), xpos=0, ypos=0, xanchor=0, yanchor=0)

# Character types
define tc = Character("J2-sensei")
define my = Character("???")
define bs = Character("Beluga-senpai")
define bb = Character("Big Blue")
define mc = DynamicCharacter("mc_name")
define nr = Character("Nurse")
define fk = Character("Kira-chan")

# Disclaimer/Intro/Credits images
image ship        = "ship.png"
image disclaimer  = "disclaimer.png"
image intro       = "intro.png"
image bg home     = "IntroScene.jpg"
image credit text = "credits.png"

# Character images
image char bb angry       = "bb_angry.png"
image char bb disapproval = "bb_disapproval.png"
image char bb excited     = "bb_excited.png"
image char bb happy       = "bb_happy.png"
image char bb joking      = "bb_joking.png"
image char bb love        = "bb_love.png"
image char bb neutral     = "bb_neutral.png"
image char bb panic       = "bb_panic.png"
image char bb sad         = "bb_sad.png"
image char bb scared      = "bb_scared.png"
image char bb thinking    = "bb_think.png"

image char bs angry       = "bs_angry.png"
image char bs blush       = "bs_tsundere.png"
image char bs disapproval = "bs_disapproval.png"
image char bs excited     = "bs_excited.png"
image char bs happy       = "bs_happy.png"
image char bs joking      = "bs_joking.png"
image char bs neutral     = "bs_neutral.png"
image char bs panic       = "bs_panic.png"
image char bs sad         = "bs_sad.png"
image char bs thinking    = "bs_think.png"

image char fk angry       = "fk_angry.png"
image char fk disapproval = "fk_disapproval.png"
image char fk excited     = "fk_excited.png"
image char fk happy       = "fk_happy.png"
image char fk joking      = "fk_joking.png"
image char fk love        = "fk_love.png"
image char fk neutral     = "fk_neutral.png"
image char fk panic       = "fk_panic.png"
image char fk sad         = "fk_sad.png"
image char fk scared      = "fk_scared.png"
image char fk thinking    = "fk_think.png"

image char tc = "sensei.png"
image char tc flip = im.Flip("sensei.png", horizontal=True)
image char nr = "nurse.png"

# Time cards
# THANKS THRYN FOR THE NAMING CONVENTION!
image hours 10 = "title ten.jpg"
image hours 9  = "title nine.jpg"
image hours 8  = "title eight.jpg"
image hours 7  = "title seven.jpg"
image hours 6  = "title six.jpg"
image hours 5  = "title five.jpg"
image hours 4  = "title four.jpg"
image hours 3  = "title three.jpg"
image hours 2  = "title two.jpg"
image hours 1  = "title one.jpg"

# End cards
image end bad          = "end bad.png"
image end bedder       = "end bedder.png"
image end beluga       = "end beluga.png"
image end bad beluga   = "end bad beluga.png"
image end big blue     = "end big blue.png"
image end bad big blue = "end bad big blue.png"
image end kira         = "end kira.png"
image end bad kira     = "end bad kira.png"

# Transforms
transform slowmovein:
    xanchor 0.0 yanchor 0.0 ypos 0.0 xpos 0.65
    linear 20.0 xpos 0.0

transform slowmoveout:
    xanchor 0.0 yanchor 0.0 ypos 0.0 xpos 0.0
    linear 10.0 xpos 0.65
    
transform creditspan:
    xanchor 0.0 yanchor 0.0 ypos 1.0 xpos 0.0
    linear 20.0 ypos -1.2

