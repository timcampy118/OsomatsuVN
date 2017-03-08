# micelle's scrip
# The game start

label start:
  
    scene bg_outside

    #show osoSera at right

    "One day SeraOso was walking to school"

    show seraOso at right

    o "COOL!"

    o "My uniform looks so cute" 

    show kara at left with dissolve

    with scrshake #sudden screen shake

    k "Hello burazah, how are you this fine day?"

    "Osomatsu looked stunned"

    show seraOso wut at right

    o "What the hell Karamatsu!"

    o "Why the fuck are you naked?"

    k "Various circumstances has caused me to be in this form"

    k "Want to come with me?"

    show seraOso blank at right

    call subroutine #in script2.rpy

    show seraOso wut at right

    o "What the hell was that?"

    show seraOso blank at right

    k "I have no idea."

    k "Nevetherless..."

    k "back to the question at hand..."

    k "Will you be coming with me Osomatsu?"

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

    show kara at left with moveinright

    k "Fishing is fun"

    show seraOso wut at right with tremble #show characters while shaking

    o "You're fucked up"

    jump end

   
label byeoso:

    scene classroom
    with dissolve

    show seraOso

    o "Glad I could get away from that pervert"

    hide seraOso with moveoutleft
    call subroutine

label end:

    scene black
    with dissolve

    "The end"

return