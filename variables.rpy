init:
    
    #chara positions
    $ leftPos = Position(xpos=50, xanchor=50, ypos=1.0, yanchor=1.0)
    $ rightPos = Position(xpos=0.98, xanchor=0.98, ypos =1.0, yanchor=1.0)
    $ rightPos2 = Position(xpos=0.7, xanchor=0.8, ypos = 1.0, yanchor=1.0)
    $ crightPos = Position (xpos=0.98,xanchor=0.98, ypos=1.8,yanchor=1.8)
    
    #Calendar
    $ currentDate = 31
    $ currentDay = "Mon"
    $ currentMonth = 12
    $ currentTime = "Morning"
    
    screen calendar:
        button:
            background None
            add "misc/calendar_frame.png" xalign 1.005 yalign -0.25
            text ("%d/%d" % (currentMonth,currentDate)) xalign 0.95 yalign 12.5 size 40
            text ("%s" % (currentDay)) xalign 0.99 yalign 3.0 size 30
            text ("%s" % (currentTime)) xalign 0.98 yalign 8.5 size 30
    
    python:
        
        def charComposite(chara, exp, expNo, expNo2, clothes, fade, width, height, st,at):
            
            body = "images/" + chara + "/" + chara + "_" + clothes + ".png"
            arms = "images/" + chara + "/" + chara + "_" + clothes + "_arms.png"
            head1 = "images/" + chara + "/" + chara + "_" + exp + expNo + ".png"
            head2 = "images/" + chara + "/" + chara + "_" + exp + expNo2 + ".png"
            
            if fade == "false":
                lc = LiveComposite(
                    (width,height),
                    (0,0), body,
                    (0,0), arms,
                    (0,0), head(chara, head1, head2)
                    )
            elif fade == "true":
                lc = LiveComposite(
                    (width,height),
                    (0,0), im.MatrixColor(body,im.matrix.brightness(-.25)),
                    (0,0), im.MatrixColor(arms,im.matrix.brightness(-.25)),
                    (0,0), head(chara, im.MatrixColor(head1,im.matrix.brightness(-.25)), im.MatrixColor(head2,im.matrix.brightness(-.25)))
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

image oso = DynamicDisplayable(renpy.curry(charComposite)("oso","neutral","01","02","schools","false",800,950))
image kara = DynamicDisplayable(renpy.curry(charComposite)("kara","neutral","01","02","schools","false",800,950))
image choro = DynamicDisplayable(renpy.curry(charComposite)("choro","neutral","01","02","schools","false",800,950))
image ichi = DynamicDisplayable(renpy.curry(charComposite)("ichi","neutral","01","02","schools","false",800,950))
image jyushi = DynamicDisplayable(renpy.curry(charComposite)("jyushi","neutral","01","02","schools","false",800,950))
image todo = DynamicDisplayable(renpy.curry(charComposite)("todo","neutral","01","02","schools","false",800,950))

image atsushi = DynamicDisplayable(renpy.curry(charComposite)("atsushi","neutral","","","schoolw","false",800,1000))
image chibita = DynamicDisplayable(renpy.curry(charComposite)("chibita","neutral","","","schoolw","false",800,950))
image totoko = DynamicDisplayable(renpy.curry(charComposite)("totoko","neutral","","","schoolw","false",800,950))

image matsuyo = "images/matsuyo/matsuyo_normal.png"
image matsuzo = "images/matsuyo/matsuzo_normal.png"

image npcFemale = "images/npcstudent/npcstudent_fem.png"
image npcMale = "images/npcstudent/npcstudent_male.png"

image kara flip = Transform("kara",xzoom=-1.0)
image oso flip = Transform("oso",xzoom=-1.0)
image choro flip = Transform("choro",xzoom=-1.0)
image ichi flip = Transform("ichi",xzoom=-1.0)
image jyushi flip = Transform("jyushi",xzoom=-1.0)
image todo flip = Transform("todo",xzoom=-1.0)

image atsushi flip = Transform("atsushi",xzoom=-1.0)