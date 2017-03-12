init python:
    def charcomposite(matsu, express, clothes,st,at):
            lc = LiveComposite(
                (800,950),
                (0, 0), "images/" + matsu + "/"+matsu+"_"+clothes+".png",
                (0, 0), "images/" + matsu + "/head/"+matsu+"_"+express+"01.png",
                (0, 0), "images/" + matsu + "/"+matsu+"_"+clothes+"_arms.png",
                (0, 0), blinkBitch(name=matsu+"_"+express),
                )
            return lc, None

init:
    $ left = Position(xpos=0.0, xanchor='left')
    $ center = Position(xpos=0.5, xanchor='center')
    $ right = Position(xpos=1.0, xanchor='right')
    $ kara_points = 0 #for point system 


#changed the font in gui.rpy
#added a font folder and changed this value
#define gui.text_font = "font/helsinki.ttf"

#expression variables 
$ neutralExp = "neutral"

#image definitions
image kara = im.Flip("images/kara/kara_naked_full.png", horizontal=True)
image dayon = "images/Dayon.png"

image seraOso = DynamicDisplayable(renpy.curry(charcomposite)("oso", "neutral", "sera"))
image seraOso wut = DynamicDisplayable(renpy.curry(charcomposite)("oso", "suprised", "sera"))
image seraOso blank = DynamicDisplayable(renpy.curry(charcomposite)("oso", "blank", "sera"))

# image osoSera = LiveComposite(
#                     (800,950),
#                     (0,0),"images/oso/head/oso_neutral01.png",
#                     (0,0),"images/oso/oso_sera.png",
#                     (0,0),"images/oso/oso_sera_arms.png",
#                     (0,0),"osoheadblink",
#                     )


#backgrounds
image bg_outside = "images/bg/outside.jpg"
image bg_fish = "images/bg/fish.jpg"
image classroom = "images/bg/classroom1a.jpg"

#define roles
define o = Character("Osomatsu", color="#f7030e")
define k = Character("Karamatsu",color="#2b90f5")

#define extra
define slowDissolve = Dissolve(1.0)

#blinking animation
# image osoheadblink:
#    "images/oso/head/oso_neutral01.png"
#    choice:
#        4.5
#    choice:
#        3.5
#    choice:
#        1.5
#    "images/oso/head/oso_neutral02.png"
#    .25
#    repeat

#blinking animation with variables
transform blinkBitch(name=""):
    "images/oso/head/{0}01.png".format(name)
    choice:
        2.5
    choice:
        1.5
    choice:
        0.5
    "images/oso/head/{0}02.png".format(name)
    .25
    repeat
