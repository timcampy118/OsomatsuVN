init:
    
    python:
        
        import math
        
        #for mcshakin magic
        class Shaker(object):
            
            anchors = {
                'top' : 0.0,
                'center' : 0.5,
                'bottom' : 1.0,
                'left' : 0.0,
                'right' : 1.0
                }
            

            ### Plays a sound after each line###
            def character_callback(event, interact=True, **kwargs):
                if(event == "end") and interact:
                    renpy.sound.play("sfx/button_next.ogg")
            
            config.character_callback = character_callback
            
=======

            def __init__(self,start,child,dist):
                if start is None:
                    start = child.get_plcaement()
                    
                self.start = [ self.anchors.get(1,1) for i in start] #central position
                self.dist = dist # maximum distance, in pixel, from the starting point
                self.child = child
                
            def __call__(self, t, sizes):
                # Float to integer, turns floating point numbers to integers
                
                def fti(x,r):
                    if x is None:
                        x = 0
                    if isinstance(x, float):
                        return int(x * r)
                    else:
                        return x
                        
                xpos, ypos, xanchor, yanchor = [ fti(a,b) for a,b in zip( self.start,sizes ) ]
                
                xpos = xpos - xanchor
                ypos = ypos - yanchor
                
                nx = xpos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
                ny = ypos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
                
                return (int(nx), int(ny),0,0)
                
        
        def _Shake(start, time, child=None, dist=100.0, **properties):
            
            move = Shaker(start,child, dist=dist)
            
            return renpy.display.layout.Motion(move,time,child,add_sizes=True,**properties)
            
        Shake = renpy.curry(_Shake)
                
        
        def charComposite(chara, exp, expNo, expNo2, clothes, acc, armPos, armExp, fade, width, height, st,at):
            
            body = "images/" + chara + "/" + chara + "_" + clothes + ".png"
            head1 = "images/" + chara + "/" + chara + "_" + exp + expNo + ".png"
            head2 = "images/" + chara + "/" + chara + "_" + exp + expNo2 + ".png"
            
            #checks position of arms, then assigns them
            if armPos == 1:
                frontArm = "images/" + chara + "/" + chara + "_" + clothes + "_arms" + armExp + ".png"
                backArm = "blank.png"
            elif armPos == 0:
                frontArm = "blank.png"
                backArm = "images/" + chara + "/" + chara + "_" + clothes + "_arms" + armExp + ".png"
            
            #checks if there's an accessory, else just use a blank image
            if acc != "":
                acc = "images/" + chara + "/" + chara + "_" + acc + ".png"
            else:
                acc = "blank.png"
            
            if fade == "false":
                lc = LiveComposite(
                    (width,height),
                    (0,0), body,
                    (0,0), backArm,
                    (0,0), head(chara, head1, head2),
                    (0,0), acc,
                    (0,0), frontArm
                    )
            elif fade == "true":
                lc = LiveComposite(
                    (width,height),
                    (0,0), im.MatrixColor(body,im.matrix.brightness(-.25)),
                    (0,0), im.MatrixColor(backArm,im.matrix.brightness(-.25)),
                    (0,0), head(chara, im.MatrixColor(head1,im.matrix.brightness(-.25)), im.MatrixColor(head2,im.matrix.brightness(-.25))),
                    (0,0), im.MatrixColor(acc, im.matrix.brightness(-.25)),
                    (0,0), im.MatrixColor(frontArm,im.matrix.brightness(-.25))
                    )
            return lc, None
        
        def changeDate(newMonth, newDate, newDay, newTime):
            global currentDate
            global currentDay
            global currentMonth
            global currentTime
            
            currentDate = newDate
            currentDay = newDay
            currentMonth = newMonth
            currentTime = newTime

#a bunch of variables
init:
    
    ##### CHARACTER POSITIONS#####
    
    #default left position 
    $ leftPos = Position(xpos=0.25, xanchor='center', ypos=1.0, yanchor=1.0)
    
    #left position, close to center
    $ leftPos2 = Position(xpos=0.4, xanchor='center', ypos=1.0, yanchor=1.0)
    
    #left position, far left
    $ leftPos3 = Position(xpos=0.1, xanchor='center', ypos=1.0, yanchor=1.0)
    
    #default right position
    $ rightPos = Position(xpos=0.75, xanchor='center', ypos =1.0, yanchor=1.0)
    
    #right position, close to center
    $ rightPos2 = Position(xpos=0.6, xanchor='center', ypos = 1.0, yanchor=1.0)
    
    #right position, far right
    $ rightPos3 = Position(xpos=0.9, xanchor='center', ypos=1.0, yanchor=1.0)
    
    #Special Chibita Position
    $ crightPos = Position (xpos=0.75,xanchor='center', ypos=2.3,yanchor=2.3)
    
    ##### CALENDAR #####
    $ currentDate = 31
    $ currentDay = "Mon"
    $ currentMonth = 12
    $ currentTime = "Morning"
    
    $ broPoints = 0
    $ scrShake = Shake((0,0,0,0),1.0,dist=15) # Shake(position,duration,max distance)
    
    screen calendar:
        button:
            background None
            add "misc/calendar_frame.png" xalign 1.005 yalign -0.25
            text ("%d/%d" % (currentMonth,currentDate)) xalign 0.95 yalign 12.5 size 40
            text ("%s" % (currentDay)) xalign 0.99 yalign 3.0 size 30
            text ("%s" % (currentTime)) xalign 0.98 yalign 8.5 size 30

transform head(chara,head1,head2):
    
    head1
    choice:
        2.5
    choice:
        1.5
    choice:
        1
    head2
    .25
    repeat

##### SPLASH SCREEN #####

image splash = "credit.jpg"

label splashscreen:
    
    #skip is still possible with this
    scene black 
    with Pause(1)

    
    play sound ("sfx/logo_jingle.ogg")
=======


    show splash with dissolve
    with Pause(5)
    
    scene black with dissolve
    with Pause(1)
    
    ### NEW CODE AKA NO SKIP ###
    ### Uncomment on release ###
    
    #scene black 
    #show splash with dissolve
    #$ renpy.pause(5.0, hard=True)
    
    #scene black with dissolve
    #with Pause(1)
    #return

    return

###### LAND OF NO RETURN ######
##### Uncomment on release ####

#label no_return:
        #$ renpy.block_rollback()
        #"You made your decision already."


##### CLICK TO CONTINUE ######
###### A blinking arrow ######

image ctc_blink:
    "gui/arrow.png"
    linear 0.5 alpha 1.0
    "gui/arrow_blank.png"
    linear 0.5 alpha 1.0
    repeat

# Declare characters

define oso = Character("Osomatsu", color = "#273ce0", who_outlines=[(10,"#0b1b7a"),(5,"#FFFFFF")], ctc="ctc_blink",ctc_position="nestled")
define kara = Character("Karamatsu", color = "#273ce0", who_outlines=[(10,"#0b1b7a"),(5,"#FFFFFF")], ctc="ctc_blink",ctc_position="nestled")
define choro = Character("Choromatsu", color = "#273ce0", who_outlines=[(10,"#0b1b7a"),(5,"#FFFFFF")], ctc="ctc_blink",ctc_position="nestled")
define ichi = Character("Ichimatsu", color = "#273ce0", who_outlines=[(10,"#0b1b7a"),(5,"#FFFFFF")], ctc="ctc_blink",ctc_position="nestled")
define jyushi = Character("Jyushimatsu", color = "#273ce0", who_outlines=[(10,"#0b1b7a"),(5,"#FFFFFF")], ctc="ctc_blink",ctc_position="nestled")
define todo = Character("Todomatsu", color = "#273ce0", who_outlines=[(10,"#0b1b7a"),(5,"#FFFFFF")], ctc="ctc_blink",ctc_position="nestled")

define matsuyo = Character("Matsuyo", color = "#273ce0", who_outlines=[(10,"#0b1b7a"),(5,"#FFFFFF")], ctc="ctc_blink",ctc_position="nestled")
define matsuzo = Character("Matsuyo", color = "#273ce0", who_outlines=[(10,"#0b1b7a"),(5,"#FFFFFF")], ctc="ctc_blink",ctc_position="nestled")
define chibita = Character("Chibita", color = "#273ce0", who_outlines=[(10,"#0b1b7a"),(5,"#FFFFFF")], ctc="ctc_blink",ctc_position="nestled")
define iyami = Character("Iyami", color = "#273ce0", who_outlines=[(10,"#0b1b7a"),(5,"#FFFFFF")], ctc="ctc_blink",ctc_position="nestled")
define totoko = Character("Totoko", color = "#273ce0", who_outlines=[(10,"#0b1b7a"),(5,"#FFFFFF")], ctc="ctc_blink",ctc_position="nestled")
define atsushi = Character("Atsushi", color = "#273ce0", who_outlines=[(10,"#0b1b7a"),(5,"#FFFFFF")], ctc="ctc_blink",ctc_position="nestled")
define kaede = Character("Kaede", color = "#273ce0", who_outlines=[(10,"#0b1b7a"),(5,"#FFFFFF")], ctc="ctc_blink",ctc_position="nestled")

define mystery = Character("???", color = "#273ce0", who_outlines=[(10,"#0b1b7a"),(5,"#FFFFFF")], ctc="ctc_blink",ctc_position="nestled")

define everyone = Character("Everyone", color = "#273ce0", who_outlines=[(10,"#0b1b7a"),(5,"#FFFFFF")], ctc="ctc_blink",ctc_position="nestled")
define rest = Character("The Rest", color = "#273ce0", who_outlines=[(10,"#0b1b7a"),(5,"#FFFFFF")], ctc="ctc_blink",ctc_position="nestled")

# Declare characters

define oso = Character("Osomatsu", color = "#273ce0", who_outlines=[(10,"#0b1b7a"),(5,"#FFFFFF")])
define kara = Character("Karamatsu", color = "#273ce0", who_outlines=[(10,"#0b1b7a"),(5,"#FFFFFF")])
define choro = Character("Choromatsu", color = "#273ce0", who_outlines=[(10,"#0b1b7a"),(5,"#FFFFFF")])
define ichi = Character("Ichimatsu", color = "#273ce0", who_outlines=[(10,"#0b1b7a"),(5,"#FFFFFF")])
define jyushi = Character("Jyushimatsu", color = "#273ce0", who_outlines=[(10,"#0b1b7a"),(5,"#FFFFFF")])
define todo = Character("Todomatsu", color = "#273ce0", who_outlines=[(10,"#0b1b7a"),(5,"#FFFFFF")])

define matsuyo = Character("Matsuyo", color = "#273ce0", who_outlines=[(10,"#0b1b7a"),(5,"#FFFFFF")])
define matsuzo = Character("Matsuyo", color = "#273ce0", who_outlines=[(10,"#0b1b7a"),(5,"#FFFFFF")])
define chibita = Character("Chibita", color = "#273ce0", who_outlines=[(10,"#0b1b7a"),(5,"#FFFFFF")])
define iyami = Character("Iyami", color = "#273ce0", who_outlines=[(10,"#0b1b7a"),(5,"#FFFFFF")])
define totoko = Character("Totoko", color = "#273ce0", who_outlines=[(10,"#0b1b7a"),(5,"#FFFFFF")])
define atsushi = Character("Atsushi", color = "#273ce0", who_outlines=[(10,"#0b1b7a"),(5,"#FFFFFF")])
define kaede = Character("Kaede", color = "#273ce0", who_outlines=[(10,"#0b1b7a"),(5,"#FFFFFF")])

define mystery = Character("???", color = "#273ce0", who_outlines=[(10,"#0b1b7a"),(5,"#FFFFFF")])

define everyone = Character("Everyone", color = "#273ce0", who_outlines=[(10,"#0b1b7a"),(5,"#FFFFFF")])
define rest = Character("The Rest", color = "#273ce0", who_outlines=[(10,"#0b1b7a"),(5,"#FFFFFF")])


# for narration
define narrator = Character("")
    
# character sprites

###### ATSUSHI ######
image atsushi Neutral = DynamicDisplayable(renpy.curry(charComposite)("atsushi","neutral","","","schoolw","",0,"","false",800,1000))
image atsushi Neutral Fade = DynamicDisplayable(renpy.curry(charComposite)("atsushi","neutral","","","schoolw","",0,"","true",800,1000))
image atsushi Neutral Flip = Transform("atsushi Neutral",xzoom=-1.0)
image atsushi Neutral Fade Flip = Transform("atsushi Neutral Fade",xzoom=-1.0)

image atsushi Blank = DynamicDisplayable(renpy.curry(charComposite)("atsushi","blank","01","01","schoolw","",0,"","false",800,1000))
image atsushi Blank Fade = DynamicDisplayable(renpy.curry(charComposite)("atsushi","blank","01","01","schoolw","",0,"","true",800,1000))
image atsushi Blank Flip = Transform("atsushi Blank",xzoom=-1.0)
image atsushi Blank Fade Flip = Transform("atsushi Blank Fade",xzoom=-1.0)

image atsushi Happy = DynamicDisplayable(renpy.curry(charComposite)("atsushi","happy","01","01","schoolw","",0,"","false",800,1000))
image atsushi Happy Fade = DynamicDisplayable(renpy.curry(charComposite)("atsushi","happy","01","01","schoolw","",0,"","true",800,1000))
image atsushi Happy Flip = Transform("atsushi Happy",xzoom=-1.0)
image atsushi Happy Fade Flip = Transform("atsushi Happy Fade",xzoom=-1.0)

image atsushi Surprised = DynamicDisplayable(renpy.curry(charComposite)("atsushi","surprised","01","01","schoolw","",0,"","false",800,1000))
image atsushi Surprised Fade = DynamicDisplayable(renpy.curry(charComposite)("atsushi","surprised","01","01","schoolw","",0,"","true",800,1000))
image atsushi Surprised Flip = Transform("atsushi Surprised",xzoom=-1.0)
image atsushi Surprised Fade Flip = Transform("atsushi Surprised Fade",xzoom=-1.0)

###### IYAMI ######

image iyami Regular Neutral = DynamicDisplayable(renpy.curry(charComposite)("iyami","neutral","","","regular","",0,"","false",800,1010))
image iyami Regular Neutral Fade = DynamicDisplayable(renpy.curry(charComposite)("iyami","neutral","","","regular","",0,"","true",800,1010))
image iyami Regular Neutral Flip = Transform("iyami Regular Neutral",xzoom=-1.0)
image iyami Regular Neutral Fade Flip = Transform("iyami Regular Neutral Fade",xzoom=-1.0)

image iyami Regular Angry = DynamicDisplayable(renpy.curry(charComposite)("iyami","angry","","","regular","",0,"","false",800,1010))
image iyami Regular Angry Fade = DynamicDisplayable(renpy.curry(charComposite)("iyami","angry","","","regular","",0,"","true",800,1010))
image iyami Regular Angry Flip = Transform("iyami Regular Angry",xzoom=-1.0)
image iyami Regular Angry Fade Flip = Transform("iyami Regular Angry Fade",xzoom=-1.0)

image iyami Regular Frown = DynamicDisplayable(renpy.curry(charComposite)("iyami","frown","","","regular","",0,"","false",800,1010))
image iyami Regular Frown Fade = DynamicDisplayable(renpy.curry(charComposite)("iyami","frown","","","regular","",0,"","true",800,1010))
image iyami Regular Frown Flip = Transform("iyami Regular Frown",xzoom=-1.0)
image iyami Regular Frown Fade Flip = Transform("iyami Regular Frown Fade",xzoom=-1.0)

image iyami Regular Happy = DynamicDisplayable(renpy.curry(charComposite)("iyami","happy","","","regular","",0,"","false",800,1010))
image iyami Regular Happy Fade = DynamicDisplayable(renpy.curry(charComposite)("iyami","happy","","","regular","",0,"","true",800,1010))
image iyami Regular Happy Flip = Transform("iyami Regular Happy",xzoom=-1.0)
image iyami Regular Happy Fade Flip = Transform("iyami Regular Happy Fade",xzoom=-1.0)

image iyami Work Neutral = DynamicDisplayable(renpy.curry(charComposite)("iyami","neutral","","","work","work_hat",0,"","false",800,1010))
image iyami Work Neutral Fade = DynamicDisplayable(renpy.curry(charComposite)("iyami","neutral","","","work","work_hat",0,"","true",800,1010))
image iyami Work Neutral Flip = Transform("iyami Work Neutral",xzoom=-1.0)
image iyami Work Neutral Fade Flip = Transform("iyami Work Neutral Fade",xzoom=-1.0)

image iyami Work Angry = DynamicDisplayable(renpy.curry(charComposite)("iyami","angry","","","work","work_hat",0,"","false",800,1010))
image iyami Work Angry Fade = DynamicDisplayable(renpy.curry(charComposite)("iyami","angry","","","work","work_hat",0,"","true",800,1010))
image iyami Work Angry Flip = Transform("iyami Work Angry",xzoom=-1.0)
image iyami Work Angry Fade Flip = Transform("iyami Work Angry Fade",xzoom=-1.0)

image iyami Work Frown = DynamicDisplayable(renpy.curry(charComposite)("iyami","frown","","","work","work_hat",0,"","false",800,1010))
image iyami Work Frown Fade = DynamicDisplayable(renpy.curry(charComposite)("iyami","frown","","","work","work_hat",0,"","true",800,1010))
image iyami Work Frown Flip = Transform("iyami Work Frown",xzoom=-1.0)
image iyami Work Frown Fade Flip = Transform("iyami Work Frown Fade",xzoom=-1.0)

image iyami Work Happy = DynamicDisplayable(renpy.curry(charComposite)("iyami","happy","","","work","work_hat",0,"","false",800,1010))
image iyami Work Happy Fade = DynamicDisplayable(renpy.curry(charComposite)("iyami","happy","","","work","work_hat",0,"","true",800,1010))
image iyami Work Happy Flip = Transform("iyami Work Happy",xzoom=-1.0)
image iyami Work Happy Fade Flip = Transform("iyami Work Happy Fade",xzoom=-1.0)

##### CHIBITA #####

image chibita Neutral = DynamicDisplayable(renpy.curry(charComposite)("chibita","neutral","","","schoolw","",0,"","false",800,950))
image chibita Neutral Fade = DynamicDisplayable(renpy.curry(charComposite)("chibita","neutral","","","schoolw","",0,"","true",800,950))

image chibita Displeased = DynamicDisplayable(renpy.curry(charComposite)("chibita","displeased","","","schoolw","",0,"","false",800,950))
image chibita Displeased Fade = DynamicDisplayable(renpy.curry(charComposite)("chibita","displeased","","","schoolw","",0,"","true",800,950))

image chibita Angry = DynamicDisplayable(renpy.curry(charComposite)("chibita","angry","","","schoolw","",0,"","false",800,950))
image chibita Angry Fade = DynamicDisplayable(renpy.curry(charComposite)("chibita","angry","","","schoolw","",0,"","true",800,950))

image chibita Frown = DynamicDisplayable(renpy.curry(charComposite)("chibita","frown","","","schoolw","",0,"","false",800,950))
image chibita Frown Fade = DynamicDisplayable(renpy.curry(charComposite)("chibita","frown","","","schoolw","",0,"","true",800,950))

##### TOTOKO #####

image totoko = DynamicDisplayable(renpy.curry(charComposite)("totoko","neutral","","","schoolw","",0,"","false",800,950))
image totoko Fade = DynamicDisplayable(renpy.curry(charComposite)("totoko","neutral","","","schoolw","",0,"","true",800,950))

##### MATSUYO #####

image matsuyo Neutral = DynamicDisplayable(renpy.curry(charComposite)("matsuyo","neutral","","","regular","",0,"","false",800,1000))
image matsuyo Neutral Fade = DynamicDisplayable(renpy.curry(charComposite)("matsuyo","neutral","","","regular","",0,"","true",800,1000))
image matsuyo Neutral Flip = Transform("matsuyo Neutral",xzoom=-1.0)
image matsuyo Neutral Fade Flip = Transform ("matsuyo Neutral Fade",xzoom=-1.0)

image matsuyo Mad = DynamicDisplayable(renpy.curry(charComposite)("matsuyo","mad","","","regular","",0,"","false",800,1000))
image matsuyo Mad Fade = DynamicDisplayable(renpy.curry(charComposite)("matsuyo","mad","","","regular","",0,"","true",800,1000))
image matsuyo Mad Flip = Transform("matsuyo Mad",xzoom=-1.0)
image matsuyo Mad Fade Flip = Transform ("matsuyo Mad Fade",xzoom=-1.0)

image matsuyo Blank = DynamicDisplayable(renpy.curry(charComposite)("matsuyo","blank","01","01","regular","",0,"","false",800,1000))
image matsuyo Blank Fade = DynamicDisplayable(renpy.curry(charComposite)("matsuyo","blank","01","01","regular","",0,"","true",800,1000))
image matsuyo Blank Flip = Transform("matsuyo Blank",xzoom=-1.0)
image matsuyo Blank Fade Flip = Transform ("matsuyo Blank Fade",xzoom=-1.0)

image matsuyo Displeased = DynamicDisplayable(renpy.curry(charComposite)("matsuyo","displeased","01","01","regular","",0,"","false",800,1000))
image matsuyo Displeased Fade = DynamicDisplayable(renpy.curry(charComposite)("matsuyo","displeased","01","01","regular","",0,"","true",800,1000))
image matsuyo Displeased Flip = Transform("matsuyo Displeased",xzoom=-1.0)
image matsuyo Displeased Fade Flip = Transform ("matsuyo Displeased Fade",xzoom=-1.0)

image matsuyo Happy = DynamicDisplayable(renpy.curry(charComposite)("matsuyo","happy","01","01","regular","",0,"","false",800,1000))
image matsuyo Happy Fade = DynamicDisplayable(renpy.curry(charComposite)("matsuyo","happy","01","01","regular","",0,"","true",800,1000))
image matsuyo Happy Flip = Transform("matsuyo Happy",xzoom=-1.0)
image matsuyo Happy Fade Flip = Transform ("matsuyo Happy Fade",xzoom=-1.0)

image matsuyo Surprised = DynamicDisplayable(renpy.curry(charComposite)("matsuyo","surprised","01","01","regular","",0,"","false",800,1000))
image matsuyo Surprised Fade = DynamicDisplayable(renpy.curry(charComposite)("matsuyo","surprised","01","01","regular","",0,"","true",800,1000))
image matsuyo Surprised Flip = Transform("matsuyo Happy",xzoom=-1.0)
image matsuyo Surprised Fade Flip = Transform ("matsuyo Happy Fade",xzoom=-1.0)

##### MATUSZO #####

image matsuzo Neutral = DynamicDisplayable(renpy.curry(charComposite)("matsuzo","neutral","","","regular","",0,"","false",800,1000))
image matsuzo Neutral Fade = DynamicDisplayable(renpy.curry(charComposite)("matsuzo","neutral","","","regular","",0,"","true",800,1000))
image matsuzo Neutral Flip = Transform("matsuzo Neutral",xzoom=-1.0)
image matsuzo Neutral Fade Flip = Transform ("matsuzo Neutral Fade",xzoom=-1.0)

image matsuzo Stunned = DynamicDisplayable(renpy.curry(charComposite)("matsuzo","stunned","","","regular","",0,"","false",800,1000))
image matsuzo Stunned Fade = DynamicDisplayable(renpy.curry(charComposite)("matsuzo","stunned","","","regular","",0,"","true",800,1000))
image matsuzo Stunned Flip = Transform("matsuzo Stunned",xzoom=-1.0)
image matsuzo Stunned Fade Flip = Transform ("matsuzo Stunned Fade",xzoom=-1.0)

##### NPC FEMALE #####

image npcFemale = "images/npcstudent/npcstudent_fem.png"
image npcFemale Fade = im.MatrixColor("images/npcstudent/npcstudent_fem.png",im.matrix.brightness(-.25))
image npcMale = "images/npcstudent/npcstudent_male.png"