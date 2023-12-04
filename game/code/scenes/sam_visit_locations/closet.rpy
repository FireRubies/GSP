label closet:
    scene closet

    $ closet_choices = 0
    #Sam goes home & looks at old closet. She brought it from her old house.
    #It's the closet where she first tried on stereotypically feminine clothes.

    #"Sam goes to house w/ u. Go in & look at closet. Sam explains why the closet is special to her. You can comment on it. Your comments in this visiting branch affect the main storyline!"

    scene sams house
    with dissolve

    pause 2

    scene closet
    with fade

    pause 1

    show sam smile at left
    show michelle at center

    sam "Well here we are. It doesn't look like much but this closet is where I put my first dress!"
    sam "It was actually at my old house where I lived with my parents but I paid to have it moved because it means so much to me."

    menu:
        "Aww. That's so sweet.":
            $ closet_choices += 1
            you "Aww. That's so sweet."

            show sam blush
            sam "Aww thanks!"

            "Sam goes up and hugs the closet."
            

        "Why's that matter?":
            $ closet_choices -= 0.5
            you "Why's that matter?":

            show sam frown
            show michelle frown
            sam "Ah well it was a special moment for me!"

            menu:
                "Ehh. Just seems like clothing to me.":
                    $ closet_choices -= 0.5
                
                "Ah okay I see! Sorry for my ignorance there.":
                    $ closet_choices += 0.5

                    show sam smile
                    show michelle neutral
                    sam "Ah it's no problem! Now you know."

    menu:
        "So when did you get your first dress?":
            sam "Hmm. It must've been something like... mmm. 5 years ago?"

            you "Ah so it's been a while then!"

            #sam yes it has been

            menu:
                "I thought transgender people were usually diagnosed young?":
                    #sam spits facts here about how that's not entirely correct

                "5 years? Hmm. That's not a while. Are you sure you're trans?":
                    $ closet_choices -= 1



    #All good comments - great ending
    #Mostly good comments - good ending
    # Half & Half - okay ending
    # Mostly bad comments - bad ending
    # All bad comments - horrible ending

    #Add player comments here!

    call visit_sam(event="after_journey")