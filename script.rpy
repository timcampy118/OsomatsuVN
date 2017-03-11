init:
    #$ rightosPos = (1,1)
    #$ righttransPos = (0.5,1)
    $ leftPos = Position(xpos=0.15, xanchor=0.15, ypos=1.0, yanchor=1.0)
    $ rightPos = Position(xpos=0.85, xanchor=0.85, ypos =1.0, yanchor=1.0)
    
    #various expressions
    $ angry1 = "angry1"
    $ angry2 = "angry2"
    $ neutral = "neutral"
    $ blank = "blank"
    $ dark = "dark"
    $ displeased = "displeased"
    $ happy = "happy"
    $ shocked = "shocked"
    $ surprised = "surprised"
    
    #various clothes
    $ school = "school"
    $ naked = "naked"
    $ sera = "sera"
    
    #vars to change face/clothes
    $ osoExp = neutral
    $ karaExp = neutral
    $ osoClothes = naked
    $ karaClothes = naked
    
# The script of the game goes in this file.

# Images are declared here

# Original Oso without animation
#image oso normal = "oso_naked.png"
#image oso normal flip = im.Flip("oso_naked.png",horizontal = True)
#image oso faded flip = im.Flip(im.MatrixColor('oso_naked.png',im.matrix.brightness(-.25)), horizontal = True)

#image kara normal = "kara_naked.png"

image kara head:
    ConditionSwitch(
        "karaExp == neutral", "kara_neutral01.png"
        )
    choice:
        3
    choice:
        2.5
    choice:
        1.5
    ConditionSwitch(
        "karaExp == neutral", "kara_neutral02.png"
        )
    .25
    repeat

image kara = LiveComposite(
                        (800,950),
                        (0,0),ConditionSwitch(
                            "karaClothes == school", "kara_schools.png",
                            "karaClothes == naked", "kara_naked.png"
                            ),
                        (0,0),ConditionSwitch(
                            "karaClothes == school", "kara_schools_arms.png",
                            "karaClothes == naked", "kara_naked_arms.png"
                            ),
                        (0,0),"kara head"
                    )

# Oso with animation
image oso = Flatten(
            LiveComposite(
                    (800,950),
                    (0,0), ConditionSwitch(
                        "osoClothes == school", "oso_schools.png",
                        "osoClothes == naked", "oso_naked.png",
                        "osoClothes == sera", "oso_sera.png"
                        ),
                    (0,0),ConditionSwitch(
                        "osoClothes == school", "oso_schools_arms.png",
                        "osoClothes == naked", "oso_naked_arms.png",
                        "osoClothes == sera", "oso_sera_arms.png"
                        ),
                    (0,0),"oso head"
                    )
            )

#To animate eyes
image oso head:
    ConditionSwitch(
        "osoExp == neutral", "oso_neutral01.png",
        "osoExp == displeased", "oso_displeased01.png",
        "osoExp == angry1", "oso_angry01.png",
        "osoExp == angry2", "oso_angry03.png",
        "osoExp == blank", "oso_blank01.png",
        "osoExp == dark", "oso_dark.png",
        "osoExp == happy", "oso_happy01.png",
        "osoExp == shocked", "oso_shocked01.png",
        "osoExp == surprised", "oso_surprised01.png"
    )
    choice:
        3
    choice:
        2.5
    choice:
        1.5
    #Randomnizes time between blinking
    ConditionSwitch(
        "osoExp == neutral", "oso_neutral02.png",
        "osoExp == displeased", "oso_displeased02.png",
        "osoExp == angry1", "oso_angry02.png",
        "osoExp == angry2", "oso_angry04.png",
        "osoExp == blank", "oso_blank02.png",
        "osoExp == dark", "oso_dark.png",
        "osoExp == happy", "oso_happy02.png",
        "osoExp == shocked", "oso_shocked02.png",
        "osoExp == surprised", "oso_surprised02.png"
    )
    .25
    repeat

#old faded code stuff
image oso eyes faded:
    im.MatrixColor("oso_neutral01.png",im.matrix.brightness(-.25))
    choice:
        3
    choice:
        2.5
    choice:
        1.5
    #Randomnizes time between blinking
    im.MatrixColor("oso_neutral02.png",im.matrix.brightness(-.25))
    .25
    repeat

# To flip
image oso flip = Transform("oso",xzoom=-1.0)

# image oso faded flip = Transform("oso faded",xzoom=-1.0)

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define o = Character("Osomatsu", color = "#c20000")
define k = Character("Karamatsu", color = "#2860f0")

# Font Style Stuff

style itai_text is text:
    size 80
    font "cac_champagne.ttf"

# The game starts here.

label start:

    # Declare variables
    
    $ karaPoints = 0
    
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg_classroom

    #show oso normal flip at leftPos
    show oso flip at leftPos with dissolve
    
    # These display lines of dialogue.

    o "Hey hey where's everyone...?"

    #hide oso normal flip
    #show oso faded flip at leftPos
    show kara at rightPos with dissolve
    #show kara naked at Move(rightosPos,righttransPos,1.5, xanchor = "center", yanchor = "bottom")
    
    k "You called, brother?"
    
    o "Oh you haven't changed either"
    
    k "Yeah"
    
    o "Let's go!"
    
    hide kara
    
    o "Hrm... what should I wear...?"
    
    menu:
        "Wear the sailor outfit":
            jump SeraOso
        "Wear your normal uniform":
            jump NormalOso
    
label SeraOso:
    
    $ osoClothes = sera
    $ karaClothes = school
    $ osoExp = displeased
    
    o "T-the skirt's a little shor--"
    
    show kara at rightPos
    $ osoExp = shocked
    
    k "I'm back"
    
    o "I-"
    
    k "UH"
    
    return
    
label NormalOso:
    
    $ osoClothes = school
    $ karaClothes = school
    
    o "Let's go?"
    
    k "Let's go"
    
    return
    
    #label annoyedKara:
    
    #k "I was changing when you called me, Osomatsu."
    
    #k "Give me a sec"
    
    #jump finalComparison
    
    #return

    #label okKara:
        
    #k "I was changing, my dear brother."
    
    #k "For my... {=itai_text}Karamatsu Girls{/style}."
    
    #"You have [karaPoints] support point(s) with Karamatsu."
    
    #jump finalComparison
    
    #return
    
    #label finalComparison:
    
    #if karaPoints > max(jyushiPoints,ichiPoints):
    #    "You are now BFFs with Karamatsu"
        
    #    "{size=+20}SHEEEEEEEHHHH!!!!!!1ONE1!!1{/size}"
    #    return
    #else:
    #    "Karamatsu BAD END"
    #    return

    # This ends the game.

    return
