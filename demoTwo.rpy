label demoTwo:
        
    scene bg_hallway with fade
    
    show screen calendar
    $changeDate("JUL",18,"MORNING")
    
    play music "music/tell me hatabou.mp3" fadeout 2.0 fadein 2.0 
    
    show choro SchoolS 02 Nervous at pos7 with Dissolve(0.05)
    choro "We..."
    hide choro
    show todo SchoolS 02 Nervous at pos7 with Dissolve(0.05)
    todo "Barely..."
    hide todo
    show oso SchoolS 02 Happy1 at pos7 with Dissolve(0.05)
    oso "—PASSED!!!"
    show oso SchoolS 03 Happy1 at pos7 with Dissolve(0.05)
    oso "Ha! Told ya I'd be fine!"
    hide oso
    show ichi SchoolS 02 Angry2 at pos7 with Dissolve(0.05)
    ichi "Tch... I owe Todomatsu 500 yen..."
    hide ichi
    show oso SchoolS 03 Neutral Flip at pos3 with Dissolve(0.05)
    #show ichi SchoolS 02 Angry2 Fade at pos7 with Dissolve(0.1)
    oso "What was that?"
    show oso SchoolS 03 Neutral Fade Flip at pos3 with Dissolve(0.1)
    show jyushi SchoolS 03 Nervous at pos6 with Dissolve(0.05)
    jyushi "Nothing!"
    show oso SchoolS 03 Neutral Fade Flip at pos3 with Dissolve(0.1)
    show jyushi SchoolS 03 Happy1 at pos6 with Dissolve(0.05)
    jyushi "Ahaha! Let's get ready for summer!"
    show oso SchoolS 01 Happy1 Flip at pos3 with Dissolve(0.05)
    show jyushi SchoolS 03 Happy1 Fade at pos6 with Dissolve(0.1)
    oso "Oh... Haha. That's the spirit, Jyushimatsu!"
    hide oso
    hide jyushi
    hide ichi
    
    scene bg_kitchen with fade
    
    $changeDate("JUL",21,"MORNING")
    
    $ renpy.music.set_volume(0.7, delay=0, channel='music')
    play music "music/dogeza.ogg" fadeout 2.0 fadein 2.0 
    
    show oso Maintee 03 Sad Flip at pos3 
    show kara Maintee 01 Neutral Fade at pos6 
    oso "Ugh..."
    oso "The heat..."
    show oso Maintee 01 Sad Flip at pos3 with Dissolve(0.05)
    show kara Maintee 01 Neutral Fade at pos6 with Dissolve(0.1)
    oso "Karamatsu, can you pass me a popsicle?"
    show oso Maintee 01 Sad Fade Flip at pos3 with Dissolve(0.1)
    show kara Maintee 01 Neutral at pos6 with Dissolve(0.05)
    kara "Here you go, Osomatsu."
    show oso Maintee 01 Neutral Flip at pos3 with Dissolve(0.05)
    show kara Maintee 01 Neutral Fade at pos6 with Dissolve(0.1)
    oso "Aha, thanks! This tastes really good!"
    show oso Maintee 01 Neutral Fade Flip at pos3 with Dissolve(0.1)
    show kara Maintee 01 Happy1 at pos6 with Dissolve(0.05)
    kara "Heh. Of course it does, my brother. I poured all my passion into making it just right for everyone the night before!"
    show oso Maintee 01 Blank1 Flip at pos3 with Dissolve(0.05)
    show kara Maintee 01 Happy1 Fade at pos6 with Dissolve(0.1)
    oso "More like you poured all your sweat into it."
    hide oso
    hide kara
    show ichi Maintee 01 Neutral Flip at pos3 
    show jyushi Maintee 01 Displeased1 Fade at pos6 
    ichi "Time's up, Jyushimatsu. It's my turn to use the electric fan now."
    show ichi Maintee 01 Neutral Fade Flip at pos3 with Dissolve(0.1)
    show jyushi Maintee 01 Shocked1 at pos6 with Dissolve(0.05)
    jyushi "But it's so hot!"
    show ichi Maintee 02 Angry2 Flip at pos3 with Dissolve(0.05)
    show jyushi Maintee 01 Shocked1 Fade at pos6 with Dissolve(0.1)
    ichi "You've hogged it for an hour. Can't you share?"
    show ichi Maintee 02 Angry2 Fade Flip at pos3 with Dissolve(0.1)
    show jyushi Maintee 01 Angry1 at pos6 with Dissolve(0.05)
    jyushi "I need air conditioning!"
    show ichi Maintee 01 Gasp Flip at pos3 with Dissolve(0.05)
    show jyushi Maintee 01 Angry1 Fade at pos6 with Dissolve(0.1)
    ichi "C-Calm down, Jyushimatsu-”"
    
    play sound "sfx/crunch01.ogg"
    
    show ichi Maintee 01 Gasp Fade Flip at pos3 with Dissolve(0.1)
    show jyushi Maintee 03 Angry2 at pos6 with Dissolve(0.05)
    jyushi "{size=+10}{b}AIR CONDITIONING!!!{/b}{/size}" with scrShake
    show ichi Maintee 01 Shocked1 Flip at pos3 with Dissolve(0.05)
    show jyushi Maintee 03 Angry2 Fade at pos6 with Dissolve(0.1)
    ichi "—?!"
    show ichi Maintee 01 Nervous Flip at pos3 with Dissolve(0.05)
    show jyushi Maintee 03 Angry2 Fade at pos6 with Dissolve(0.1)
    ichi "D-Did you just eat the rest of our popsicles in one bite?"
    show ichi Maintee 01 Nervous Fade Flip at pos3 with Dissolve(0.1)
    show jyushi Maintee 03 Angry2 Fade at pos4 with move
    show choro Maintee 01 Angry3 at pos5 with moveinright
    choro "You know, you could've used a paper fan too, instead of eating all of that, right?"
    hide ichi
    hide jyushi
    hide choro
    #show oso Maintee 03 Blank1 Flip at pos3 with Dissolve(0.05)
    #show choro Maintee 01 Angry3 Fade at pos6 with Dissolve(0.1)
    #oso "Hot sure is summer..."
    #show oso Maintee 03 Blank1 Fade Flip at pos3 with Dissolve(0.1)
    #show choro Maintee 01 Blank1 at pos6 with Dissolve(0.05)
    #choro "Don't you mean, \"summer sure is hot?\""
    #show oso Maintee 03 Nervous Flip at pos3 with Dissolve(0.05)
    #show choro Maintee 01 Blank1 Fade at pos6 with Dissolve(0.1)
    #oso "Ah... The brain's really messing with my heat."
    show oso Maintee 03 Surprised Flip at pos7 with Dissolve(0.05)
    #show choro Maintee 01 Blank1 Fade at pos6 with Dissolve(0.1)
    oso "Gahh!! It's sooooo hot!"
    show oso Maintee 01 Shocked1 Flip at pos7 with Dissolve(0.05)
    #show choro Maintee 01 Blank1 Fade at pos6 with Dissolve(0.1)
    oso "And I'm sooooo bored..."
    show oso Maintee 01 Angry5 Flip at pos7 
    #show choro Maintee 01 Blank1 Fade at pos6 with Dissolve(0.1)
    oso "Can't summer be more exciting?!"
    #hide choro
    show oso Maintee 01 Angry5 Fade Flip at pos3 with move
    show todo Maintee 01 Angry1 at pos6 with Dissolve(0.05)
    #show todo Maintee 01 Angry1 at pos6 with moveinright
    
    todo "Ahh, geez! Osomatsu-niisan, will you shut up already?!"
    show oso Maintee 01 Angry5 Fade Flip at pos3 with Dissolve(0.1)
    show todo Maintee 01 Displeased1 at pos6 with Dissolve(0.05)
    todo "If you stopped moving around so much, you wouldn't feel as hot."
    hide oso
    hide todo
    
    scene bg_lr_daytime with fade
    $changeDate("JUL",21,"AFTERNOON")
    
    show oso Maintee 01 Sad Flip at pos7 with Dissolve(0.05)
    oso "Doesn't anyone else here feel bored?"
    show oso Maintee 01 Angry5 Flip at pos7 with Dissolve(0.05)
    oso "It's only the third day of summer, and I'm already dying of boredom!"
    show oso Maintee 01 Blank1 Fade Flip at pos7 with Dissolve(0.1)
    everyoneelse "..."
    show oso Maintee 01 Displeased1 Flip at pos7 with Dissolve(0.05)
    oso "{i}Everyone's ignoring me, huh.{/i}"
    show oso Maintee 02 Happy1 Flip at pos7 with Dissolve(0.05)
    oso "Oh!"
    show oso Maintee 02 Neutral Flip at pos7 with Dissolve(0.05)
    oso "Why don't we all go to the beach?"
    
    show oso Maintee 02 Neutral Fade Flip at pos3 with move
    show jyushi Maintee 01 Thinking at pos6 with Dissolve(0.05)
    jyushi "Beach?!"
    jyushi "Right now?!"
    
    show oso Maintee 02 Neutral Flip at pos3 with Dissolve(0.05)
    show jyushi Maintee 01 Thinking Fade at pos6 with Dissolve(0.1)
    oso "What better time to go than the present?"
    
    hide jyushi
    show oso Maintee 02 Neutral Fade Flip at pos3 with Dissolve(0.1)
    show todo Maintee 01 Neutral at pos6 with Dissolve(0.05)
    show sweatTick at pos6 with Dissolve(0.05)
    todo "Osomatsu-niisan, that's too abrupt."
    
    hide todo
    hide sweatTick
    show kara Maintee 01 Neutral at pos6 with Dissolve(0.1)
    kara "Todomatsu's right, but..."
    
    show oso Maintee 02 Neutral Flip at pos3 with Dissolve(0.05)
    show kara Maintee 01 Neutral Fade at pos6 with Dissolve(0.1)
    oso "\"But?\""
    
    show oso Maintee 02 Neutral Fade Flip at pos3 with Dissolve(0.1)
    show kara Maintee 01 Happy1 at pos6 with Dissolve(0.05)
    kara "It'll be the perfect place for me to put my hard work to good use!"
    
    show oso Maintee 02 Neutral Fade Flip at pos3 with Dissolve(0.1)
    show kara Maintee 01 Happy1 Fade at pos4 with move
    show choro Maintee 01 Displeased1 at pos5 with Dissolve(0.05)
    choro "Don't you dare, Karamatsu-niisan!"
    
    show oso Maintee 02 Happy1 Flip at pos3 with Dissolve(0.05)
    show kara Maintee 01 Happy1 Fade at pos4 with Dissolve(0.1)
    show choro Maintee 01 Displeased1 Fade at pos5 with Dissolve(0.1)
    oso "No, please do! It'll be hilarious!"
    
    hide choro
    hide kara
    show oso Maintee 02 Happy1 Fade Flip at pos3 with Dissolve(0.1)
    show todo Maintee 01 Surprised at pos6 with Dissolve(0.05)
    todo "Wait, so we {i}are{/i} going right now?"
    
    show oso Maintee 02 Neutral Flip at pos3 with Dissolve(0.05)
    show todo Maintee 01 Surprised Fade at pos6 with Dissolve(0.1)
    oso "Why not? Jyushimatsu's already in his swimsuit."
    
    show oso Maintee 02 Neutral Fade Flip at pos3 with Dissolve(0.1)
    show todo Maintee 01 Shocked1 at pos6 with Dissolve(0.05)
    todo "When- What?!"
    
    show oso Maintee 02 Neutral Fade Flip at pos3 with Dissolve(0.1)
    show todo Maintee 01 Shocked1 Fade at pos4 with move
    show jyushi Swim 03 Happy1 at pos5 with Dissolve(0.05)
    jyushi "Beach! Beach!"
    
    hide oso
    show choro Maintee 01 Neutral Flip at pos3 with Dissolve(0.05)
    show todo Maintee 01 Shocked1 Fade at pos4 with Dissolve(0.1)
    show jyushi Swim 03 Happy1 Fade at pos5 with Dissolve(0.1)
    choro "Don't forget to pack sunscreen."
    
    show choro Maintee 01 Neutral Fade Flip at pos3 with Dissolve(0.1)
    show todo Maintee 01 Shocked1 Fade at pos4 with Dissolve(0.1)
    show jyushi Swim 03 Happy1 at pos5 with Dissolve(0.05)
    jyushi "Yes!"

    show choro Maintee 01 Neutral Fade Flip at pos3 with Dissolve(0.1)
    show todo Maintee 01 Displeased1 at pos4 with Dissolve(0.05)
    show jyushi Swim 03 Happy1 Fade at pos5 with Dissolve(0.1)
    todo "..."
    todo "Fine. But Karamatsu-niisan better not start monologuing when we get there!"
    
    stop music fadeout 2.0
    
    scene bg_black with fade
    $ renpy.pause(1.0, hard=True)
    scene bg_beach with fade
    
    $changeDate("JUL",25,"MORNING")
    $ renpy.music.set_volume(1.0, delay=0, channel='music')
    play music "music/chibita flower fairy.ogg" fadeout 2.0 fadein 2.0 
    
    show kara Swim 01 Surprised at pos7 with Dissolve(0.05)
    kara "Oh my! Whatever is this lovely maiden doing, lying unconsious on the shore?"
    show kara Swim 02 Thinking at pos7 with Dissolve(0.05)
    kara "As the prince of this kingdom, it is my sworn duty to ensure that no harm befalls any of my loyal subjects."
    show kara Swim 02 Displeased1 at pos7 with Dissolve(0.05)
    kara "It would be especially tragic to lose one of those that have graced this Earth with such divine beauty..."
    show kara Swim 03 Shocked1 at pos7 with Dissolve(0.05)
    kara "Oh! You're as cold as death..."
    show kara Swim 03 Sad at pos7 with Dissolve(0.05)
    kara "Come, let us hurry you back to the castle."
    show kara Swim 03 Gasp at pos7 with Dissolve(0.05)
    kara "My, how light you are... It is as if I am caressing a cloud, or perhaps a ghost from a dream... Your eyes remain closed, yet I feel as if you are gazing into my very core with tender, uncertain yearning..."
    $ renpy.music.set_volume(0.4, delay=0, channel='sound')
    play sound "sfx/smack01.ogg"
    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    stop music
    
    show kara Swim 01 Angry1 at pos7 with Dissolve(0.05)
    kara "{size=+10}{b}AHHH!!! OW, OW, OW!!! IT'S PINCHING ME!!! GET IT OFF!!! GET IT OFF!!!{/b}{/size}" with scrShake
    
    
    play music "music/tell me hatabou.mp3" fadeout 2.0 fadein 2.0
    
   
    show kara Swim 01 Angry1 Fade at pos6 with move
    show choro Swim 01 Nervous Flip at pos3 with Dissolve(0.05)
    choro "Ah—! Karamatsu-niisan!"
    show choro Swim 01 Nervous Fade Flip at pos3 with Dissolve(0.1)
    show kara Swim 01 Shocked1 at pos6 with Dissolve(0.05)
    kara "Phew..."
    show choro Swim 01 Nervous Fade Flip at pos3 with Dissolve(0.1)
    show kara Swim 01 Blank1 at pos6 with Dissolve(0.05)
    kara "I thought I was going to die..."
    show choro Swim 01 Nervous Fade Flip at pos3 with Dissolve(0.1)
    show kara Swim 01 Happy1 at pos6 with Dissolve(0.05)
    kara "Thank you for getting rid of that crab, Choromatsu."
    show choro Swim 01 Displeased3 Flip at pos3 with Dissolve(0.05)
    show kara Swim 01 Happy1 Fade at pos6 with Dissolve(0.1)
    choro "What the hell were you doing...?"
    show choro Swim 01 Displeased3 Flip at pos3 with Dissolve(0.05)
    show kara Swim 01 Happy1 Fade at pos6 with Dissolve(0.1)
    choro "Talking like that to a crab... And what did we say about monologuing?"
    show choro Swim 01 Displeased3 Fade Flip at pos3 with Dissolve(0.1)
    show kara Swim 02 Neutral at pos6 with Dissolve(0.05)
    kara "I was trying to improve my acting."
    show choro Swim 01 Displeased3 Fade Flip at pos3 with Dissolve(0.1)
    show kara Swim 02 Displeased2 at pos6 with Dissolve(0.05)
    kara "Since I failed in obtaining the lead role..."
    hide choro
    show oso Swim 01 Neutral Flip at pos3 with Dissolve(0.05)
    show kara Swim 02 Displeased2 Fade at pos6 with Dissolve(0.1)
    oso "Nyahahaha! Your acting was really funny, Karamatsu!"
    show oso Swim 01 Happy1 Flip at pos3 with Dissolve(0.05)
    show kara Swim 02 Displeased2 Fade at pos6 with Dissolve(0.1)
    oso "Haaa, I haven't laughed this hard in a while!"
    show oso Swim 01 Happy1 Fade Flip at pos3 with Dissolve(0.1)
    show kara Swim 02 Nervous at pos6 with Dissolve(0.05)
    kara "You were watching the whole time?!"
    show oso Swim 01 Neutral Flip at pos3 with Dissolve(0.05)
    show kara Swim 02 Nervous Fade at pos6 with Dissolve(0.1)
    oso "Yup!"
    show oso Swim 01 Neutral Fade Flip at pos3 with Dissolve(0.1)
    show kara Swim 03 Nervous at pos6 with Dissolve(0.05)
    kara "W-Why didn't you help me with the crab?"
    show oso Swim 03 Happy1 Flip at pos3 with Dissolve(0.05)
    show kara Swim 03 Nervous Fade at pos6 with Dissolve(0.1)
    oso "Because it was way too funny!"
    show oso Swim 03 Happy1 Fade Flip at pos3 with Dissolve(0.1)
    show kara Swim 03 Nervous at pos6 with Dissolve(0.05)
    kara "I... I see. Well, nevermind that."
    show oso Swim 03 Happy1 Fade Flip at pos3 with Dissolve(0.1)
    show kara Swim 03 Nervous at pos6 with Dissolve(0.05)
    kara "W-What did you think of my acting?"
    show oso Swim 03 Gasp Flip at pos3 with Dissolve(0.05)
    show kara Swim 03 Nervous Fade at pos6 with Dissolve(0.1)
    oso "Oh, um..."
    
    
    menu:
        
        "It was so bad, it was funny!":
   
            show oso Swim 03 Happy1 Flip at pos3 with Dissolve(0.05)
            show kara Swim 03 Nervous Fade at pos6 with Dissolve(0.1)
            oso "You'd be a hit playing the butt of the joke! Ahaha!"
            
        "You have a lotta potential!":
            show oso Swim 03 Neutral Flip at pos3 with Dissolve(0.05)
            show kara Swim 03 Nervous Fade at pos6 with Dissolve(0.1)
            oso "Just keep practicing and you'll be able to get the lead role one day!"
            show oso Swim 03 Neutral Flip at pos3 with Dissolve(0.05)
            show kara Swim 03 Nervous Fade at pos6 with Dissolve(0.1)
            oso "Trust me! I'm your older brother, after all."
        
            
        "It looked natural, I guess.":
            show oso Swim 03 Happy1 Flip at pos3 with Dissolve(0.05)
            show kara Swim 03 Nervous Fade at pos6 with Dissolve(0.1)
            oso "I think it suits you!"
            show oso Swim 03 Thinking Flip at pos3 with Dissolve(0.05)
            show kara Swim 03 Nervous Fade at pos6 with Dissolve(0.1)
            oso "But it's not like I know much about acting in the first place."
    
    
    show oso Swim 03 Neutral Fade Flip at pos3 with Dissolve(0.1)
    show kara Swim 01 Gasp at pos6 with Dissolve(0.05)
    kara "I see..."
    show oso Swim 03 Neutral Fade Flip at pos3 with Dissolve(0.1)
    show kara Swim 01 Neutral at pos6 with Dissolve(0.05)
    kara "Thanks for the feedback, Osomatsu."
    show oso Swim 03 Neutral Fade Flip at pos3 with Dissolve(0.1)
    show kara Swim 01 Neutral Fade at pos4 with move
    show choro Swim 03 Neutral at pos5 with Dissolve(0.05)
    choro "You should have more confidence in yourself, Karamatsu-niisan."
    show oso Swim 03 Neutral Fade Flip at pos3 with Dissolve(0.1)
    show kara Swim 01 Neutral Fade at pos4 with Dissolve(0.1)
    show choro Swim 03 Happy1 at pos5 with Dissolve(0.05)
    choro "After all, didn't you join the drama club because you enjoyed their performance at the cultural festival?"
    show oso Swim 03 Neutral Fade Flip at pos3 with Dissolve(0.1)
    show kara Swim 01 Displeased2 at pos4 with Dissolve(0.05)
    show choro Swim 03 Happy1 Fade at pos5 with Dissolve(0.1)
    kara "Ah... That's true."
    show oso Swim 03 Displeased1 Flip at pos3 with Dissolve(0.05)
    show kara Swim 01 Displeased2 Fade at pos4 with Dissolve(0.1)
    show choro Swim 03 Happy1 Fade at pos5 with Dissolve(0.1)
    oso "It's nothing to be stressed about. "
    show oso Swim 03 Neutral Flip at pos3 with Dissolve(0.05)
    show kara Swim 01 Displeased2 Fade at pos4 with Dissolve(0.1)
    show choro Swim 03 Happy1 Fade at pos5 with Dissolve(0.1)
    oso "Right now, we're here to enjoy summer!"
    show oso Swim 03 Displeased1 Flip at pos3 with Dissolve(0.05)
    show kara Swim 01 Displeased2 Fade at pos4 with Dissolve(0.1)
    show choro Swim 03 Neutral Fade at pos5 with Dissolve(0.1)
    oso "But it's pretty disappointing to see that there aren't many people here..."
    show oso Swim 03 Angry1 Flip at pos3 with Dissolve(0.05)
    show kara Swim 01 Displeased2 Fade at pos4 with Dissolve(0.1)
    show choro Swim 03 Neutral Fade at pos5 with Dissolve(0.1)
    oso "...And it's all old people! What the hell?!"
    show oso Swim 03 Angry4 Flip at pos3 with Dissolve(0.05)
    show kara Swim 01 Displeased2 Fade at pos4 with Dissolve(0.1)
    show choro Swim 03 Neutral Fade at pos5 with Dissolve(0.1)
    oso "I don't wanna see some grandpa's back."
    show oso Swim 03 Angry2 Fade Flip at pos3 with Dissolve(0.1)
    show kara Swim 01 Displeased2 Fade at pos4 with Dissolve(0.1)
    show choro Swim 01 Blank1 at pos5 with Dissolve(0.05)


    choro "Speaking of seeing, I can see Ichimatsu, Jyushimatsu and Todomatsu from here."
    
    #hide choro with Dissolve(0.05)
    #hide kara with Dissolve(0.05)
    #hide oso with Dissolve(0.05)
    #show jyushi Swim 03 Neutral Flip at pos3 with Dissolve(0.05)
    
    #show todo Swim 01 Neutral Fade at pos4 with Dissolve(0.05)
    #show ichi Swim 01 Neutral Fade at pos5 with Dissolve(0.05)
    #jyushi "YAHOOOO!!!"
    
    
    
    hide choro with moveoutright
    hide kara with moveoutright
    hide oso  with moveoutleft
    show jyushi Swim 03 Neutral Flip at pos3 with moveinleft
    
    show todo Swim 01 Neutral Fade at pos4 with moveinright
    show ichi Swim 01 Neutral Fade at pos5 with moveinright
    jyushi "YAHOOOO!!!"
    
    show jyushi Swim 03 Neutral at pos3 with Dissolve(0.05)
    hide jyushi with moveoutleft
    #show jyushi Swim 03 Neutral Fade Flip at pos3 with Dissolve(0.1)
    show todo Swim 03 Nervous at pos4 with Dissolve(0.05)
    show ichi Swim 01 Neutral Fade at pos5 with Dissolve(0.1)
    todo "Jyushimatsu-niisan, wait! You need to put some sunscreen on first!"
    #show jyushi Swim 03 Neutral Fade Flip at pos3 with Dissolve(0.1)
    show todo Swim 03 Nervous at pos4 with Dissolve(0.05)
    show ichi Swim 01 Neutral Fade at pos5 with Dissolve(0.1)
    todo "Don't just run off like that..."
    #show jyushi Swim 03 Neutral Fade Flip at pos3 with Dissolve(0.1)
    show todo Swim 03 Surprised Flip at pos4 with Dissolve(0.05)
    show ichi Swim 01 Neutral Fade at pos5 with Dissolve(0.1)
    todo "Ah, geez! Jyushimatsu-niisan is so energetic."
    #hide jyushi
    show todo Swim 03 Surprised Flip at pos4 with Dissolve(0.05)
    show ichi Swim 01 Neutral Fade at pos5 with Dissolve(0.1)
    todo "It's hard to keep up with his pace."
    show todo Swim 03 Surprised Fade Flip at pos4 with Dissolve(0.1)
    show ichi Swim 01 Neutral at pos5 with Dissolve(0.05)
    ichi "Mm... Yeah."
    show todo Swim 01 Happy1 Flip at pos4 with Dissolve(0.05)
    show ichi Swim 01 Happy1 Fade at pos5 with Dissolve(0.1)
    todo "Ahh, whatever! I'm just going to relax under this shade~"
    show todo Swim 01 Happy1 Flip Fade at pos4 with Dissolve(0.1)
    show ichi Swim 01 Angry2 at pos5 with Dissolve(0.05)
    ichi "You're just gonna lie there...?"
    show todo Swim 01 Happy1 Flip at pos4 with Dissolve(0.05)
    show ichi Swim 01 Angry2 Fade at pos5 with Dissolve(0.1)
    todo "Hmm... Yep! Call me when the watermelon splitting game starts."
    show todo Swim 01 Happy1 Fade Flip at pos4 with Dissolve(0.1)
    show ichi Swim 01 Angry2 at pos5 with Dissolve(0.05)
    ichi "Eh..."

    show oso Swim 01 Happy1 Flip at pos3 with Dissolve(0.05)
    show todo Swim 01 Happy1 Fade at pos4 with Dissolve(0.1)
    show ichi Swim 01 Angry2 Fade at pos5 with Dissolve(0.1)
    oso "Yo, Ichimatsu~! Todomatsu~!"
    show oso Swim 01 Happy1 Fade Flip at pos2 with move
    show choro Swim 01 Displeased3 Flip at pos1 with Dissolve(0.05)
    show todo Swim 01 Happy1 Fade at pos4 with Dissolve(0.1)
    show ichi Swim 01 Angry2 Fade at pos5 with Dissolve(0.1)
    choro "Oh, you two aren't going to play in the water? "
    show choro Swim 01 Displeased3 Fade Flip at pos1 with Dissolve(0.1)
    show oso Swim 01 Happy1 Fade Flip at pos2 with Dissolve(0.1)
    show todo Swim 01 Happy2 at pos4 with Dissolve(0.05)
    show ichi Swim 01 Angry2 Fade at pos5 with Dissolve(0.1)
    todo "Mmm~? I'm okay with relaxing in the shade. I might even nap for a bit."
    hide todo
    show choro Swim 01 Displeased3 Fade Flip at pos1 with Dissolve(0.1)
    show oso Swim 01 Thinking Flip at pos2 with Dissolve(0.05)
    show ichi Swim 01 Angry2 Fade at pos6 with move
    oso "Yeah, yeah. Good night, little princess. "
    show choro Swim 01 Displeased3 Fade Flip at pos1 with Dissolve(0.1)
    show oso Swim 01 Thinking Fade Flip at pos2 with Dissolve(0.1)
    show ichi Swim 01 Neutral at pos6 with Dissolve(0.05)
    ichi "Mmm... I'm going to go look for shells."
    hide ichi
    show choro Swim 01 Displeased3 Fade Flip at pos1 with Dissolve(0.1)
    show oso Swim 01 Thinking Fade Flip at pos2 with Dissolve(0.1)
    show kara Swim 01 Neutral at pos6 with Dissolve(0.1)
    kara "It's just as Todomatsu said. Let us sit down and relax, Choromatsu."
    show choro Swim 01 Displeased3 Fade Flip at pos1 with Dissolve(0.1)
    show oso Swim 01 Thinking Fade Flip at pos2 with Dissolve(0.1)
    show kara Swim 02 Neutral at pos6 with Dissolve(0.05)
    kara "Ah, this is quite the comfortable rock. It's much softer than any I've ever sat on before."
    
    stop music fadeout 2.0
    
    show choro Swim 01 Blank1 Fade Flip at pos1 with Dissolve(0.1)
    show oso Swim 01 Blank1 Fade Flip at pos2 with Dissolve(0.1)
    show kara Swim 01 Blank1 Fade at pos6 with Dissolve(0.1)
    mystery "MMRHGRHGRH!!!" 
    show choro Swim 01 Blank1 Fade Flip at pos1 with Dissolve(0.1)
    show oso Swim 01 Blank1 Fade Flip at pos2 with Dissolve(0.1)
    show kara Swim 01 Blank1 at pos6 with Dissolve(0.05)
    kara "Hm...? Did you guys hear that?"
    show choro Swim 01 Blank1 Fade Flip at pos1 with Dissolve(0.1)
    show oso Swim 01 Thinking Flip at pos2 with Dissolve(0.05)
    show kara Swim 01 Blank1 Fade at pos6 with Dissolve(0.1)
    oso "I think it's coming from the rock..."
    show choro Swim 01 Nervous Flip at pos1 with Dissolve(0.05)
    show oso Swim 01 Thinking Fade Flip at pos2 with Dissolve(0.1)
    show kara Swim 01 Nervous Fade at pos6 with Dissolve(0.1)
    choro "Wait a second..."
    show choro Swim 01 Nervous Fade Flip at pos1 with Dissolve(0.1)
    show oso Swim 01 Happy1 Flip at pos2 with Dissolve(0.05)
    show kara Swim 01 Nervous Fade at pos6 with Dissolve(0.1)
    oso "Ahahahaha!! Karamatsu! You're sitting on Chibita!"
    show choro Swim 01 Nervous Fade Flip at pos1 with Dissolve(0.1)
    show oso Swim 01 Happy1 Fade Flip at pos2 with Dissolve(0.1)
    show kara Swim 01 Gasp at pos6 with Dissolve(0.05)
    kara "E-EH?!"
    hide choro
    hide oso
    hide kara
    show chibita Naked Angry1 Flip at cpos7 with Dissolve(0.05)
    chibita "{size=+10}{b}GET OFF, YA IDJIT!!!{/b}{/size}" with scrShake
    chibita "WHAT THE HELL!!! I WAS JUST RELAXING IN THE SAND—”"
    chibita "—AND YOU COME OVER AND SUFFOCATE ME WITH YOUR ASS?!"
    chibita "CAN'T I ENJOY MY SUMMER BREAK IN PEACE?! DAMN IT!"
    
    show chibita Naked Displeased2 Flip at cpos3 with move
    show oso Swim 01 Neutral Fade at pos4 with Dissolve(0.1)
    show choro Swim 01 Neutral Fade at pos5 with Dissolve(0.1)
    #show kara Swim 01 Neutral Fade at pos6 with Dissolve(0.1)
    chibita "Ah."
    show chibita Naked Displeased1 Flip at cpos3 
    show oso Swim 01 Neutral Fade at pos4 with Dissolve(0.1)
    show choro Swim 01 Neutral Fade at pos5 with Dissolve(0.1)
    #show kara Swim 01 Neutral Fade at pos6 with Dissolve(0.1)
    chibita "It's {i}you guys.{/i}"
    
    play music "music/dogeza.ogg" fadeout 2.0 fadein 2.0
    
    show chibita Naked Displeased1 Fade Flip at cpos3 with Dissolve(0.1)
    show oso Swim 01 Neutral at pos4 with Dissolve(0.05)
    show choro Swim 01 Neutral Fade at pos5 with Dissolve(0.1)
    oso "Hey, Chibita!"
    show chibita Naked Displeased1 Fade Flip at cpos3 with Dissolve(0.1)
    show oso Swim 01 Neutral Fade at pos4 with Dissolve(0.1)
    show choro Swim 01 Blank1 at pos5 with Dissolve(0.05)
    choro "Uhh... Why exactly were you buried in the sand up to your neck like that...?"
    show chibita Naked Displeased2 Flip at cpos3 with Dissolve(0.05)
    show oso Swim 01 Neutral Fade at pos4 with Dissolve(0.1)
    show choro Swim 01 Blank1 Fade at pos5 with Dissolve(0.1)
    chibita "Hah? Iyami told me that I'd grow taller if I planted myself in the sand."
    show chibita Naked Displeased2 Fade Flip at cpos3 with Dissolve(0.1)
    show oso Swim 01 Neutral Fade at pos4 with Dissolve(0.1)
    show choro Swim 01 Displeased3 at pos5 with Dissolve(0.05)
    choro "And you believed him...?"
    show chibita Naked Displeased2 Fade Flip at cpos3 with Dissolve(0.1)
    show oso Swim 01 Happy1 at pos4 with Dissolve(0.05)
    show choro Swim 01 Displeased3 Fade at pos5 with Dissolve(0.1)
    oso "Gyahahaha! How dumb can you be?!"
    show chibita Naked Displeased2 Fade Flip at cpos3 with Dissolve(0.1)
    show oso Swim 01 Neutral at pos4 with Dissolve(0.05)
    show choro Swim 01 Displeased3 Fade at pos5 with Dissolve(0.1)
    oso "Chibita... Being small is kinda your thing. If you were tall, you wouldn't be {i}Chibita{\i} anymore. "
    hide oso
    hide choro
    show chibita Naked Displeased2 Fade Flip at cpos3 with Dissolve(0.1)
    show kara Swim 01 Gasp at pos6 with Dissolve(0.05)
    kara "If Iyami told you that... Doesn't that mean he's here too? "
    hide chibita
    hide kara
    
    play music "music/tell me hatabou.mp3"
    
    show iyami Regular Happy1 Flip at pos7 with Dissolve(0.05)
    iyami "Uhyohyohyo!"
    iyami "This will be me's most genius plan ever! "
    show iyami Regular Happy1 Fade Flip at pos3 with move
    show oso Swim 01 Surprised at pos6 with Dissolve(0.05)
    oso "Eh? Iyami? "
    show iyami Regular Angry1 Flip at pos3 with Dissolve(0.05)
    show oso Swim 01 Surprised Fade at pos6 with Dissolve(0.1)
    iyami "SEXTUPLETS?!"
    show iyami Regular Displeased1 Flip at pos3 with Dissolve(0.05)
    show oso Swim 01 Surprised Fade at pos6 with Dissolve(0.1)
    iyami "What are you brats doing here?"
    show iyami Regular Displeased1 Fade Flip at pos3 with Dissolve(0.1)
    show oso Swim 01 Gasp at pos6 with Dissolve(0.05)
    oso "Huh? We should be the ones asking you that. "
    hide oso
    show iyami Regular Displeased1 Fade Flip at pos3 with Dissolve(0.1)
    show kara Swim 01 Displeased1 at pos6 with Dissolve(0.05)
    kara "You're planning another scam, huh?"
    show iyami Regular Displeased1 Flip at pos3 with Dissolve(0.05)
    show kara Swim 01 Displeased1 Fade at pos6 with Dissolve(0.1)
    iyami "It's not a scam, zansu. "
    show iyami Regular Happy1 Flip at pos3 with Dissolve(0.05)
    show kara Swim 01 Displeased1 Fade at pos6 with Dissolve(0.1)
    iyami "Me is just earning some side cash aside from me's job."
    hide kara
    show iyami Regular Happy1 Fade Flip at pos3 with Dissolve(0.1)
    show choro Swim 01 Happy1 at pos6 with Dissolve(0.05)
    choro "You have a job?!"
    show iyami Regular Neutral Flip at pos3 with Dissolve(0.05)
    show choro Swim 01 Happy1 Fade at pos6 with Dissolve(0.1)
    iyami "Me sells bread at your school, zansu."
    hide choro
    show iyami Regular Neutral Fade Flip at pos3 with Dissolve(0.1)
    show oso Swim 01 Gasp at pos6 with Dissolve(0.05)
    oso "What? You work at our school?"
    show iyami Regular Angry1 Flip at pos3 with Dissolve(0.05)
    show oso Swim 01 Gasp Fade at pos6 with Dissolve(0.1)
    iyami "SHEEEH!!! You don't even remember?!"
    show iyami Regular Angry1 Fade Flip at pos3 with Dissolve(0.1)
    show oso Swim 01 Gasp Fade at pos4 with move
    show choro Swim 01 Displeased1 at pos5 with Dissolve(0.05)
    choro "Come on, Osomatsu-niisan. Let's go somewhere else."
    show iyami Regular Angry1 Fade Flip at pos3 with Dissolve(0.1)
    show oso Swim 01 Gasp Fade at pos4 behind choro
    show choro Swim 01 Displeased1 Fade at pos6 with move
    show kara Swim 01 Displeased1 at pos5 onlayer master
    kara "Best to leave the man alone."
    show iyami Regular Neutral Flip at pos3 with Dissolve(0.05)
    show oso Swim 01 Gasp Fade at pos4 with Dissolve(0.1)
    show kara Swim 01 Displeased1 Fade at pos5 with Dissolve(0.1)
    show choro Swim 01 Displeased1 Fade at pos6 with Dissolve(0.1)
    iyami "W-Wait! What if me tells you something you could do!"
    show iyami Regular Neutral Fade Flip at pos3 
    show oso Swim 01 Neutral at pos4 with Dissolve(0.05)
    oso "...I'm listening. You guys go on ahead, I'm gonna stay here and be unbored."
    hide kara with moveoutright
    hide choro with moveoutright
    hide oso
    hide iyami
    show kara Swim 01 Neutral Fade Flip at pos3 with Dissolve(0.05)
    show choro Swim 01 Displeased3 at pos6 with Dissolve(0.05)
    choro "\"Unbored\" isn't a—"
    show kara Swim 01 Happy1 Flip at pos3 with Dissolve(0.05)
    show choro Swim 01 Displeased3 Fade at pos6 with Dissolve(0.1)
    kara "Let's go, Choromatsu. May I rub sunscreen on your back?"
    show kara Swim 01 Happy1 Fade Flip at pos3 with Dissolve(0.1)
    show choro Swim 01 Thinking at pos6 with Dissolve(0.05)
    choro "Ah, fine... It'll give me a chance to read a bit of {i}No Longer Human{/i}, anyway."
    hide kara
    hide choro
    show iyami Regular Neutral Fade Flip at pos3 with Dissolve(0.1)
    show oso Swim 01 Neutral at pos6 with Dissolve(0.05)
    oso "So what's this \"something\" you've got for me to do?"
    show iyami Regular Neutral Flip at pos3 with Dissolve(0.05)
    show oso Swim 01 Neutral Fade at pos6 with Dissolve(0.1)
    iyami "Me is teaching people how to surf, zansu."
    show iyami Regular Neutral Fade Flip at pos3 with Dissolve(0.1)
    show oso Swim 01 Displeased1 at pos6 with Dissolve(0.05)
    oso "But there's barely anyone here. Just a bunch of old geezers..."
    show iyami Regular Neutral Fade Flip at pos3 with Dissolve(0.1)
    show oso Swim 01 Displeased1 at pos6 with Dissolve(0.05)
    oso "Can you actually teach people?"
    show iyami Regular Neutral Flip at pos3 with Dissolve(0.05)
    show oso Swim 01 Displeased1 Fade at pos6 with Dissolve(0.1)
    iyami "Trust me, zansu. "
    show iyami Regular Happy1 Flip at pos3 with Dissolve(0.05)
    show oso Swim 01 Displeased1 Fade at pos6 with Dissolve(0.1)
    iyami "For a small price, me can teach you how to battle the waves."
    show iyami Regular Happy1 Fade Flip at pos3 with Dissolve(0.1)
    show oso Swim 01 Gasp at pos6 with Dissolve(0.05)
    oso "How much?"
    show iyami Regular Neutral Flip at pos3 with Dissolve(0.05)
    show oso Swim 01 Gasp Fade at pos6 with Dissolve(0.1)
    iyami "2,000 yen per person for two hours. zansu"
    show iyami Regular Neutral Fade Flip at pos3 with Dissolve(0.1)
    show oso Swim 01 Thinking at pos6 with Dissolve(0.05)
    oso "Hmm, how about... 1,000 yen per person for one hour?"
    show iyami Regular Neutral Fade Flip at pos3 with Dissolve(0.1)
    show oso Swim 01 Happy1 at pos6 with Dissolve(0.05)
    oso "Like, a sextuplet discount! "
    show iyami Regular Displeased1 Flip at pos3 with Dissolve(0.05)
    show oso Swim 01 Happy1 Fade at pos6 with Dissolve(0.1)
    iyami "Hm... "
    show iyami Regular Displeased1 Fade Flip at pos3 with Dissolve(0.1)
    show oso Swim 01 Angry3 at pos6 with Dissolve(0.05)
    oso "Come on, Iyami! We've known each other for a whileâ€”at least give us a discount!"
    show iyami Regular Displeased1 Flip at pos3 with Dissolve(0.05)
    show oso Swim 01 Angry3 Fade at pos6 with Dissolve(0.1)
    iyami "Hm..."
    show iyami Regular Displeased1 Fade Flip at pos3 with Dissolve(0.1)
    show oso Swim 01 Angry5 at pos6 with Dissolve(0.05)
    oso "Geez! If you're not gonna lower the price, I'm out! "
    show iyami Regular Angry1 Flip at pos3 with Dissolve(0.05)
    show oso Swim 01 Angry5 Fade at pos6 with Dissolve(0.1)
    iyami "SHEEEH!!! You're so annoying!"
    show iyami Regular Displeased1 Flip at pos3 with Dissolve(0.05)
    show oso Swim 01 Angry5 Fade at pos6 with Dissolve(0.1)
    iyami "Fine! 10,000 yen for the six of you and 6,000 yen for one big surfboard."
    show iyami Regular Displeased1 Flip at pos3 with Dissolve(0.05)
    show oso Swim 01 Angry5 Fade at pos6 with Dissolve(0.1)
    iyami "That's my deal, zansu."
    show iyami Regular Displeased1 Fade Flip at pos3 with Dissolve(0.1)
    show oso Swim 01 Gasp at pos6 with Dissolve(0.05)
    oso "Why one?"
    show iyami Regular Displeased1 Flip at pos3 with Dissolve(0.05)
    show oso Swim 01 Gasp Fade at pos6 with Dissolve(0.1)
    iyami "Well, would you rather pay for six surfboards?"
    show iyami Regular Happy1 Flip at pos3 with Dissolve(0.05)
    show oso Swim 01 Gasp Fade at pos6 with Dissolve(0.1)
    iyami "Besides, six people on one surfboard balances it better."
    show iyami Regular Happy1 Fade Flip at pos3 with Dissolve(0.1)
    show oso Swim 01 Thinking at pos6 with Dissolve(0.05)
    oso "You've got a point there..."
    show iyami Regular Happy1 Fade Flip at pos3 with Dissolve(0.1)
    show oso Swim 01 Happy1 at pos6 with Dissolve(0.05)
    oso "Alright, I'll take it."
    show iyami Regular Happy1 Flip at pos3 with Dissolve(0.05)
    show oso Swim 01 Happy1 Fade at pos6 with Dissolve(0.1)
    iyami "That'll be 1,000 yen extra."
    show iyami Regular Happy1 Fade Flip at pos3 with Dissolve(0.1)
    show oso Swim 01 Surprised at pos6 with Dissolve(0.05)
    oso "Eh?! Why?!"
    show iyami Regular Neutral Flip at pos3 with Dissolve(0.05)
    show oso Swim 01 Surprised Fade at pos6 with Dissolve(0.1)
    iyami "You have to make an appointment, so if you pay now for a slot, you won't have to wait long."
    show iyami Regular Neutral Fade Flip at pos3 with Dissolve(0.1)
    show oso Swim 01 Surprised at pos6 with Dissolve(0.05)
    oso "Who the hell are you even teaching here?!"
    show iyami Regular Displeased1 Flip at pos3 with Dissolve(0.05)
    show oso Swim 01 Surprised Fade at pos6 with Dissolve(0.1)
    iyami "You want the deal or not, zansu? "
    show iyami Regular Displeased1 Fade Flip at pos3 with Dissolve(0.1)
    show oso Swim 01 Angry3 at pos6 with Dissolve(0.05)
    oso "Tch... Fine, whatever. Stingy."
    show iyami Regular Displeased1 Fade Flip at pos3 with Dissolve(0.1)
    show oso Swim 01 Angry3 at pos6 with Dissolve(0.05)
    oso "{i}I can't believe I'm going through all this trouble just to get my brothers to play with me...{/i}"
    show iyami Regular Displeased1 Fade Flip at pos3 with Dissolve(0.1)
    show oso Swim 01 Sad at pos6 with Dissolve(0.05)
    oso "{i}This better be worth it.{/i}"

    scene bg_beach with fade
    $changeDate("JUL",25,"AFTERNOON")

    # BGM TBD
    play music "music/dogeza.ogg" fadeout 2.0 fadein 2.0
    
    hide iyami
    show oso Swim 02 Neutral Flip at pos3 with Dissolve(0.05)
    hide todo
    oso "Hey, guys! Guess what?"
    show oso Swim 02 Neutral Fade Flip at pos3 with Dissolve(0.1)
    show todo Swim 01 Blank1 at pos6 with Dissolve(0.05)
    todo "Found some cliff for us to jump off of?"
    show oso Swim 02 Neutral Fade Flip at pos3 with Dissolve(0.1)
    show todo Swim 01 Thinking at pos6 with Dissolve(0.05)
    todo "I'm sure Ichimatsu-niisan would like that."
    show oso Swim 02 Neutral Fade Flip at pos3 with Dissolve(0.1)
    show todo Swim 01 Thinking Fade at pos4 with move
    show ichi Swim 01 Happy1 at pos5 with Dissolve(0.05)
    ichi "Finally... Bring me there."
    show oso Swim 01 Blank1 Flip at pos3 with Dissolve(0.05)
    show todo Swim 01 Thinking Fade at pos4 with Dissolve(0.1)
    show ichi Swim 01 Happy1 Fade at pos5 with Dissolve(0.1)
    oso "What? No, no, it's something else."
    show oso Swim 01 Blank1 Fade Flip at pos3 with Dissolve(0.1)
    show todo Swim 01 Neutral Fade at pos4 with Dissolve(0.1)
    show ichi Swim 01 Thinking at pos5 with Dissolve(0.05)
    ichi "Oh."
    hide todo
    hide ichi
    show oso Swim 01 Blank1 Fade Flip at pos3 with Dissolve(0.1)
    show jyushi Swim 01 Happy1 at pos4 with Dissolve(0.05)
    show kara Swim 01 Happy1 Fade at pos5 with Dissolve(0.1)
    jyushi "Want some watermelon, Osomatsu-niisan?"
    show oso Swim 01 Blank1 Fade Flip at pos3 with Dissolve(0.1)
    show jyushi Swim 01 Happy1 Fade at pos4 with Dissolve(0.1)
    show kara Swim 01 Happy1 at pos5 with Dissolve(0.05)
    kara "We saved you a slice."
    show oso Swim 01 Happy1 Flip at pos3 with Dissolve(0.05)
    show jyushi Swim 01 Happy1 Fade at pos4 with Dissolve(0.1)
    show kara Swim 01 Happy1 Fade at pos5 with Dissolve(0.1)
    oso "No thanks, I found something fun for us to do!"
    show oso Swim 01 Neutral Flip at pos3 with Dissolve(0.05)
    show jyushi Swim 01 Happy1 Fade at pos4 with Dissolve(0.1)
    show kara Swim 01 Happy1 Fade at pos5 with Dissolve(0.1)
    oso "It'll be one of those \"wild high school memories\" we can look back on and laugh about when we get older!"
    show oso Swim 01 Happy1 Flip at pos3 with Dissolve(0.05)
    show jyushi Swim 01 Happy1 Fade at pos4 with Dissolve(0.1)
    show kara Swim 01 Happy1 Fade at pos5 with Dissolve(0.1)
    oso "We're going surfing!"
    show oso Swim 01 Thinking Flip at pos3 with Dissolve(0.05)
    show jyushi Swim 01 Happy1 Fade at pos4 with Dissolve(0.1)
    show kara Swim 01 Happy1 Fade at pos5 with Dissolve(0.1)
    oso "...And Iyami will be teaching us how. "
    hide jyushi
    show oso Swim 01 Thinking Fade Flip at pos3 with Dissolve(0.1)
    show choro Swim 01 Blank1 at pos6 with Dissolve(0.05)
    hide kara
    choro "Surfing?"
    show oso Swim 01 Thinking Fade Flip at pos3 with Dissolve(0.1)
    show choro Swim 01 Displeased3 at pos6 with Dissolve(0.05)
    choro "We barely come here... What good would learning how to surf do us?"
    show oso Swim 02 Neutral Flip at pos3 with Dissolve(0.05)
    show choro Swim 01 Displeased3 Fade at pos6 with Dissolve(0.1)
    oso "But that's the point! That's why we should jump on this opportunity."
    show oso Swim 02 Neutral Flip at pos3 with Dissolve(0.05)
    show choro Swim 01 Displeased3 Fade at pos6 with Dissolve(0.1)
    oso "No time like the present, right? Let's make these memories while we still have the chance!"
    show oso Swim 01 Gasp Flip at pos3 with Dissolve(0.05)
    show choro Swim 01 Displeased3 Fade at pos6 with Dissolve(0.1)
    oso "Plus, I already paid with the money Dad gave us for the trip, so we might as well."
    hide oso
    hide choro
    show kara Swim 01 Displeased1 Flip at pos1 with Dissolve(0.05)
    show choro Swim 01 Angry2 at pos6 with Dissolve(0.05)
    show jyushi Swim 01 Displeased1 at pos5 with Dissolve(0.05)
    show todo Swim 01 Displeased1 at pos4 behind choro
    show ichi Swim 01 Displeased1 Flip at pos3 with Dissolve(0.05)
    rest "Ugggghhh..."
    hide kara
    hide choro
    hide ichi
    hide jyushi
    hide todo
    show todo Swim 02 Thinking at pos6 with Dissolve(0.05)
    todo "Well, if Dad is already paying, then I guess I don't see the harm..."
    show kara Swim 02 Blank1 Flip at pos3 with Dissolve(0.05)
    show todo Swim 02 Displeased1 Fade at pos6 with Dissolve(0.1)
    kara "Oh? You're actually going to surf, Todomatsu?"
    show kara Swim 02 Blank1 Fade Flip at pos3 with Dissolve(0.1)
    show todo Swim 02 Thinking at pos6 with Dissolve(0.05)
    todo "I don't see why not. I can't lay around all day without getting bored."
    show kara Swim 02 Blank1 Fade Flip at pos3 with Dissolve(0.1)
    show todo Swim 01 Happy1 at pos6 with Dissolve(0.05)
    todo "So why not get \"on board\" too~"
    hide kara
    hide todo
    show jyushi Swim 01 Happy1 Flip at pos3 
    show ichi Swim 01 Happy1 Fade at pos6 
    jyushi "HAHAHA!!! Good one, Todomatsu!"
    show jyushi Swim 01 Happy1 Fade Flip at pos3 with Dissolve(0.1)
    show ichi Swim 01 Happy1 at pos6 with Dissolve(0.05)
    ichi "Heh... Sure, let's try this out."
    hide jyushi
    hide ichi
    show oso Swim 01 Neutral Fade Flip at pos3 with Dissolve(0.1)
    show choro Swim 02 Displeased3 at pos6 with Dissolve(0.05)
    choro "Alright, but we better watch the time. We should head home before it gets dark."
    show oso Swim 01 Happy1 Flip at pos3 with Dissolve(0.05)
    show choro Swim 02 Displeased3 Fade at pos6 with Dissolve(0.1)
    oso "Yahoo! Surfing!"
    show oso Swim 01 Happy1 Fade Flip at pos3 with Dissolve(0.1)
    show choro Swim 02 Angry2 at pos6 with Dissolve(0.05)
    choro "Oi, hold on! It's lunch time. We should eat a bit before we head out."
    show oso Swim 02 Neutral Flip at pos3 with Dissolve(0.05)
    show choro Swim 02 Angry2 Fade at pos6 with Dissolve(0.1)
    oso "Mmmm... Food~"
    hide oso
    hide choro
    show kara Swim 02 Neutral at pos7 with Dissolve(0.05)
    kara "Ah, there it is. The eldest and his love of food."
    hide kara
    show ichi Swim 01 Happy1 at pos7 with Dissolve(0.05)
    ichi "Gross."
    hide ichi
    show jyushi Swim 01 Happy1 at pos7 with Dissolve(0.05)
    jyushi "Osomatsu-niisan's gross! Ahahaha!"
    hide jyushi
    show todo Swim 01 Happy1 at pos7 with Dissolve(0.05)
    todo "Yep, yep! He moves too much in his sleep too."
    hide todo
    show choro Swim 01 Displeased3 at pos7 with Dissolve(0.05)
    choro "Glad I'm not the only one who thinks that. "
    hide choro
    show oso Swim 01 Angry4 at pos7 with Dissolve(0.05)
    oso "Why are you all picking on Onii-chan?"
    hide oso
    show oso Swim 01 Angry4 Fade Flip at pos3 with Dissolve(0.1)
    show todo Swim 02 Happy1 at pos6 with Dissolve(0.05)
    todo "You did say we needed to bond as a family, Osomatsu-niisan."
    show oso Swim 03 Sad Flip at pos3 with Dissolve(0.05)
    show todo Swim 02 Happy1 Fade at pos6 with Dissolve(0.1)
    oso "Fine... I'll take it."
    show oso Swim 02 Neutral Flip at pos3 with Dissolve(0.05)
    show todo Swim 02 Happy1 Fade at pos6 with Dissolve(0.1)
    oso "Thanks for the food!"
    hide todo
    
    # BEACH WAVES (probably sound looped instead of music)
    play audio "<loop 0.0>sfx/beachwaves.ogg"
  
    scene bg_beach with fade
    
    show iyami Regular Displeased1 Fade Flip at pos3 with Dissolve(0.1)
    show oso Swim 01 Happy1 at pos6 with Dissolve(0.05)
    oso "Yo, Iyami!"
    show iyami Regular Displeased1 Flip at pos3 with Dissolve(0.05)
    show oso Swim 01 Happy1 Fade at pos6 with Dissolve(0.1)
    iyami "You're all late, zansu."
    show iyami Regular Displeased1 Flip at pos3 with Dissolve(0.05)
    show oso Swim 01 Happy1 Fade at pos6 with Dissolve(0.1)
    iyami "Hurry and start warming up!"
    hide oso
    show iyami Regular Displeased1 Fade Flip at pos3 with Dissolve(0.1)
    show kara Swim 01 Blank1 at pos6 with Dissolve(0.05)
    kara "What are we supposed to do?"
    show iyami Regular Happy1 Flip at pos3 with Dissolve(0.05)
    show kara Swim 01 Blank1 Fade at pos6 with Dissolve(0.1)
    iyami "For your training, you'll need to learn how to catch a wave, zansu. "
    hide kara
    show iyami Regular Happy1 Fade Flip at pos3 with Dissolve(0.1)
    show choro Swim 01 Displeased3 at pos6 with Dissolve(0.05)
    choro "And how do we do that? "
    show iyami Regular Displeased1 Flip at pos3 with Dissolve(0.05)
    show choro Swim 01 Displeased3 Fade at pos6 with Dissolve(0.1)
    iyami "Just shut your mouth and listen to me, zansu. "
    show iyami Regular Displeased1 Flip at pos3 with Dissolve(0.05)
    show choro Swim 01 Displeased3 Fade at pos6 with Dissolve(0.1)
    iyami "Now, let's start. Go and ride that wave."
    show iyami Regular Displeased1 Fade Flip at pos3 with Dissolve(0.1)
    
    show todo Swim 01 Shocked1 at pos5 with Dissolve(0.05)
    show choro Swim 01 Shocked1 Fade at pos6 with Dissolve(0.1)
    show kara Swim 01 Shocked1 Fade at pos4 behind choro
    todo "Eh-?! That huge one?! Now?!"
    show iyami Regular Displeased1 Fade Flip at pos3 with Dissolve(0.1)
    show choro Swim 01 Shocked1 at pos6 with Dissolve(0.05)
    show kara Swim 01 Shocked1 Fade at pos4 behind choro
    show todo Swim 01 Shocked1 Fade at pos5 behind choro
    choro "Surely we have to start with some warm-ups first?!"
    show iyami Regular Displeased1 Fade Flip at pos3 with Dissolve(0.1)
    show kara Swim 01 Shocked1 at pos4 with Dissolve(0.05)
    show todo Swim 01 Shocked1 Fade at pos5 with Dissolve(0.1)
    show choro Swim 01 Shocked1 Fade at pos6 behind kara
    kara "Or perhaps start with trying to balance on the board on land at least?!"
    hide iyami
    hide kara
    hide todo
    hide choro
    show iyami Regular Angry1 at pos7 with Dissolve(0.05)
    iyami "Shut up, zansu!"
    show iyami Regular Angry1 Fade at pos7 with Dissolve(0.1)
    everyone "...?!" 
    show iyami Regular Angry1 at pos7 with Dissolve(0.05)
    iyami "Who do you think is the teacher here?!"
    show iyami Regular Angry1 at pos7 with Dissolve(0.05)
    iyami "It's me! So if I say to do something, you should just do it, zansu!!"
    hide iyami
    show oso Swim 01 Nervous at pos7 with Dissolve(0.05)
    oso "C-Come on, guys! I mean, it'll probably be okay, right...?"
    show oso Swim 01 Nervous Fade at pos7 with Dissolve(0.1)
    mystery "Wow, Natsume! You're doing great! As expected of a pro-surfer!"
    show oso Swim 01 Neutral at pos7 with Dissolve(0.05)
    oso "Ah, there's someone riding that wave right now! See, he looks perfectly—"

    # SOUND: Wave sounds/probably splash
    play music "music/a murder case.mp3" fadeout 2.0 fadein 2.0
    
    play audio "sfx/splash01.ogg"

    show oso Swim 01 Neutral Fade at pos7 with Dissolve(0.1)
    mystery "Natsume—!! He's drowning!! Someone, call an ambulance!!" 
    show oso Swim 01 Blank1 Fade at pos7 with Dissolve(0.1)
    mystery "...H-He's dead!!"
    hide oso
    show kara Swim 01 Blank1 at pos1 with Dissolve(0.05)
    show choro Swim 01 Blank1 at pos2 with Dissolve(0.05)
    show ichi Swim 01 Blank1 at pos4 with Dissolve(0.05)
    show todo Swim 01 Blank1 at pos5 with Dissolve(0.05)
    show jyushi Swim 01 Blank1 at pos6 with Dissolve(0.05)
    everyone "..."
    hide kara
    hide choro
    hide ichi
    hide todo
    hide jyushi
    show oso Swim 01 Nervous at pos7 with Dissolve(0.05)
    oso "...S-See?"
    hide oso
    show oso Swim 01 Nervous Fade Flip at pos3 with Dissolve(0.1)
    show choro Swim 01 Angry1 at pos4 with Dissolve(0.05)
    show todo Swim 01 Angry1 Fade at pos5 with Dissolve(0.1)
    choro "{size=+10}{b}WHAT DO YOU MEAN, \"SEE?!\" THAT GUY JUST DIED!!!{/b}{/size}"
    show oso Swim 01 Nervous Fade Flip at pos3 with Dissolve(0.1)
    show choro Swim 01 Angry1 Fade at pos4 with Dissolve(0.1)
    show todo Swim 01 Angry1 at pos5 with Dissolve(0.05)
    todo "{size=+10}{b}AND HE WAS A PRO!!! THERE'S NO WAY I'M RIDING THAT!!!{/b}{/size}"
    hide oso
    hide choro
    hide todo
    show ichi Swim 01 Nervous Flip at pos3 with Dissolve(0.05)
    show jyushi Swim 01 Surprised at pos6 with Dissolve(0.05)
    suuji "Scary... Surfing is scary..."
    hide ichi
    hide jyushi
    show kara Swim 01 Nervous at pos7 with Dissolve(0.05)
    kara "M-Maybe we could try a smaller wave first, Iyami?"
    hide kara
    show iyami Regular Angry1 at pos7 with Dissolve(0.05)
    iyami "You cowards!!"
    hide iyami
    show oso Swim 01 Surprised at pos1 with Dissolve(0.05)
    show choro Swim 01 Surprised at pos2 with Dissolve(0.05)
    show kara Swim 01 Surprised at pos3 behind choro
    show ichi Swim 01 Shocked1 at pos4 with Dissolve(0.05)
    show todo Swim 01 Surprised at pos5 with Dissolve(0.05)
    show jyushi Swim 01 Shocked1 at pos6 with Dissolve(0.05)
    everyone "Eh?!"
    hide oso
    hide choro
    hide kara
    hide ichi
    hide todo
    hide jyushi
    show iyami Regular Displeased1 at pos7 with Dissolve(0.05)
    iyami "As me thought, none of you are worthy of the way of the board."
    show iyami Regular Displeased1 at pos7 with Dissolve(0.05)
    iyami "Me was going to give you a chance, but you have only wasted my time, zansu!"
    show iyami Regular Displeased1 at pos7 with Dissolve(0.05)
    iyami "Farewell, zansu."
    hide iyami
    show oso Swim 01 Surprised at pos1 with Dissolve(0.05)
    show choro Swim 01 Surprised at pos2 with Dissolve(0.05)
    show kara Swim 01 Surprised at pos3 behind choro
    show ichi Swim 01 Shocked1 at pos4 with Dissolve(0.05)
    show todo Swim 01 Surprised at pos5 with Dissolve(0.05)
    show jyushi Swim 01 Surprised at pos6 with Dissolve(0.05)
    everyone "{size=+10}{b}W-Wait—!{/b}{/size}"
    hide oso
    hide choro
    hide kara
    hide ichi
    hide todo
    hide jyushi
    show oso Swim 01 Sad at pos7 with Dissolve(0.05)
    oso "I-Iyami..."
    show oso Swim 01 Angry3 at pos7 with Dissolve(0.05)
    oso "We're sorry. Please, teach us how to surf!"
    hide oso
    show oso Swim 01 Angry3 at pos1 with Dissolve(0.05)
    show choro Swim 01 Angry3 at pos2 with Dissolve(0.05)
    show kara Swim 01 Angry3 at pos3 with Dissolve(0.05)
    show ichi Swim 01 Angry2 at pos4 with Dissolve(0.05)
    show todo Swim 01 Displeased1 at pos5 with Dissolve(0.05)
    show jyushi Swim 01 Thinking at pos6 with Dissolve(0.05)
    everyone "Please!"
    hide oso
    hide choro
    hide kara
    hide ichi
    hide todo
    hide jyushi
    show iyami Regular Neutral at pos7 with Dissolve(0.05)
    iyami "..."
    show iyami Regular Happy1 at pos7 with Dissolve(0.05)
    iyami "You all better be prepared!"
    hide iyami
    show oso Swim 01 Happy1 at pos1 with Dissolve(0.05)
    show choro Swim 01 Happy1 at pos2 with Dissolve(0.05)
    show kara Swim 01 Happy1 at pos3 with Dissolve(0.05)
    show ichi Swim 01 Happy1 at pos4 with Dissolve(0.05)
    show todo Swim 01 Happy1 at pos5 with Dissolve(0.05)
    show jyushi Swim 01 Happy1 at pos6 with Dissolve(0.05)
    everyone "....!!"
    hide screen calendar
    scene bg_black with fade
    
    mystery "Whoa, this board sure can hold all six of us!"
    mystery "Watch where you're touching, Todomatsu!"
    mystery "B-But I'm afraid of falling!"
    mystery "YAY!!! WE'RE SURFING!!!"
    mystery "I could get used to this..."
    mystery "I-Is that a huge wave coming at us?!"
    mystery "TURN LEFT!"
    mystery "HOW DO YOU TURN THIS THING?!"
    mystery "IT'S COMING!!!"
    mystery "DO WE JUMP OFF-”"
    mystery "TODOMATSU STOP GRABBING MY-”"
     
    play audio "sfx/splash01.ogg"
     
    mystery "A-AAAGHHH!!!"
     
    stop music
    
    play audio ["<silence 1.0>","sfx/dead01.ogg"]
    
    scene cgi_beach with fade
    show screen calendar
    chibita "O-Oi Iyami... This is bad!"
    iyami "Me sees that. "
    iyami "Any witnesses?"
    chibita "Not yet... But someone's bound to walk by and see these corpses sooner or later!"
    iyami "C-C-Calm down, zansu! We have to stay calm!"
    chibita "What do you mean \"we\"?! You're the one shaking all over!"
    iyami "Me thinks it's these sextuplet's spirits haunting me, zansu..."
    chibita "Forget that for now, Iyami! We need to do something about their bodies!"
    iyami "Me knows that, zansu! Here, take this shovel and start digging!"
    chibita "Why do you have these shovels so handy?!"
    iyami "...Me was hoping to dig for treasure, not graves."
    
    stop audio
    
    hide screen calendar
    scene bg_black with fade
    
    play music "music/dogeza.ogg" fadeout 2.0 fadein 2.0
    
    dev "Thanks for playing the demo!"
    dev "See you guys in October for the full game!"
    dev "Be sure to visit our {a=https://twitter.com/OsosanDiscord}twitter{/a} and {a=https://cansextupletsgraduate-game.tumblr.com/}tumblr{/a}!"
    dev "We hope to see you again soon!" 
    
    return
