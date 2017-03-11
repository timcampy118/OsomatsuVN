# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define o = Character("Osomatsu")
define i = Character("Ichimatsu")
define c = Character ("Choromatsu")

#Declaring Variable for background
image bgClassroom = ('classroom1a.jpg')
image bgHallway = ('hallway1a.jpg')

#Declaring Variables for Oso
image osoBodySchool=('oso_schools.png')
image osoArmSchool = ('oso_schools_arms.png')

image osoHeadAngry:
    "oso_angry04.png"
    choice:
        3
    choice:
        2.5
    choice:
        1.5
    #Randomnizes time between blinking
    "oso_angry03.png"
    .25
    repeat
    
image osoHeadHappy:
    "oso_happy01.png"
    choice:
        3
    choice:
        2.5
    choice:
        1.5
    #Randomnizes time between blinking
    "oso_happy02.png"
    .25
    repeat


#Declaring Variables for ichi

image ichiBodySchool = ('ichi_schools.png')
image ichiArmSchool = ('ichi_schools_arms.png')
image ichiHeadNorm:
    "ichi_neutral01.png"
    choice:
        3
    choice:
        2.5
    choice:
        1.5
    #Randomnizes time between blinking
    "ichi_neutral02.png"
    .25
    repeat
    
#Declaring Variables for choro
    
image choroBodySchool = ('choro_schools.png')
image choroArmSchool = ('choro_schools_arms.png')
image choroHeadNorm:
    "choro_neutral01.png"
    choice:
        3
    choice:
        2.5
    choice:
        1.5
    #Randomnizes time between blinking
    "choro_neutral02.png"
    .25
    repeat



#function to rotate left
init python:
    def transformLeft(t, st, at):
            t.xzoom=-1.0
            t.xpos=-0.
            t.ypos=0.12
            
        
            return 9999999
            
            
#function to rotate right        
    def transformRight(t, st, at):
            t.xzoom=1.0
            t.xpos=0.65
            t.ypos=0.12
            
            return 9999999

#ignore function
    def tintDark(st, at):
            im.matrix.desaturate()
            
            return 999999

            
            #0.65,0.12 Right Side
            #0.0,0.12 Left Side
      
    
    

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bgClassroom

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show osoArmSchool at Transform(function=transformRight) 
    show osoHeadHappy at Transform(function=transformRight) behind osoArmSchool 
    show osoBodySchool at Transform(function=transformRight) behind osoHeadHappy 
    
    show choroArmSchool at Transform(function=transformLeft) 
    show choroHeadNorm at Transform(function=transformLeft) behind choroArmSchool 
    show choroBodySchool at Transform(function=transformLeft) behind choroHeadNorm 
    
   
    

    # These display lines of dialogue.

    o "Hi I'm an asshole"

    c "yes you are"
    
    "Osomatsu reaches out to stroke choro's hand in a creepy manner, choro smacks him"
    
    hide osoHeadHappy
    show osoHeadAngry at Transform(function=transformRight) behind osoArmSchool 

    o "Ow! What was that for?"

    c "Because you're you"

    "Osomatsu runs out the classroom and directly into a disgruntled Ichi"



    hide osoHeadAngry
    hide osoArmSchool
    hide osoBodySchool

    hide choroArmSchool
    hide choroBodySchool
    hide choroHeadNorm

    scene bgHallway with dissolve


    show osoArmSchool at Transform(function=transformLeft)  
    show osoHeadHappy at Transform(function=transformLeft) behind osoArmSchool 
    show osoBodySchool at Transform(function=transformLeft) behind osoHeadHappy 

    show ichiArmSchool at Transform(function=transformRight) 
    show ichiHeadNorm at Transform(function=transformRight) behind ichiArmSchool 
    show ichiBodySchool at Transform(function=transformRight) behind ichiHeadNorm 



    i "Osomatsu-niisan... Er."

    "Ichimatsu looks like he wants to tell Osomatsu something"

    i "Where... do babies come from...?"

    menu:
        "Nyahah you wanna borrow my porn and find out?":
            jump babyNeet
        "Onii-chan doesn't feel like explaining, go look it up yourself, Ichimatsu.":
            jump babyGrad
        "Shouldn't you know this by now?":
            jump babyHate






    label babyNeet:

    i ".... perverted niisan"
    return



    label babyGrad:
    i "*sigh* Should've known better than to ask you"

    return



    label babyHate:

    i "Sorry for asking."
    return


    # This ends the game.

    return
