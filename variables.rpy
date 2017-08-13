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
            

            def __init__(self,start,child,dist):
                if start is None:
                    start = child.get_placement()
                    
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
        
        def changeDate(newMonth, newDate, newTime):
            global currentDate
            #global currentDay
            global currentMonth 
            global currentTime
            
            currentDate = newDate
            #currentDay = newDay
            currentMonth = newMonth
            currentTime = newTime
        
        ##### CHANGING HYPERLINK STYLE #####
        style.hlStyle = Style(style.say_dialogue)
        style.hlStyle.font = "helsinki.ttf"
        style.hlStyle.size = 36
        style.hlStyle.color = "#58b2ff"
        style.hlStyle.hover_color = "#000000"
        style.hlStyle.underline = False
        
        style.hyperlink_text = style.hlStyle

#a bunch of variables
init:
    
    ##### CHARACTER POSITIONS#####
    
    #default left position 
    $ pos3 = Position(xpos=0.25, xanchor='center', ypos=1.0, yanchor=1.0)
    
    #left position, close to center
    $ pos2 = Position(xpos=0.35, xanchor='center', ypos=1.0, yanchor=1.0)
    
    #left position, far left
    $ pos1 = Position(xpos=0.1, xanchor='center', ypos=1.0, yanchor=1.0)
    
    #default right position
    $ pos6 = Position(xpos=0.75, xanchor='center', ypos =1.0, yanchor=1.0)
    
    #right position, close to center
    $ pos4 = Position(xpos=0.65, xanchor='center', ypos = 1.0, yanchor=1.0)
    
    #right position, far right
    $ pos5 = Position(xpos=0.9, xanchor='center', ypos=1.0, yanchor=1.0)

    #middle
    $ pos7 = Position(xpos=0.5, xanchor='center', ypos=1.0, yanchor=1.0)
    
    #Special Chibita Position
    $ cpos3 = Position(xpos=0.25, xanchor='center', ypos=1.5,yanchor=1.5)
    
    #left position, close to center
    $ cpos2 = Position(xpos=0.35, xanchor='center', ypos=1.5,yanchor=1.5)
    
    #left position, far left
    $ cpos1 = Position(xpos=0.1, xanchor='center', ypos=1.5,yanchor=1.5)
    
    #default right position
    $ cpos6 = Position(xpos=0.75, xanchor='center', ypos=1.5,yanchor=1.5)
    
    #right position, close to center
    $ cpos4 = Position(xpos=0.65, xanchor='center', ypos=1.5,yanchor=1.5)
    
    #right position, far right
    $ cpos5 = Position(xpos=0.9, xanchor='center', ypos=1.5,yanchor=1.5)

    #middle
    $ cpos7 = Position(xpos=0.5, xanchor='center', ypos=1.5,yanchor=1.5)
    
    ##### CALENDAR TEXT STYLES #####
    style calendarDateStyle:
        font "FredokaOne-Regular.ttf"
        color "#FFFFFF"
        size 100
        text_align 1.0
        min_width 200
        outlines [(absolute(5),"#0b1b7a",absolute(0),absolute(0))]
        
    style calendarMonthStyle:
        font "FredokaOne-Regular.ttf"
        color "#FFFFFF"
        size 40
        text_align 0.0
        min_width 200
        outlines [(absolute(4),"#0b1b7a",absolute(0),absolute(0))]
        
    style calendarTimeStyle:
        font "FredokaOne-Regular.ttf"
        color "#FFFFFF"
        size 20
        text_align 0.0
        min_width 200
        outlines [(absolute(4),"#0b1b7a",absolute(0),absolute(0))]
    
    ##### CALENDAR #####
    $ currentDate = 31
    #$ currentDay = "Mon"
    $ currentMonth = "JAN"
    $ currentTime = "AFTER SCHOOL"
    
    $ broPoints = 0
    $ scrShake = Shake((0,0,0,0),1.0,dist=15) # Shake(position,duration,max distance)
    
    screen calendar:
        window:
            background "misc/calendar.png"
            xpos 975 ypos 270
            
            $ displayDate = At(Text("[currentDate]",style="calendarDateStyle"),Transform(rotate=-16))
            $ displayMonth = At(Text("[currentMonth]",style="calendarMonthStyle"),Transform(rotate=-16))
            $ displayTime = At(Text("[currentTime]",style="calendarTimeStyle"),Transform(rotate=-16))
            
            image displayDate xalign 0.899 yalign 0.45
            image displayMonth xalign 1.0 yalign -0.55
            image displayTime xalign 1.005 yalign 0.05
            
            #text ("%d" % (currentDate)) xalign 0.95 yalign 12.5 size 106
            #text ("%s" % (currentMonth)) xalign 0.85 yalign 12.5 size 30
            #text ("%s" % (currentDay)) xalign 0.99 yalign 3.0 size 30
            #text ("%s" % (currentTime)) xalign 0.98 yalign 8.5 size 30

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

define oso = Character("OSOMATSU", color = "#FFFFFF", ctc="ctc_blink",ctc_position="nestled")
define kara = Character("KARAMATSU", color = "#FFFFFF", ctc="ctc_blink",ctc_position="nestled")
define choro = Character("CHOROMATSU", color = "#FFFFFF", ctc="ctc_blink",ctc_position="nestled")
define ichi = Character("ICHIMATSU", color = "#FFFFFF", ctc="ctc_blink",ctc_position="nestled")
define jyushi = Character("JYUSHIMATSU", color = "#FFFFFF", ctc="ctc_blink",ctc_position="nestled")
define todo = Character("TODOMATSU", color = "#FFFFFF", ctc="ctc_blink",ctc_position="nestled")

define matsuyo = Character("MATSUYO", color = "#FFFFFF", ctc="ctc_blink",ctc_position="nestled")
define matsuzo = Character("MATSUZO", color = "#FFFFFF", ctc="ctc_blink",ctc_position="nestled")
define chibita = Character("CHIBITA", color = "#FFFFFF", ctc="ctc_blink",ctc_position="nestled")
define iyami = Character("IYAMI", color = "#FFFFFF", ctc="ctc_blink",ctc_position="nestled")
define totoko = Character("TOTOKO", color = "#FFFFFF", ctc="ctc_blink",ctc_position="nestled")
define atsushi = Character("ATSUSHI", color = "#FFFFFF", ctc="ctc_blink",ctc_position="nestled")
define kaede = Character("KAEDE", color = "#FFFFFF", ctc="ctc_blink",ctc_position="nestled")

define mystery = Character("???", color = "#FFFFFF", ctc="ctc_blink",ctc_position="nestled")
define both = Character("BOTH", color = "#FFFFFF", ctc="ctc_blink",ctc_position="nestled")

define everyone = Character("EVERYONE", color = "#FFFFFF",ctc="ctc_blink",ctc_position="nestled")
define everyoneelse = Character("EVERYONE ELSE", color = "#FFFFFF",ctc="ctc_blink",ctc_position="nestled")
define rest = Character("THE REST", color = "#FFFFFF", ctc="ctc_blink",ctc_position="nestled")
define suuji = Character("ICHIMATSU & JYUSHIMATSU", color = "#FFFFFF", ctc="ctc_blink",ctc_position="nestled")


# for narration
define narrator = Character("", color = "#FFFFFF", ctc="ctc_blink",ctc_position="nestled")
define dev = Character("DEVS", color = "#FFFFFF", ctc="ctc_blink",ctc_position="nestled")

# ticks
image angryTick = "images/ticks/AngrySymbol.png"
image sweatTick = "images/ticks/SweatSymbol.png"

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

image iyami Regular Angry1 = DynamicDisplayable(renpy.curry(charComposite)("iyami","angry","","","regular","",0,"","false",800,1010))
image iyami Regular Angry1 Fade = DynamicDisplayable(renpy.curry(charComposite)("iyami","angry","","","regular","",0,"","true",800,1010))
image iyami Regular Angry1 Flip = Transform("iyami Regular Angry1",xzoom=-1.0)
image iyami Regular Angry1 Fade Flip = Transform("iyami Regular Angry1 Fade",xzoom=-1.0)

image iyami Regular Displeased1 = DynamicDisplayable(renpy.curry(charComposite)("iyami","displeased1","","","regular","",0,"","false",800,1010))
image iyami Regular Displeased1 Fade = DynamicDisplayable(renpy.curry(charComposite)("iyami","displeased1","","","regular","",0,"","true",800,1010))
image iyami Regular Displeased1 Flip = Transform("iyami Regular Displeased1",xzoom=-1.0)
image iyami Regular Displeased1 Fade Flip = Transform("iyami Regular Displeased1 Fade",xzoom=-1.0)

image iyami Regular Happy1 = DynamicDisplayable(renpy.curry(charComposite)("iyami","happy","","","regular","",0,"","false",800,1010))
image iyami Regular Happy1 Fade = DynamicDisplayable(renpy.curry(charComposite)("iyami","happy","","","regular","",0,"","true",800,1010))
image iyami Regular Happy1 Flip = Transform("iyami Regular Happy1",xzoom=-1.0)
image iyami Regular Happy1 Fade Flip = Transform("iyami Regular Happy1 Fade",xzoom=-1.0)

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

image chibita SchoolW Neutral = DynamicDisplayable(renpy.curry(charComposite)("chibita","neutral","","","schoolw","",0,"","false",800,950))
image chibita SchoolW Neutral Fade = DynamicDisplayable(renpy.curry(charComposite)("chibita","neutral","","","schoolw","",0,"","true",800,950))
image chibita SchoolW Neutral Flip = Transform("chibita SchoolW Neutral",xzoom=-1.0)
image chibita SchoolW Neutral Fade Flip = Transform("chibita SchoolW Neutral Fade",xzoom=-1.0)

image chibita SchoolW Displeased1 = DynamicDisplayable(renpy.curry(charComposite)("chibita","displeased1","","","schoolw","",0,"","false",800,950))
image chibita SchoolW Displeased1 Fade = DynamicDisplayable(renpy.curry(charComposite)("chibita","displeased1","","","schoolw","",0,"","true",800,950))

image chibita SchoolW Angry1 = DynamicDisplayable(renpy.curry(charComposite)("chibita","angry1","","","schoolw","",0,"","false",800,950))
image chibita SchoolW Angry1 Fade = DynamicDisplayable(renpy.curry(charComposite)("chibita","angry1","","","schoolw","",0,"","true",800,950))

image chibita SchoolW Displeased2 = DynamicDisplayable(renpy.curry(charComposite)("chibita","displeased2","","","schoolw","",0,"","false",800,950))
image chibita SchoolW Displeased2 Fade = DynamicDisplayable(renpy.curry(charComposite)("chibita","displeased2","","","schoolw","",0,"","true",800,950))

image chibita Naked Neutral = DynamicDisplayable(renpy.curry(charComposite)("chibita","neutral","","","Naked","",0,"","false",800,950))
image chibita Naked Neutral Fade = DynamicDisplayable(renpy.curry(charComposite)("chibita","neutral","","","Naked","",0,"","true",800,950))
image chibita Naked Neutral Flip = Transform("chibita Naked Neutral",xzoom=-1.0)
image chibita Naked Neutral Fade Flip = Transform("chibita Naked Neutral Fade",xzoom=-1.0)

image chibita Naked Displeased1 = DynamicDisplayable(renpy.curry(charComposite)("chibita","displeased1","","","Naked","",0,"","false",800,950))
image chibita Naked Displeased1 Fade = DynamicDisplayable(renpy.curry(charComposite)("chibita","displeased1","","","Naked","",0,"","true",800,950))
image chibita Naked Displeased1 Flip = Transform("chibita Naked Displeased1",xzoom=-1.0)
image chibita Naked Displeased1 Fade Flip = Transform("chibita Naked Displeased1 Fade",xzoom=-1.0)

image chibita Naked Angry1 = DynamicDisplayable(renpy.curry(charComposite)("chibita","angry1","","","Naked","",0,"","false",800,950))
image chibita Naked Angry1 Fade = DynamicDisplayable(renpy.curry(charComposite)("chibita","angry1","","","Naked","",0,"","true",800,950))
image chibita Naked Angry1 Flip = Transform("chibita Naked Angry1",xzoom=-1.0)
image chibita Naked Angry1 Fade Flip = Transform("chibita Naked Angry1 Fade",xzoom=-1.0)

image chibita Naked Displeased2 = DynamicDisplayable(renpy.curry(charComposite)("chibita","displeased2","","","Naked","",0,"","false",800,950))
image chibita Naked Displeased2 Fade = DynamicDisplayable(renpy.curry(charComposite)("chibita","displeased2","","","Naked","",0,"","true",800,950))
image chibita Naked Displeased2 Flip = Transform("chibita Naked Displeased2",xzoom=-1.0)
image chibita Naked Displeased2 Fade Flip = Transform("chibita Naked Displeased2 Fade",xzoom=-1.0)

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