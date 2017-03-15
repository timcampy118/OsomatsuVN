init:
    
    #chara positions
    $ leftPos = Position(xpos=50, xanchor=50, ypos=1.0, yanchor=1.0)
    $ rightPos = Position(xpos=0.98, xanchor=0.98, ypos =1.0, yanchor=1.0)
    $ rightPos2 = Position(xpos=0.7, xanchor=0.8, ypos = 1.0, yanchor=1.0)
    
    #various expressions
    $ angry1 = "angry1"
    $ angry2 = "angry2"
    $ neutral = "neutral"
    $ blank = "blank"
    $ dark = "dark"
    $ displeased1 = "displeased1"
    $ displeased2 = "displeased2"
    $ happy1 = "happy1"
    $ happy2 = "happy2"
    $ shocked = "shocked"
    $ surprised = "surprised"
    
    #various clothes
    $ school = "school"
    $ naked = "naked"
    $ sera = "sera"
    
    #various clothes FADED
    
    #to fade
    $ fade = "F"
    $ darkenTrue = "darkenTrue"
    $ darkenFalse = "darkenFalse"
    
    #vars to change face/clothes
    $ osoExp = neutral
    $ karaExp = neutral
    $ choroExp = neutral
    $ osoClothes = naked
    $ karaClothes = naked
    $ choroClothes = naked
    
    #characters
    $ oso = "oso"
    $ kara = "kara"
    $ choro = "choro"
    
    #functions
    python:
        
        #call this at the beginning of each scene unless the character changes clothes/expression
        #then call it again to save
        def saveChara(chara):
            
            #so variables are accessible
            global currentOsoExp
            global currentOsoClothes
            global currentKaraExp
            global currentKaraClothes
            global currentChoroExp
            global currentChoroClothes
            
            if chara == oso:
                currentOsoExp = osoExp
                currentOsoClothes = osoClothes
            elif chara == kara:
                currentKaraExp = karaExp
                currentKaraClothes = karaClothes
            elif chara == choro:
                currentChoroExp = choroExp
                currentChoroClothes = choroClothes
        
        #to darken or lighten characters in convos
        #you'll need to call it again when you change expression while chara is still faded
        #chara = name of chara, darken = darkenTrue or darkenFalse
        def darkenChara(chara,darken):
            
            global osoExp
            global karaExp
            global choroExp
            global osoClothes
            global karaClothes
            global choroClothes
            
            #to darken
            if darken == darkenTrue:
                if chara == oso:
                    osoExp = osoExp + fade
                    osoClothes = osoClothes + fade
                elif chara == kara:
                    karaExp = karaExp + fade
                    karaClothes = karaClothes + fade
                elif chara == choro:
                    choroExp = choroExp + fade
                    choroClothes = choroClothes + fade
            #to lighten
            elif darken == darkenFalse:
                if chara == oso:
                    osoExp = currentOsoExp
                    osoClothes = currentOsoClothes
                elif chara == kara:
                    karaExp = currentKaraExp
                    karaClothes = currentKaraClothes
                elif chara == choro:
                    choroExp = currentChoroExp
                    choroClothes = currentChoroClothes
            

# Choromatsu
image choro head:
    ConditionSwitch(
        "choroExp == neutral", "choro_neutral01.png",
        "choroExp == angry1", "choro_angry01.png",
        "choroExp == dark", "choro_dark.png",
        "choroExp == displeased1", "choro_displeased01.png",
        "choroExp == displeased2", "choro_displeased03.png",
        "choroExp == happy1", "choro_happy01.png",
        "choroExp == happy2", "choro_happy03.png",
        "choroExp == surprise", "choro_surprise01.png",
        "choroExp == 'neutralF'", im.MatrixColor("choro_neutral01.png",im.matrix.brightness(-.25)),
        "choroExp == 'angry1F'", im.MatrixColor("choro_angry01.png",im.matrix.brightness(-.25)),
        "choroExp == 'darkF'", im.MatrixColor("choro_dark.png",im.matrix.brightness(-.25)),
        "choroExp == 'displeased1F'", im.MatrixColor("choro_displeased01.png",im.matrix.brightness(-.25)),
        "choroExp == 'displeased2F'", im.MatrixColor("choro_displeased03.png",im.matrix.brightness(-.25)),
        "choroExp == 'happy1F'", im.MatrixColor("choro_happy01.png",im.matrix.brightness(-.25)),
        "choroExp == 'happy2F'", im.MatrixColor("choro_happy03.png",im.matrix.brightness(-.25)),
        "choroExp == 'surpriseF'", im.MatrixColor("choro_surprise01.png",im.matrix.brightness(-.25))
    )
    choice:
        3
    choice:
        2.5
    choice:
        1.5
    ConditionSwitch(
        "choroExp == neutral", "choro_neutral02.png",
        "choroExp == angry1", "choro_angry02.png",
        "choroExp == dark", "choro_dark.png",
        "choroExp == displeased1", "choro_displeased02.png",
        "choroExp == displeased2", "choro_displeased04.png",
        "choroExp == happy1", "choro_happy02.png",
        "choroExp == happy2", "choro_happy04.png",
        "choroExp == surprise", "choro_surprise02.png",
        "choroExp == 'neutralF'", im.MatrixColor("choro_neutral02.png",im.matrix.brightness(-.25)),
        "choroExp == 'angry1F'", im.MatrixColor("choro_angry02.png",im.matrix.brightness(-.25)),
        "choroExp == 'darkF'", im.MatrixColor("choro_dark.png",im.matrix.brightness(-.25)),
        "choroExp == 'displeased1F'", im.MatrixColor("choro_displeased02.png",im.matrix.brightness(-.25)),
        "choroExp == 'displeased2F'", im.MatrixColor("choro_displeased04.png",im.matrix.brightness(-.25)),
        "choroExp == 'happy1F'", im.MatrixColor("choro_happy02.png",im.matrix.brightness(-.25)),
        "choroExp == 'happy2F'", im.MatrixColor("choro_happy04.png",im.matrix.brightness(-.25)),
        "choroExp == 'surpriseF'", im.MatrixColor("choro_surprise02.png",im.matrix.brightness(-.25))
    )
    .25
    repeat
    
image choro = LiveComposite(
                    (800,950),
                    (0,0),ConditionSwitch(
                        "choroClothes == school", "choro_schools.png",
                        "choroClothes == naked", "choro_naked.png",
                        "choroClothes == 'schoolF'", im.MatrixColor("choro_schools.png",im.matrix.brightness(-.25)),
                        "choroClothes == 'nakedF'", im.MatrixColor("choro_naked.png",im.matrix.brightness(-.25))
                        ),
                    (0,0),ConditionSwitch(
                        "choroClothes == school", "choro_schools_arms.png",
                        "choroClothes == naked", "choro_schools_arms.png",
                        "choroClothes == 'schoolF'", im.MatrixColor("choro_schools_arms.png",im.matrix.brightness(-.25)),
                        "choroClothes == 'nakedF'", im.MatrixColor("choro_schools_arms.png",im.matrix.brightness(-.25))
                        ),
                    (0,0),"choro head"
                )

# Karamatsu
image kara head:
    ConditionSwitch(
        "karaExp == neutral", "kara_neutral01.png",
        "karaExp == 'neutralF'", im.MatrixColor("kara_neutral01.png",im.matrix.brightness(-.25))
        )
    choice:
        3
    choice:
        2.5
    choice:
        1.5
    ConditionSwitch(
        "karaExp == neutral", "kara_neutral02.png",
        "karaExp == 'neutralF'", im.MatrixColor("kara_neutral02.png",im.matrix.brightness(-.25))
        )
    .25
    repeat

image kara = LiveComposite(
                        (800,950),
                        (0,0),ConditionSwitch(
                            "karaClothes == school", "kara_schools.png",
                            "karaClothes == 'schoolF'", im.MatrixColor("kara_schools.png",im.matrix.brightness(-.25)),
                            "karaClothes == naked", "kara_naked.png",
                            "karaClothes == 'nakedF'", im.MatrixColor("kara_naked.png",im.matrix.brightness(-.25))
                            ),
                        (0,0),ConditionSwitch(
                            "karaClothes == school", "kara_schools_arms.png",
                            "karaClothes == 'schoolF'", im.MatrixColor("kara_schools_arms.png",im.matrix.brightness(-.25)),
                            "karaClothes == naked", "kara_naked_arms.png",
                            "karaClothes == 'nakedF'", im.MatrixColor("kara_naked_arms.png",im.matrix.brightness(-.25))
                            ),
                        (0,0),"kara head"
                    )

# Osomatsu
image oso =  LiveComposite(
                    (800,950),
                    (0,0), ConditionSwitch(
                        "osoClothes == school", "oso_schools.png",
                        "osoClothes == 'schoolF'", im.MatrixColor("oso_schools.png",im.matrix.brightness(-.25)),
                        "osoClothes == naked", "oso_naked.png",
                        "osoClothes == 'nakedF'", im.MatrixColor("oso_naked.png",im.matrix.brightness(-.25)),
                        "osoClothes == sera", "oso_sera.png",
                        "osoClothes == 'seraF'", im.MatrixColor("oso_sera.png",im.matrix.brightness(-.25))
                        ),
                    (0,0),ConditionSwitch(
                        "osoClothes == school", "oso_schools_arms.png",
                        "osoClothes == naked", "oso_naked_arms.png",
                        "osoClothes == sera", "oso_sera_arms.png",
                        "osoClothes == 'schoolF'", im.MatrixColor("oso_schools_arms.png",im.matrix.brightness(-.25)),
                        "osoClothes == 'nakedF'", im.MatrixColor("oso_naked_arms.png",im.matrix.brightness(-.25)),
                        "osoClothes == 'seraF'", im.MatrixColor("oso_sera_arms.png",im.matrix.brightness(-.25))
                        ),
                    (0,0),"oso head"
                    )

image oso head:
    ConditionSwitch(
        "osoExp == neutral", "oso_neutral01.png",
        "osoExp == displeased1", "oso_displeased01.png",
        "osoExp == angry1", "oso_angry01.png",
        "osoExp == angry2", "oso_angry03.png",
        "osoExp == blank", "oso_blank01.png",
        "osoExp == dark", "oso_dark.png",
        "osoExp == happy1", "oso_happy01.png",
        "osoExp == shocked", "oso_shock01.png",
        "osoExp == surprised", "oso_surprised01.png",
        "osoExp == 'neutralF'", im.MatrixColor("oso_neutral01.png",im.matrix.brightness(-.25)),
        "osoExp == 'displeased1F'", im.MatrixColor("oso_displeased01.png",im.matrix.brightness(-.25)),
        "osoExp == 'angry1F'", im.MatrixColor("oso_angry01.png",im.matrix.brightness(-.25)),
        "osoExp == 'angry2F'", im.MatrixColor("oso_angry03.png",im.matrix.brightness(-.25)),
        "osoExp == 'blankF'", im.MatrixColor("oso_blank01.png",im.matrix.brightness(-.25)),
        "osoExp == 'darkF'", im.MatrixColor("oso_dark.png",im.matrix.brightness(-.25)),
        "osoExp == 'happy1F'", im.MatrixColor("oso_happy01.png",im.matrix.brightness(-.25)),
        "osoExp == 'shockedF'", im.MatrixColor("oso_shock01.png",im.matrix.brightness(-.25)),
        "osoExp == 'surprisedF'", im.MatrixColor("oso_surprised01.png",im.matrix.brightness(-.25))
    )
    choice:
        3
    choice:
        2.5
    choice:
        1.5
    ConditionSwitch(
        "osoExp == neutral", "oso_neutral02.png",
        "osoExp == displeased1", "oso_displeased02.png",
        "osoExp == angry1", "oso_angry02.png",
        "osoExp == angry2", "oso_angry04.png",
        "osoExp == blank", "oso_blank02.png",
        "osoExp == dark", "oso_dark.png",
        "osoExp == happy1", "oso_happy02.png",
        "osoExp == shocked", "oso_shock02.png",
        "osoExp == surprised", "oso_surprised02.png",
        "osoExp == 'neutralF'", im.MatrixColor("oso_neutral02.png",im.matrix.brightness(-.25)),
        "osoExp == 'displeased1F'", im.MatrixColor("oso_displeased02.png",im.matrix.brightness(-.25)),
        "osoExp == 'angry1F'", im.MatrixColor("oso_angry02.png",im.matrix.brightness(-.25)),
        "osoExp == 'angry2F'", im.MatrixColor("oso_angry04.png",im.matrix.brightness(-.25)),
        "osoExp == 'blankF'", im.MatrixColor("oso_blank02.png",im.matrix.brightness(-.25)),
        "osoExp == 'darkF'", im.MatrixColor("oso_dark.png",im.matrix.brightness(-.25)),
        "osoExp == 'happy1F'", im.MatrixColor("oso_happy02.png",im.matrix.brightness(-.25)),
        "osoExp == 'shockedF'", im.MatrixColor("oso_shock02.png",im.matrix.brightness(-.25)),
        "osoExp == 'surprisedF'", im.MatrixColor("oso_surprised02.png",im.matrix.brightness(-.25))
    )
    .25
    repeat

# To flip
image oso flip = Transform("oso",xzoom=-1.0)

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define o = Character("Osomatsu", color = "#c20000", who_outlines=[(10,"#0b1b7a"),(5,"#FFFFFF")])
define k = Character("Karamatsu", color = "#2860f0", who_outlines=[(10,"#0b1b7a"),(5,"#FFFFFF")])
define c = Character("Choromatsu", color = "#0fa833", who_outlines=[(10,"#0b1b7a"),(5,"#FFFFFF")])

# Font Style Stuff

style itai_text is text:
    size 80
    font "cac_champagne.ttf"

# The game starts here.

label start:

    # Declare variables
    
    $ karaPoints = 0
    
    # Save the current characters' clothes for fading/unfading purposes
    
    $ saveChara(oso)
    $ saveChara(kara)
    
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg_classroom

    #show oso normal flip at leftPos
    show oso flip at leftPos with dissolve
    
    # These display lines of dialogue.

    o "Hey hey where's everyone...?"
    
    $ darkenChara(oso,darkenTrue)
    
    show kara at rightPos with dissolve
    
    k "You called, brother?"
    
    # Fade Kara, Unfade Oso
    $ darkenChara(oso,darkenFalse)
    $ darkenChara(kara,darkenTrue)
    
    o "Oh you haven't changed either"
    
    $ darkenChara(oso,darkenTrue)
    $ darkenChara(kara,darkenFalse)
    
    k "Yeah"
    
    $ darkenChara(oso,darkenFalse)
    $ darkenChara(kara,darkenTrue)
    
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
    $ osoExp = displeased1
    
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
    
    show kara at rightPos
    
    o "Let's go?"

    k "Let's go"
    
    scene bg_hallway with dissolve 
    
    show oso flip at leftPos
    show kara at rightPos
    
    o "Hrm..."
    
    k "Is that Choromatsu?"
    
    $ osoExp = happy1
    
    o "OI!! CHOROMATSUUUUU!!"
    
    $ choroClothes = school
    $ choroExp = displeased2

    show choro at rightPos2
    
    $ darkenChara(oso)
    $ darkenChara(kara)
    
    c "What is it, Osomatsu..."
    
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
