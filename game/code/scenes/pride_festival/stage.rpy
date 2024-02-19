label stage:

    scene stage

    show sam
    "Sam walks onto the stage."

    sam "Hey everyone! Thank you all for being here tonight."

    # Depending on previous choices, adjust Sam's confidence or nervousness
    if made_michelle_angry and handled_closet_badly:
        "Sam didn't show up... everyone leaves, confused and annoyed."
        
    elif closet_choices > 1:
        sam """This song means a lot to me, and I'm thrilled to share it with all of you. I'm trans and I've been transitioning for a while now."
        It's been an incredible journey, and this song reflects a piece of that.
        I hope you all enjoy it!"""

        play music "tropical_summer_music.mp3" volume 0.25

        """She walked along a winding road, {w=1}{nw}
        Searching for a love untold, {w=1}{nw}
        Carrying dreams within her soul, {w=1}{nw}
        Embracing courage, breaking molds. {w=1}{nw}

        In the mirror, she saw a reflection, {w=1}{nw}
        A world desiring her connection, {w=1}{nw}
        With every step, she found her way, {w=1}{nw}
        Unveiling the truth without delay. {w=1}{nw}

        Transcendence, her true essence shines, {w=1}{nw}
        A beautiful journey without confines, {w=1}{nw}
        Through highs and lows, she found her voice, {w=1}{nw}
        Rising above, she embraced her choice. {w=1}{nw}

        With grace and strength, she bloomed anew, {w=1}{nw}
        Unveiling colors, vibrant and true, {w=1}{nw}
        Through the storms, she weathered the pain, {w=1}{nw}
        Emerging fearless, like an autumn rain. {w=1}{nw}

        In the mirror, she saw transformation, {w=1}{nw}
        A symphony born from self-liberation, {w=1}{nw}
        With every note, she sang her truth, {w=1}{nw}
        Resonating love, unending proof. {w=1}{nw}

        Transcendence, her true essence shines, {w=1}{nw}
        A beautiful journey without confines, {w=1}{nw}
        Through highs and lows, she found her voice, {w=1}{nw}
        Rising above, she embraced her choice. {w=1}{nw}

        Through the darkness, she found her light, {w=1}{nw}
        Embracing love, wrapped in pure delight, {w=1}{nw}
        Society's whispers turned into a hum, {w=1}{nw}
        Her spirit soaring, no longer numb. {w=1}{nw}

        With outstretched wings, she took to flight, {w=1}{nw}
        Her heart empowered, ready to ignite, {w=1}{nw}
        A beacon of hope, a guiding star, {w=1}{nw}
        Empathy and love, her guiding guitar. {w=1}{nw}

        In the mirror, she saw liberation, {w=1}{nw}
        A soul reborn, a vivid revelation, {w=1}{nw}
        With every strum, she shared her tale, {w=1}{nw}
        Inspiring others, her love would prevail. {w=1}{nw}

        Transcendence, her true essence shines, {w=1}{nw}
        A beautiful journey without confines, {w=1}{nw}
        Through highs and lows, she found her voice, {w=1}{nw}
        Rising above, she embraced her choice. {w=1}{nw}

        May her story echo near and far, {w=1}{nw}
        A testament to strength and who we are, {w=1}{nw}
        In unity, let's celebrate the brave, {w=1}{nw}
        For in their light, all of us can be saved. {w=1}{nw}"""
        
    elif closet_choices < 1:
        sam "T-. This song means a-. a lot to me. so-. so I hope you a-all en-enjoy it!"

        play music "tropical_summer_music.mp3" volume 0.25

        """She strolled down a lame old path, {w=1}{nw}
        Looking for love, facing the wrath, {w=1}{nw}
        Carrying some dreams, kinda small, {w=1}{nw}
        Embracing meh, breaking a wall. {w=1}{nw}

        In the mirror, she saw her face, {w=1}{nw}
        A world kinda wanting her place, {w=1}{nw}
        With each step, she sorta walked, {w=1}{nw}
        Unveiling kinda truth, kinda balked. {w=1}{nw}

        Transcendence, her sorta essence glows, {w=1}{nw}
        A so-so journey, no real oohs or woes, {w=1}{nw}
        Through not-so highs and sorta lows, she found her voice, {w=1}{nw}
        Rising a bit, she kinda made a choice. {w=1}{nw}

        With kinda grace, she kinda bloomed, {w=1}{nw}
        Showing colors, maybe gloomed, {w=1}{nw}
        Through some storms, she kinda felt pain, {w=1}{nw}
        Emerging sorta fearless, like, okay, a bit of rain. {w=1}{nw}

        In the mirror, she saw sorta change, {w=1}{nw}
        A so-so song, kinda feels strange, {w=1}{nw}
        With each note, she sang a bit, {w=1}{nw}
        Resonating a little, kinda hit. {w=1}{nw}

        Transcendence, her sorta essence glows, {w=1}{nw}
        A so-so journey, no real oohs or woes, {w=1}{nw}
        Through not-so highs and sorta lows, she found her voice, {w=1}{nw}
        Rising a bit, she kinda made a choice. {w=1}{nw}

        Through the darkness, she kinda found a light, {w=1}{nw}
        Embracing like, I guess, alright, a slight delight, {w=1}{nw}
        Society's whispers, sorta hummed, {w=1}{nw}
        Her spirit kinda soaring, no longer a bit numb. {w=1}{nw}

        With wings kinda outstretched, she kinda flew, {w=1}{nw}
        Her heart like, sorta empowered, ready to do, {w=1}{nw}
        A beacon maybe, sorta a guide, {w=1}{nw}
        Empathy and like, sorta love, her kinda guide. {w=1}{nw}

        In the mirror, she saw, like, freed, {w=1}{nw}
        A soul sorta reborn, a little, a vivid feed, {w=1}{nw}
        With each strum, she kinda shared, {w=1}{nw}
        Inspiring like, kinda others, her love sorta spared. {w=1}{nw}

        Transcendence, her sorta essence glows, {w=1}{nw}
        A so-so journey, no real oohs or woes, {w=1}{nw}
        Through not-so highs and sorta lows, she found her voice, {w=1}{nw}
        Rising a bit, she kinda made a choice. {w=1}{nw}

        May her story kinda echo, sorta close and far, {w=1}{nw}
        A testament a bit to strength, kinda who we are, {w=1}{nw}
        In unity, let's maybe kinda celebrate the sorta brave, {w=1}{nw}
        For in their light, like, all of us can be a little saved. {w=1}{nw}"""

        "Most of the audience cheered but it was less enthusiastic than it could've been."

    stop music fadeout 1.0

    # Depending on previous choices, adjust the audience's reaction
    if closet_choices > 1:
        "audience like."
        # Audience reacts positively
        # Show expressions of enjoyment or excitement
        # Add dialogue from supportive characters cheering Sam on
    else:
        "audience less like."
        # Audience reaction might be more neutral or varied
        # Show expressions indicating mixed emotions or curiosity
        # Add dialogue with varied responses from characters

    #NOTE: REMEMBER TO NOT HAVE SAM SHOW UP IF THE PLAYER HASN'T APLOGIZED TO SAM BEFORE GOING!!!
    jump pride_festival_options