# micelle's script
# variables in different script


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

 #   scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

  #  show eileen happy
  
    scene bg_outside
    show oso_naked

    # These display lines of dialogue.

    "Look at that virgin NEET"

    o "COOL"

    o "I'm naked! Lookit me."

    "You wonder why this man is disgusting and yet his smile was ... nice"

    "sorta..."

    "actually he's quite charming."

    o "You want to come with me?"
    menu:

        "NO! Get away from me you pervert!":

            jump byeoso

        "Sure. I guess":

            jump why
        
       # "Pretend you didn't see him":        


label why:

    scene bg_fish
    with dissolve

    show oso_naked

    o "Fishing is fun"

    "Are you usually naked when you fish?"

    o "No."

    o "I just don't have clothes right now because I lost all my money in gambling"

    o "so I paid them with my clothes"

    scene black
    with dissolve

    "And thus begins your lovely adventure with this virgin NEET"

    return
label byeoso:

    scene black
    with dissolve

    "And thus ends your lovely adventure with this virgin NEET"

    return
