# micelle's scrip
# The game start

label start:
  
    scene bg_outside

    #show osoSera at right

    "One day SeraOso was walking to school"

    show osoSera at right

    o "COOL!"

    o "My uniform looks so cute" 

    show kara at left with dissolve

    k "Hello burazah, how are you this fine day?"

    "Osomatsu looked stunned"

    show osoSera angry at right

    o "What the hell Karamatsu!"

    o "Why the fuck are you naked?"

    k "Various circumstances has caused me to be in this form"

    k "Want to come with me?"

    menu:

        "WTF NO!":

            jump byeoso

        "Sure. I guess":
            $kara_points +=1
            jump why
        
       # "Pretend you didn't see him":        


label why:

    scene bg_fish
    with dissolve

    show kara at left

    k "Fishing is fun"

    show osoSera wut at right with dissolve

    o "You're fucked up"

    scene black
    with dissolve

    "The end"

    jump end
    
label byeoso:

    scene classroom
    with dissolve

    show osoSera

    o "Glad I could get away from that pervert"

label end:

    scene black
    with dissolve

    "The end"

return