init:
 python:

    import math
    
    def charcomposite(matsu, express, clothes,st,at):
            lc = LiveComposite(
                (800,950),
                (0, 0), "images/" + matsu + "/"+matsu+"_"+clothes+".png",
                (0, 0), "images/" + matsu + "/head/"+matsu+"_"+express+"01.png",
                (0, 0), "images/" + matsu + "/"+matsu+"_"+clothes+"_arms.png",
                (0, 0), blinkBitch(name=matsu+"_"+express),
                )
            return lc, None

    class Shaker(object):
        
            anchors = {
                'top' : 0.0,
                'center' : 0.5,
                'bottom' : 1.0,
                'left' : 0.0,
                'right' : 1.0,
                }
        
            def __init__(self, start, child, dist):
                if start is None:
                    start = child.get_placement()
                #
                self.start = [ self.anchors.get(i, i) for i in start ]  # central position
                self.dist = dist    # maximum distance, in pixels, from the starting point
                self.child = child
                
            def __call__(self, t, sizes):
                # Float to integer... turns floating point numbers to
                # integers.                
                def fti(x, r):
                    if x is None:
                        x = 0
                    if isinstance(x, float):
                        return int(x * r)
                    else:
                        return x

                xpos, ypos, xanchor, yanchor = [ fti(a, b) for a, b in zip(self.start, sizes) ]

                xpos = xpos - xanchor
                ypos = ypos - yanchor
                
                nx = xpos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
                ny = ypos + (1.0-t) * self.dist * (renpy.random.random()*2-1)

                return (int(nx), int(ny), 0, 0)

    def _Shake(start, time, child=None, dist=100.0, **properties):

            move = Shaker(start, child, dist=dist)

            return renpy.display.layout.Motion(move,time,child,add_sizes=True,**properties)

    Shake = renpy.curry(_Shake)
           
    #

#

init:
    $ left = Position(xpos=0.0, xanchor='left')
    $ center = Position(xpos=0.5, xanchor='center')
    $ right = Position(xpos=1.0, xanchor='right')
    $ kara_points = 0 #for point system 
    $ scrshake = Shake((0, 0, 0, 0), 1.0, dist=15) # Shake(position, duration, maximum distance)
    $ tremble = Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=5) 


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
