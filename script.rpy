init:
    $ leftPos = Position(xpos=0.15, xanchor=0.15, ypos=1.0, yanchor=1.0)
    $ rightPos = Position(xpos=0.85, xanchor=0.85, ypos =1.0, yanchor=1.0)
    
# The script of the game goes in this file.

# Images are declared here

image oso normal = "oso_naked.png"
image oso normal flip = im.Flip("oso_naked.png",horizontal = True)
image oso faded flip = im.Flip(im.MatrixColor('oso_naked.png',im.matrix.brightness(-.25)), horizontal = True)
image kara normal = "kara_naked.png"

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define o = Character("Osomatsu", color = "#c20000")
define k = Character("Karamatsu", color = "#2860f0") 

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show oso normal flip at leftPos

    # These display lines of dialogue.

    "It's quiet"
    
    o "Hey hey where's everyone...?"

    hide oso normal flip
    show oso faded flip at leftPos
    show kara normal at rightPos
    
    k "You called, \brother\?"

    # This ends the game.

    return
