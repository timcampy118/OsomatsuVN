init:
    $ left = Position(xpos=0.0, xanchor='left')
    $ center = Position(xpos=0.5, xanchor='center')
    $ right = Position(xpos=1.0, xanchor='right')
    $ kara_points = 0 #for point system 


#changed the font in gui.rpy
#added a font folder and changed this value
#define gui.text_font = "font/helsinki.ttf"

#image definitions
image kara = im.Flip("images/kara/kara_naked_full.png", horizontal=True)


image osoSera = LiveComposite(
                    (800,950),
                    (0,0),"images/oso/head/oso_neutral01.png",
                    (0,0),"images/oso/oso_sera.png",
                    (0,0),"images/oso/oso_sera_arms.png",
                    (0,0),"osoheadblink",
                    )

image osoSera angry = LiveComposite(
                    (800,950),
                    (0,0),"images/oso/oso_sera.png",
                    (0,0),"images/oso/head/oso_angry03.png",
                    (0,0),"images/oso/oso_sera_arms.png",
                    )

image osoSera wut = LiveComposite(
                    (800,950),
                    (0,0),"images/oso/oso_sera.png",
                    (0,0),"images/oso/head/oso_suprised01.png",
                    (0,0),"images/oso/oso_sera_arms.png",
                    )


#blinking animation
image osoheadblink:
   "images/oso/head/oso_neutral01.png"
   choice:
       4.5
   choice:
       3.5
   choice:
       1.5
   "images/oso/head/oso_neutral02.png"
   .25
   repeat

#backgrounds
image bg_outside = "images/bg/outside.jpg"
image bg_fish = "images/bg/fish.jpg"
image classroom = "images/bg/classroom1a.jpg"

#define roles
define o = Character("Osomatsu", color="#f7030e")
define k = Character("Karamatsu",color="#2b90f5")