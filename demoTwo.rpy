label demoTwo:
        
    scene bg_hallway with fade
    
    show screen calendar
    $changeDate("JUL",18,"MORNING")
    
    show choro SchoolS 02 Nervous at pos7
    choro "We..."
    hide choro
    show todo SchoolS 02 Nervous at pos7
    todo "Barely..."
    hide todo
    show oso SchoolS 02 Happy1 at pos7
    oso "—PASSED!!!"
    show oso SchoolS 03 Happy1 at pos7
    oso "Ha! Told ya I'd be fine!"
    hide oso
    show ichi SchoolS 02 Angry2 at pos7
    ichi "Tch... I owe Todomatsu 500 yen..."
    hide ichi
    show oso SchoolS 03 Neutral Flip at pos3
    #show ichi SchoolS 02 Angry2 Fade at pos7
    oso "What was that?"
    show oso SchoolS 03 Neutral Fade Flip at pos3
    show jyushi SchoolS 03 Nervous at pos6
    jyushi "Nothing!"
    show oso SchoolS 03 Neutral Fade Flip at pos3
    show jyushi SchoolS 03 Happy1 at pos6
    jyushi "Ahaha! Let's get ready for summer!"
    show oso SchoolS 01 Happy1 Flip at pos3
    show jyushi SchoolS 03 Happy1 Fade at pos6
    oso "Oh... Haha. That's the spirit, Jyushimatsu!"
    hide oso
    hide jyushi
    hide ichi
    
    scene bg_lr_daytime with fade
    
    $changeDate("JUL",22,"AFTERNOON")
    
    #play music "music/dogeza.mp3" fadeout 2.0 fadein 2.0
    
    show oso Maintee 03 Sad Flip at pos3
    show kara Maintee 01 Neutral Fade at pos6
    oso "Ugh..."
    oso "The heat..."
    show oso Maintee 01 Sad Flip at pos3
    show kara Maintee 01 Neutral Fade at pos6
    oso "Karamatsu, can you pass the shaved ice?"
    show oso Maintee 01 Sad Fade Flip at pos3
    show kara Maintee 01 Neutral at pos6
    kara "Here you go, Osomatsu."
    show oso Maintee 01 Neutral Flip at pos3
    show kara Maintee 01 Neutral Fade at pos6
    oso "Aha, Thanks! This tastes really good!"
    show oso Maintee 01 Neutral Fade Flip at pos3
    show kara Maintee 01 Happy1 at pos6
    kara "Heh. Of course it does, my brother. I poured all my passion into it, after all."
    show oso Maintee 01 Blank1 Flip at pos3
    show kara Maintee 01 Happy1 Fade at pos6
    oso "More like you poured all your sweat into it."
    hide oso
    hide kara
    show ichi Maintee 01 Neutral Flip at pos3
    show jyushi Maintee 01 Displeased1 Fade at pos6
    ichi "Time's up, Jyushimatsu. It's my turn to use the fan now."
    show ichi Maintee 01 Neutral Fade Flip at pos3
    show jyushi Maintee 01 Shocked1 at pos6
    jyushi "But! It's so hot!"
    show ichi Maintee 02 Angry2 Flip at pos3
    show jyushi Maintee 01 Shocked1 Fade at pos6
    ichi "You've hogged it for an hour. Can't you share?"
    show ichi Maintee 02 Angry2 Fade Flip at pos3
    show jyushi Maintee 01 Angry1 at pos6
    jyushi "I need air conditioning!"
    show ichi Maintee 01 Gasp Flip at pos3
    show jyushi Maintee 01 Angry1 Fade at pos6
    ichi "C-Calm down, Jyushimatsu—"
    
    #SFX: Crunching Sound
    #play sound ""
    
    show ichi Maintee 01 Gasp Fade Flip at pos3
    show jyushi Maintee 03 Angry1 at pos6
    jyushi "{size=+10}{b}AIR CONDITIONING!!!{/b}{/size}" with scrShake
    show ichi Maintee 01 Shocked1 Flip at pos3
    show jyushi Maintee 03 Angry1 Fade at pos6
    ichi "—?!"
    show ichi Maintee 01 Nervous Flip at pos3
    show jyushi Maintee 03 Angry1 Fade at pos6
    ichi "D-Did you just eat three whole popsicles in one bite?"
    show ichi Maintee 01 Nervous Fade Flip at pos3
    show jyushi Maintee 03 Angry1 Fade at pos4
    show choro Maintee 01 Angry3 at pos5
    choro "You know, you could just use a hand fan instead..."
    hide ichi
    hide jyushi
    show oso Maintee 03 Blank1 Flip at pos3
    show choro Maintee 01 Angry3 Fade at pos6
    oso "Hot sure is summer..."
    show oso Maintee 03 Blank1 Fade Flip at pos3
    show choro Maintee 01 Blank1 at pos6
    choro "Don't you mean, \"summer sure is hot?\""
    show oso Maintee 03 Nervous Flip at pos3
    show choro Maintee 01 Blank1 Fade at pos6
    oso "Ah... The brain's really messing with my heat."
    show oso Maintee 03 Surprised Flip at pos3
    show choro Maintee 01 Blank1 Fade at pos6
    oso "Gahh!! It's sooooo hot!"
    show oso Maintee 01 Shocked1 Flip at pos3
    show choro Maintee 01 Blank1 Fade at pos6
    oso "And I'm sooooo bored..."
    show oso Maintee 01 Angry5 Flip at pos3 
    show choro Maintee 01 Blank1 Fade at pos6
    oso "Can't summer be more exciting?!"
    hide choro
    show oso Maintee 01 Angry5 Fade Flip at pos3
    show todo Maintee 01 Angry1 at pos6
    todo "Ahh, geez! Osomatsu-niisan, will you shut up already?!"
    show oso Maintee 01 Angry5 Fade Flip at pos3
    show todo Maintee 01 Displeased1 at pos6
    todo "If you stopped moving around so much, you wouldn't feel as hot."
    hide oso
    hide todo
    show oso Maintee 01 Sad at pos7
    oso "Doesn't anyone else here feel bored?"
    show oso Maintee 01 Angry5 at pos7
    oso "It's only the third day of summer, and I'm already dying of boredom!"
    show oso Maintee 01 Blank1 Fade at pos7
    rest "... {i}There is silence for a while.{/i}"
    show oso Maintee 01 Displeased1 at pos7
    oso "{i}Everyone's ignoring me, huh.{/i}"
    show oso Maintee 02 Happy1 at pos7
    oso "Oh!"
    show oso Maintee 02 Neutral at pos7
    oso "Why don't we all go to the beach?"
    
    scene bg_beach with fade
    
    $changeDate("JUL",25,"MORNING")
    
    play music "music/tell me hatabou.mp3" fadeout 2.0 fadein 2.0
    
    show kara Swim 01 Surprised at pos7
    kara "Oh my! Whatever is this lovely maiden doing, lying unconsious on the shore?"
    show kara Swim 02 Thinking at pos7
    kara "As the prince of this kingdom, it is my sworn duty to ensure that no harm befalls any of my loyal subjects."
    show kara Swim 02 Displeased1 at pos7
    kara "It would be especially tragic to lose one of those that have graced this Earth with such divine beauty..."
    show kara Swim 03 Shocked1 at pos7
    kara "Oh! You're as cold as death..."
    show kara Swim 03 Sad at pos7
    kara "Come, let us hurry you back to the castle."
    show kara Swim 03 Gasp at pos7
    kara "My, how light you are... It is as if I am caressing a cloud, or perhaps a ghost from a dream... Your eyes remain closed, yet I feel as if you are gazing into my very core with tender, uncertain yearning..."
    
    # Sound: BONE SNAPPING SOUND
    #play sound ""
    
    show kara Swim 01 Angry1 at pos7
    kara "AHHH!!! OW, OW, OW!!! IT'S PINCHING ME!!! GET IT OFF!!! GET IT OFF!!!"
    hide kara
    show choro Swim 01 Nervous Flip at pos3
    show kara Swim 01 Angry1 Fade at pos6
    choro "Ah—! Karamatsu-niisan!"
    show choro Swim 01 Nervous Fade Flip at pos3
    show kara Swim 01 Shocked1 at pos6
    kara "Phew..."
    show choro Swim 01 Nervous Fade Flip at pos3
    show kara Swim 01 Blank1 at pos6
    kara "I thought I was going to die..."
    show choro Swim 01 Nervous Fade Flip at pos3
    show kara Swim 01 Happy1 at pos6
    kara "Thank you for getting rid of that crab, Choromatsu."
    show choro Swim 01 Displeased3 Flip at pos3
    show kara Swim 01 Happy1 Fade at pos6
    choro "What the hell were you doing...?"
    show choro Swim 01 Displeased3 Flip at pos3
    show kara Swim 01 Happy1 Fade at pos6
    choro "Talking like that to a crab..."
    show choro Swim 01 Displeased3 Fade Flip at pos3
    show kara Swim 02 Neutral at pos6
    kara "I was trying to improve my acting."
    show choro Swim 01 Displeased3 Fade Flip at pos3
    show kara Swim 02 Displeased2 at pos6
    kara "Since I failed in obtaining the lead role..."
    hide choro
    show oso Swim 01 Neutral Flip at pos3
    show kara Swim 02 Displeased2 Fade at pos6
    oso "Nyahahaha! Your acting was really funny, Karamatsu!"
    show oso Swim 01 Happy1 Flip at pos3
    show kara Swim 02 Displeased2 Fade at pos6
    oso "Haaa, I haven't laughed this hard in a while!"
    show oso Swim 01 Happy1 Fade Flip at pos3
    show kara Swim 02 Nervous at pos6
    kara "You were watching the whole time?!"
    show oso Swim 01 Neutral Flip at pos3
    show kara Swim 02 Nervous Fade at pos6
    oso "Yup!"
    show oso Swim 01 Neutral Fade Flip at pos3
    show kara Swim 03 Nervous at pos6
    kara "W-Why didn't you help me with the crab?"
    show oso Swim 03 Happy1 Flip at pos3
    show kara Swim 03 Nervous Fade at pos6
    oso "Because it was way too funny!"
    show oso Swim 03 Happy1 Fade Flip at pos3
    show kara Swim 03 Nervous at pos6
    kara "I... I see. Well, nevermind that."
    show oso Swim 03 Happy1 Fade Flip at pos3
    show kara Swim 03 Nervous at pos6
    kara "W-What did you think of my acting?"
    show oso Swim 03 Gasp Flip at pos3
    show kara Swim 03 Nervous Fade at pos6
    oso "Oh, um..."
    
    
    menu:
        
        "It was so bad, it was funny!":
   
            show oso Swim 03 Happy1 Flip at pos3
            show kara Swim 03 Nervous Fade at pos6
            oso "You'd be a hit playing the butt of the joke! Ahaha!"
            
        "You have a lotta potential!":
            show oso Swim 03 Neutral Flip at pos3
            show kara Swim 03 Nervous Fade at pos6
            oso "Just keep practicing and you'll be able to get the lead role one day!"
            show oso Swim 03 Neutral Flip at pos3
            show kara Swim 03 Nervous Fade at pos6
            oso "Trust me! I'm your older brother, after all."
        
            
        "It looked natural, I guess.":
            show oso Swim 03 Happy1 Flip at pos3
            show kara Swim 03 Nervous Fade at pos6
            oso "I think it suits you!"
            show oso Swim 03 Thinking Flip at pos3
            show kara Swim 03 Nervous Fade at pos6
            oso "But it's not like I know much about acting in the first place."
    
    
    show oso Swim 03 Neutral Fade Flip at pos3
    show kara Swim 01 Gasp at pos6
    kara "I see..."
    show oso Swim 03 Neutral Fade Flip at pos3
    show kara Swim 01 Neutral at pos6
    kara "Thanks for the feedback, Osomatsu."
    show oso Swim 03 Neutral Fade Flip at pos3
    show kara Swim 01 Neutral Fade at pos4
    show choro Swim 03 Neutral at pos5
    choro "You should have more confidence in yourself, Karamatsu-niisan."
    show oso Swim 03 Neutral Fade Flip at pos3
    show kara Swim 01 Neutral Fade at pos4
    show choro Swim 03 Happy2 at pos5
    choro "After all, didn't you join the drama club because you enjoyed their performance at the cultural festival?"
    show oso Swim 03 Neutral Fade Flip at pos3
    show kara Swim 01 Displeased2 at pos4
    show choro Swim 03 Happy2 Fade at pos5
    kara "Ah... That's true."
    show oso Swim 03 Displeased1 Flip at pos3
    show kara Swim 01 Displeased2 Fade at pos4
    show choro Swim 03 Happy2 Fade at pos5
    oso "It's nothing to be stressed about. "
    show oso Swim 03 Neutral Flip at pos3
    show kara Swim 01 Displeased2 Fade at pos4
    show choro Swim 03 Neutral Fade at pos5
    oso "Right now, we're here to enjoy summer!"
    show oso Swim 03 Displeased1 Flip at pos3
    show kara Swim 01 Displeased2 Fade at pos4
    show choro Swim 03 Neutral Fade at pos5
    oso "But it's pretty disappointing to see that there aren't many people here..."
    show oso Swim 03 Angry1 Flip at pos3
    show kara Swim 01 Displeased2 Fade at pos4
    show choro Swim 03 Neutral Fade at pos5
    oso "...And it's all old people! What the hell?!"
    show oso Swim 03 Angry2 Flip at pos3
    show kara Swim 01 Displeased2 Fade at pos4
    show choro Swim 03 Neutral Fade at pos5
    oso "I don't wanna see some grandpa's back."
    show oso Swim 03 Angry2 Fade Flip at pos3
    show kara Swim 01 Displeased2 Fade at pos4
    show choro Swim 01 Blank1 at pos5


    choro "{i}Choromatsu shifts his gaze farther up the beach, to an umbrella where the younger three brothers were gathered.{/i}"
    choro "At least everyone else looks like they're enjoying themselves."
    hide kara
    hide choro
    show jyushi Swim 03 Neutral Flip at pos3
    hide oso
    show todo Swim 01 Neutral Fade at pos4
    show ichi Swim 01 Neutral Fade at pos5
    jyushi "YAHOOOO!"
    show jyushi Swim 03 Neutral Fade Flip at pos3
    show todo Swim 03 Nervous at pos4
    show ichi Swim 01 Neutral Fade at pos5
    todo "Jyushimatsu-niisan, wait! You need to put some sunscreen on first!"
    show jyushi Swim 03 Neutral Fade Flip at pos3
    show todo Swim 03 Nervous at pos4
    show ichi Swim 01 Neutral Fade at pos5
    todo "Don't just run off like that..."
    show jyushi Swim 03 Neutral Fade Flip at pos3
    show todo Swim 03 Surprised at pos4
    show ichi Swim 01 Neutral Fade at pos5
    todo "Ah, geez! Jyushimatsu-niisan is so energetic."
    hide jyushi
    show todo Swim 03 Surprised at pos4
    show ichi Swim 01 Neutral Fade at pos5
    todo "It's hard to keep up with his pace."
    show todo Swim 03 Surprised Fade at pos4
    show ichi Swim 01 Happy1 at pos5
    ichi "Mm... Yeah."
    show todo Swim 01 Happy1 at pos4
    show ichi Swim 01 Happy1 Fade at pos5
    todo "Ahh, whatever! I'm just going to relax under this shade~"
    show todo Swim 01 Happy1 Fade at pos4
    show ichi Swim 01 Angry2 at pos5
    ichi "You're just gonna lie there...?"
    show todo Swim 01 Happy1 at pos4
    show ichi Swim 01 Angry2 Fade at pos5
    todo "Hmm... Yep! Call me when the watermelon splitting game starts."
    show todo Swim 01 Happy1 Fade at pos4
    show ichi Swim 01 Angry2 at pos5
    ichi "Eh..."
    show oso Swim 02 Happy1 Flip at pos3
    show todo Swim 01 Blank1 Fade at pos4
    show ichi Swim 01 Neutral Fade at pos5
    oso "Yo, Ichimatsu~! Todomatsu~!"
    hide ichi
    show choro Swim 02 Displeased3 Flip at pos1
    show oso Swim 02 Happy1 Fade Flip at pos2
    hide todo
    show todo Swim 01 Blank1 Fade at pos5
    choro "Oh, you two aren't going to play in the water? Not even on the shore?"
    show choro Swim 02 Displeased3 Fade Flip at pos1
    show oso Swim 02 Neutral Fade Flip at pos2
    hide todo
    show kara Swim 01 Neutral at pos6
    kara "Let's just sit down and relax, Choromatsu."
    hide kara
    
    stop music fadeout 2.0
    
    show choro Swim 02 Neutral Fade Flip at pos1
    show oso Swim 02 Neutral Fade Flip at pos2
    show kara Swim 01 Neutral at pos4
    kara "Ah, this is quite a comfortable rock. Softer than any other rock I've ever sat on."
    show choro Swim 02 Blank1 Fade Flip at pos1
    show oso Swim 02 Blank1 Fade Flip at pos2
    show kara Swim 01 Blank1 at pos4
    kara "Hm...? Did you guys hear that?"
    show choro Swim 02 Blank1 Fade Flip at pos1
    show oso Swim 02 Blank1 Fade Flip at pos2
    show kara Swim 01 Blank1 Fade at pos4
    show choro Swim 02 Blank1 Fade Flip at pos1
    show oso Swim 02 Blank1 Fade Flip at pos2
    show kara Swim 01 Surprised at pos6
    mystery "MMRHGRHGRH!!!"
    show ichi Swim 01 Thinking at pos5
    ichi "I think it's coming from that rock..."
    show choro Swim 01 Nervous Flip at pos1
    show oso Swim 02 Blank1 Fade Flip at pos2
    show kara Swim 01 Blank1 Fade at pos4
    show ichi Swim 01 Thinking Fade at pos5
    choro "Wait a second..."
    show choro Swim 01 Nervous Fade Flip at pos1
    show oso Swim 02 Happy1 Flip at pos2
    show kara Swim 01 Blank1 Fade at pos4
    hide ichi
    oso "Ahahahaha!! Karamatsu! You're sitting on Chibita!"
    show choro Swim 01 Nervous Fade Flip at pos1
    show oso Swim 02 Happy1 Fade Flip at pos2
    show kara Swim 01 Gasp at pos4
    kara "E-EH?!"
    hide choro
    hide oso
    hide kara
    
    chibita "{size=+10}{b}GET OFF, YA IDJIT!!!{/b}{/size}" with scrShake
    chibita "WHAT THE HELL!!! I WAS JUST RELAXING IN THE SAND—"
    chibita "—AND YOU COME OVER AND SUFFOCATE ME WITH YOUR ASS?!"
    chibita "CAN'T I ENJOY MY SUMMER BREAK IN PEACE?! DAMN IT!!!"
    chibita "Ah."
    chibita "It's you guys."
    
    #replace with dogeza
    play music "music/dozikkomarch.mp3" fadeout 2.0 fadein 2.0
    
    show ichi Swim 01 Neutral Fade Flip at pos1
    show oso Swim 02 Neutral Flip at pos2
    show choro Swim 02 Neutral Fade at pos6
    oso "Hey, Chibita!"
    show ichi Swim 01 Neutral Fade Flip at pos1
    show oso Swim 02 Neutral Fade Flip at pos2
    show choro Swim 02 Blank1 at pos6
    choro "Uhh... Why exactly were you buried in the sand up to your neck like that...?"
    show ichi Swim 01 Neutral Fade Flip at pos1
    show oso Swim 02 Neutral Fade Flip at pos2
    show choro Swim 02 Blank1 Fade at pos6
    chibita "Hah? Iyami told me that I'd grow taller if I planted myself in the sand."
    show ichi Swim 01 Neutral Fade Flip at pos1
    show oso Swim 02 Neutral Fade Flip at pos2
    show choro Swim 02 Displeased3 at pos6
    choro "And you believed him...?"
    show ichi Swim 01 Neutral Fade Flip at pos1
    show oso Swim 01 Happy1 Flip at pos2
    show choro Swim 02 Displeased3 Fade at pos6
    oso "Gyahahaha! How dumb can you be?!"
    show ichi Swim 01 Neutral Fade Flip at pos1
    show oso Swim 01 Neutral Flip at pos2
    show choro Swim 02 Displeased3 Fade at pos6
    oso "Chibita... Being small is kinda your thing. If you were tall, you wouldn't be Chibita anymore. "
    show ichi Swim 03 Gasp Flip at pos1
    show oso Swim 01 Neutral Fade Flip at pos2
    show choro Swim 02 Displeased3 Fade at pos6
    ichi "If Iyami told you that... Doesn't that mean he's here too? "
    hide ichi
    hide oso
    hide choro
    iyami "Uhyohyohyo!"
    iyami "This will be me's most genius plan ever! "
    show oso Swim 02 Surprised at pos4
    oso "Eh? Iyami? "
    show oso Swim 02 Surprised Fade at pos4
    iyami "SEXTUPLETS?!"
    show oso Swim 02 Surprised Fade at pos4
    iyami "What are you brats doing here?"
    show oso Swim 02 Gasp at pos4
    oso "Huh? We should be the ones asking you that. "
    hide oso
    show ichi Swim 03 Displeased1 at pos4
    ichi "You're planning another scam, huh?"
    show ichi Swim 03 Displeased1 Fade at pos4
    iyami "It's not a scam, zansu. "
    show ichi Swim 03 Displeased1 Fade at pos4
    iyami "Me is just earning some side cash aside from me's job."
    hide ichi
    show jyushi Swim 01 Happy1 at pos4
    jyushi "You have a job?!"
    show jyushi Swim 01 Happy1 Fade at pos4
    iyami "Me sells bread at your school, zansu."
    hide jyushi
    show oso Swim 02 Gasp at pos4
    oso "What? You work at our school?"
    show oso Swim 02 Gasp Fade at pos4
    iyami "SHEEEH!!! You don't even remember?!"
    show oso Swim 02 Gasp Fade at pos4
    show choro Swim 02 Displeased1 at pos5
    choro "Come on, Osomatsu-niisan. Let's go somewhere else."
    show oso Swim 02 Gasp Fade at pos4
    show choro Swim 02 Displeased1 Fade at pos5
    show kara Swim 02 Displeased1 at pos7
    kara "Best to leave the man alone."
    show oso Swim 02 Gasp Fade at pos4
    show choro Swim 02 Displeased1 Fade at pos5
    show kara Swim 02 Displeased1 Fade at pos7
    iyami "W-Wait! What if me tells you something you could do!"
    show oso Swim 01 Neutral at pos4
    show choro Swim 02 Displeased1 Fade at pos5
    show kara Swim 02 Displeased1 Fade at pos7
    oso "...I'm listening. You guys go on ahead, I'm gonna stay here and be unbored."
    hide kara
    hide choro
    show oso Swim 01 Neutral Fade at pos4
    show kara Swim 01 Displeased1 Fade Flip at pos2
    show choro Swim 01 Displeased3 at pos5
    choro "\"Unbored\" isn't a—"
    show kara Swim 03 Happy1 Flip at pos2
    show choro Swim 01 Displeased3 Fade at pos5
    kara "Let's go, Choromatsu. May I rub sunscreen on your back?"
    show kara Swim 03 Happy1 Fade Flip at pos2
    show choro Swim 01 Thinking at pos5
    choro "Ah, fine... It'll give me a chance to read a bit of {i}No Longer Human{/i}, anyway."
    hide kara
    hide choro
    show oso Swim 01 Neutral at pos4
    oso "So what's this \"something\" you've got for me to do."
    show oso Swim 01 Neutral Fade at pos4
    iyami "Me is teaching people how to surf, zansu."
    oso "But there's barely anyone here. Just a bunch of old geezers..."
    oso "Can you actually teach people?"
    show oso Swim 03 Displeased1 at pos4
    iyami "Trust me, zansu. "
    show oso Swim 03 Sad at pos4
    iyami "For a small price, me can teach you how to battle the waves."
    show oso Swim 03 Sad Fade at pos4
    oso "How much?"
    show oso Swim 03 Sad Fade at pos4
    iyami "2,000 yen per person for two hours."
    show oso Swim 03 Gasp at pos4
    oso "Hmm, how about... 1,000 yen per person for one hour?"
    show oso Swim 03 Gasp Fade at pos4
    oso "Like, a sextuplet discount! "
    show oso Swim 03 Thinking at pos4
    iyami "Hm... "
    show oso Swim 03 Happy1 at pos4
    oso "Come on, Iyami! We've known each other for a while—at least give us a discount!"
    show oso Swim 03 Happy1 Fade at pos4
    iyami "Hm..."
    show oso Swim 01 Angry2 Fade at pos4
    oso "Geez! If you're not gonna lower the price, I'm out! "
    show oso Swim 01 Angry5 at pos4
    iyami "SHEEEH!!! You're so annoying!"
    show oso Swim 01 Angry5 Fade at pos4
    iyami "Fine! 10,000 yen for the six of you and 6,000 yen for one big surfboard."
    show oso Swim 01 Angry5 Fade at pos4
    iyami "That's my deal, zansu."
    show oso Swim 01 Angry5 Fade at pos4
    oso "Why one?"
    show oso Swim 03 Gasp at pos4
    iyami "Well, would you rather pay for six surfboards?"
    show oso Swim 03 Gasp Fade at pos4
    iyami "Besides, six people on one surfboard balances it better."
    show oso Swim 03 Gasp Fade at pos4
    oso "You've got a point there..."
    show oso Swim 03 Thinking at pos4
    oso "Alright, I'll take it."
    show oso Swim 03 Happy1 at pos4
    iyami "That'll be 1,000 yen extra."
    show oso Swim 03 Happy1 Fade at pos4
    oso "Eh?! Why?!"
    show oso Swim 03 Angry3 at pos4
    iyami "You have to make an appointment, so if you pay now for a slot, you won't have to wait long."
    show oso Swim 03 Angry3 Fade at pos4
    oso "Who the hell are you even teaching here?!"
    show oso Swim 03 Angry2 at pos4
    iyami "You want the deal or not, zansu? "
    show oso Swim 03 Angry2 Fade at pos4
    oso "Tch... Fine, whatever. Stingy."
    show oso Swim 01 Angry4 at pos4
    oso "{i}I can't believe I'm going through all this trouble just to get my brothers to play with me...{/i}"
    show oso Swim 01 Angry3 at pos4
    oso "{i}This better be worth it.{/i}"
    show oso Swim 01 Sad at pos4

    $changeDate("JUL",25,"AFTERNOON")
    
    # BGM TBD
    #play music "music/dozikkomarch.mp3" fadeout 2.0 fadein 2.0

    show oso Swim 02 Neutral Flip at pos2
    hide todo
    oso "Hey, guys! Guess what?"
    show oso Swim 02 Neutral Fade Flip at pos2
    show todo Swim 01 Blank1 at pos4
    todo "Found some cliff for us to jump off of?"
    show oso Swim 02 Neutral Fade Flip at pos2
    show todo Swim 01 Thinking at pos4
    todo "I'm sure Ichimatsu-niisan would like that."
    show oso Swim 02 Neutral Fade Flip at pos2
    show todo Swim 01 Thinking Fade at pos4
    show ichi Swim 01 Happy1 at pos5
    ichi "Finally... Bring me there."
    show oso Swim 01 Blank1 Flip at pos2
    show todo Swim 01 Thinking Fade at pos4
    show ichi Swim 01 Happy1 Fade at pos5
    oso "What? No, no, it's something else."
    show oso Swim 01 Blank1 Fade Flip at pos2
    show todo Swim 01 Neutral Fade at pos4
    show ichi Swim 01 Thinking at pos5
    ichi "Oh."
    hide todo
    hide ichi
    show oso Swim 01 Blank1 Fade Flip at pos2
    show jyushi Swim 01 Happy1 at pos4
    show kara Swim 01 Happy1 Fade at pos5
    jyushi "Want some watermelon, Osomatsu-niisan?"
    show oso Swim 01 Blank1 Fade Flip at pos2
    show jyushi Swim 01 Happy1 Fade at pos4
    show kara Swim 01 Happy1 at pos5
    kara "We saved you a slice."
    show oso Swim 01 Happy1 Flip at pos2
    show jyushi Swim 01 Happy1 Fade at pos4
    show kara Swim 01 Happy1 Fade at pos5
    oso "No thanks, I found something fun for us to do!"
    show oso Swim 01 Neutral Flip at pos2
    show jyushi Swim 01 Happy1 Fade at pos4
    show kara Swim 01 Happy1 Fade at pos5
    oso "It'll be one of those \"wild high school memories\" we can look back on and laugh about when we get older!"
    show oso Swim 01 Happy1 Flip at pos2
    show jyushi Swim 01 Happy1 Fade at pos4
    show kara Swim 01 Happy1 Fade at pos5
    oso "We're going surfing!"
    show oso Swim 01 Thinking Flip at pos2
    show jyushi Swim 01 Happy1 Fade at pos4
    show kara Swim 01 Happy1 Fade at pos5
    oso "...And Iyami will be teaching us how. "
    hide jyushi
    show oso Swim 01 Thinking Fade Flip at pos2
    show choro Swim 01 Blank1 at pos4
    hide kara
    choro "Surfing?"
    show oso Swim 01 Thinking Fade Flip at pos2
    show choro Swim 01 Displeased3 at pos4
    choro "We barely come here... What good would learning how to surf do us?"
    show oso Swim 02 Neutral Flip at pos2
    show choro Swim 01 Displeased3 Fade at pos4
    oso "But that's the point! That's why we should jump on this opportunity."
    show oso Swim 02 Neutral Flip at pos2
    show choro Swim 01 Displeased3 Fade at pos4
    oso "No time like the present, right? Let's make these memories while we still have the chance!"
    show oso Swim 01 Gasp Flip at pos2
    show choro Swim 01 Displeased3 Fade at pos4
    oso "Plus, I already begged Dad for the money, so we might as well."
    hide oso
    hide choro
    show kara Swim 01 Displeased1 Flip at pos1
    show choro Swim 01 Angry2 Flip at pos2
    show jyushi Swim 01 Displeased1 at pos4
    show todo Swim 01 Displeased1 at pos5
    show ichi Swim 01 Displeased1 at pos7
    rest "Ugggghhh..."
    hide kara
    hide choro
    hide ichi
    hide jyushi
    hide todo
    show todo Swim 02 Displeased1 at pos4
    todo "Well, if Dad is already paying, then I guess I don't see the harm..."
    show kara Swim 02 Blank1 Flip at pos3
    show todo Swim 02 Displeased1 Fade at pos4
    kara "Oh? You're actually going to surf, Todomatsu?"
    show kara Swim 02 Blank1 Fade Flip at pos3
    show todo Swim 02 Thinking at pos4
    todo "I don't see why not. I can't lay around all day without getting bored."
    show kara Swim 02 Blank1 Fade Flip at pos3
    show todo Swim 01 Happy1 at pos4
    todo "So why not get \"on board\" too~"
    hide kara
    hide todo
    show jyushi Swim 01 Happy1 Flip at pos2
    show ichi Swim 01 Happy1 Fade at pos4
    jyushi "HAHAHA!!! Good one, Todomatsu!"
    show jyushi Swim 01 Happy1 Fade Flip at pos2
    show ichi Swim 01 Happy1 at pos4
    ichi "Heh... Sure, let's try this out."
    hide jyushi
    hide ichi
    show oso Swim 01 Neutral Fade Flip at pos2
    show choro Swim 02 Displeased3 at pos4
    choro "Alright, but we better watch the time. We should head back to Mom and Dad straight after so we can make it back to Uncle's village before dark."
    show oso Swim 01 Happy1 Flip at pos2
    show choro Swim 02 Displeased3 Fade at pos4
    oso "Yahoo! Surfing!"
    show oso Swim 01 Happy1 Fade Flip at pos2
    show choro Swim 02 Angry2 at pos4
    choro "Oi, hold on! Eat your share first, then head out. It's lunch time."
    show oso Swim 02 Neutral Flip at pos2
    show choro Swim 02 Angry2 Fade at pos4
    oso "Mmmm... Food~"
    hide oso
    hide choro
    show kara Swim 02 Neutral at pos7
    kara "Ah, there it is. The eldest and his love of food."
    hide kara
    show ichi Swim 01 Happy1 at pos7
    ichi "Gross."
    show ichi Swim 01 Happy1 at pos7
    jyushi "Osomatsu-niisan's gross! Ahahaha!"
    hide ichi
    show todo Swim 01 Happy1 at pos7
    todo "Yep, yep! He moves too much in his sleep too."
    hide todo
    show choro Swim 01 Happy2 at pos7
    choro "Glad I'm not the only one who thinks that. "
    hide choro
    show oso Swim 01 Angry4 at pos7
    oso "Hey! Why're you all so mean to Onii-chan?!"
    hide oso
    show oso Swim 01 Angry4 Fade Flip at pos2
    show todo Swim 02 Happy1 at pos4
    todo "You did say we needed to bond as a family, Nii-san."
    show oso Swim 02 Neutral Flip at pos2
    show todo Swim 02 Happy1 Fade at pos4
    oso "Fine... I'll take it."
    show oso Swim 02 Neutral Flip at pos2
    show todo Swim 02 Happy1 Fade at pos4
    oso "Thanks for the food!"
    hide todo
    
    # BEACH WAVES (probably sound looped instead of music)
    #play music "music/dozikkomarch.mp3" fadeout 2.0 fadein 2.0
    
    show oso Swim 03 Happy1 at pos4
    oso "Yo, Iyami!"
    show oso Swim 03 Happy1 Fade at pos4
    iyami "You're all late, zansu."
    show oso Swim 03 Happy1 Fade at pos4
    iyami "Hurry and start warming up!"
    hide oso
    show kara Swim 01 Displeased1 at pos4
    kara "What are we supposed to do?"
    show kara Swim 01 Displeased1 Fade at pos4
    iyami "For your training, you'll need to learn how to catch a wave, zansu. "
    hide kara
    show choro Swim 01 Displeased3 at pos4
    choro "And how do we do that? "
    show choro Swim 01 Displeased3 Fade at pos4
    iyami "Just shut your mouth and listen to me, zansu. "
    show choro Swim 01 Displeased3 Fade at pos4
    iyami "Now, let's start. Go and ride that wave."
    show choro Swim 01 Surprised Fade at pos4
    show todo Swim 01 Shocked1 at pos5
    todo "Eh—?! That huge one?! Now?!"
    show choro Swim 01 Surprised at pos4
    show todo Swim 01 Shocked1 Fade at pos5
    choro "Surely we have to start with some warm-ups first?!"
    hide choro
    show kara Swim 01 Nervous at pos4
    hide todo
    kara "Or perhaps start with trying to balance on the board on land at least?!"
    show kara Swim 01 Nervous Fade at pos4
    iyami "Shut up, zansu!"
    hide kara
    show oso Swim 01 Surprised Flip at pos1
    show choro Swim 01 Surprised Flip at pos2
    show kara Swim 01 Surprised Flip at pos3
    show ichi Swim 01 Shocked1 at pos4
    show todo Swim 01 Shocked1 at pos5
    show jyushi Swim 01 Shocked1 at pos6
    everyone "...?!"
    hide oso
    hide choro
    hide kara
    hide ichi
    hide todo
    hide jyushi
    iyami "Who do you think is the teacher here?!"
    iyami "It's me, zansu! So if I say to do something, you should just do it, zansu!!"
    show oso Swim 01 Nervous at pos7
    oso "C-Come on, guys! I mean, it'll probably be okay, right...?!"
    show oso Swim 01 Nervous Fade at pos7
    mystery "Wow, Natsume! You're doing great! As expected from a pro-surfer!"
    show oso Swim 01 Neutral at pos7
    oso "Ah, there's someone riding that wave right now! See, he looks perfectly—"
    show oso Swim 01 Blank1 Fade at pos7
    
    # SOUND: Wave sounds/probably splash
    #play music "music/dozikkomarch.mp3" fadeout 2.0 fadein 2.0
    
    mystery "Natsume—!! He's drowning!! Someone, call an ambulance!!"
    mystery "...H-He's dead!!"
    show oso Swim 01 Blank1 Flip at pos1
    show choro Swim 01 Blank1 Flip at pos2
    show kara Swim 01 Blank1 Flip at pos3
    show ichi Swim 01 Blank1 at pos4
    show todo Swim 01 Blank1 at pos5
    show jyushi Swim 01 Blank1 at pos6
    everyone "..."
    hide oso
    hide choro
    hide kara
    hide ichi
    hide todo
    hide jyushi
    oso "...S-See?"
    show oso Swim 01 Nervous Fade Flip at pos2
    show choro Swim 01 Angry1 at pos4
    choro "{size=+10}{b}WHAT DO YOU MEAN, \"SEE?!\" THAT GUY JUST DIED!!!{/b}{/size}" with scrShake
    show oso Swim 01 Nervous Fade Flip at pos2
    show choro Swim 01 Angry1 Fade at pos4
    show todo Swim 02 Angry1 at pos5
    todo "{size=+10}{b}AND HE WAS A PRO!!! THERE'S NO WAY I'M RIDING THAT!!!{/b}{/size}" with scrShake
    show ichi Swim 03 Nervous Flip at pos2
    show jyushi Swim 02 Surprised at pos4
    hide todo
    both "Scary... Surfing is scary..."
    hide jyushi
    hide ichi
    show kara Swim 03 Nervous at pos4
    kara "M-Maybe we could try a smaller wave first, Iyami?"
    hide kara
    iyami "You cowards!!!"
    show oso Swim 01 Surprised Flip at pos1
    show choro Swim 01 Surprised Flip at pos2
    show kara Swim 01 Surprised Flip at pos3
    show ichi Swim 01 Shocked1 at pos4
    show todo Swim 01 Surprised at pos5
    show jyushi Swim 01 Shocked1 at pos6
    everyone "Eh?!"
    hide oso
    hide choro
    hide kara
    hide ichi
    hide todo
    hide jyushi
    iyami "As me thought, none of you are worthy of the way of the board."
    iyami "Me was going to give you a chance, but you have only wasted my time, zansu!"
    iyami "Farewell, zansu."
    show oso Swim 01 Surprised Flip at pos1
    show choro Swim 01 Surprised Flip at pos2
    show kara Swim 01 Surprised Flip at pos3
    show ichi Swim 01 Shocked1 at pos4
    show todo Swim 01 Surprised at pos5
    show jyushi Swim 01 Shocked1 at pos6
    everyone "{size=+10}{b}W-Wait—!{/b}{/size}" with scrShake
    hide oso
    hide choro
    hide kara
    hide ichi
    hide todo
    hide jyushi
    show oso Swim 03 Sad at pos7
    oso "I-Iyami..."
    show oso Swim 03 Sad at pos7
    oso "We're sorry. Please, teach us how to surf!"
    hide oso
    show oso Swim 01 Sad Flip at pos1
    show choro Swim 01 Sad Flip at pos2
    show kara Swim 01 Sad Flip at pos3
    show ichi Swim 01 Sad at pos4
    show todo Swim 01 Sad at pos5
    show jyushi Swim 01 Sad at pos6
    everyone "Please!" with scrShake
    hide oso
    hide choro
    hide kara
    hide ichi
    hide todo
    hide jyushi
    iyami "..."
    iyami "You all better be prepared!"
    show oso Swim 01 Happy1 Flip at pos1
    show choro Swim 01 Happy1 Flip at pos2
    show kara Swim 01 Happy1 Flip at pos3
    show ichi Swim 01 Happy1 at pos4
    show todo Swim 01 Happy1 at pos5
    show jyushi Swim 01 Happy1 at pos6
    everyone "....!!!"
    
    return