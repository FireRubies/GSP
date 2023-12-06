label closet:
    scene closet

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

            you "Ah so it's been a few years."

            sam "Yup!"

            menu:
                "I thought transgender people were usually diagnosed young?":
                    show sam smile
                    sam "Ah yeah that's what most people think but really people can come out of their egg at any point."

                    "Michelle nods"

                    menu:
                        "Egg?":
                            $ closet_choices += 0.25
                            sam "Ah it's what we in the community call someone who doesn't realize they're trans yet."

                            you "Ohhhhh okay. Thanks for the explanation."

                            sam "No problem!"

                        "Ah okay":
                            you "Ah okay."

                    

                "5 years? Hmm. That's not a while. Are you sure you're trans?":
                    $ closet_choices -= 1

                    show sam frown
                    show michelle frown

                    sam "Yes... very. Anyway I didn't say I came out of my egg then. Regardless it's offensive to ask that."

        "So this is where you keep all your clothes?":
            $ closet_choices += 0.25

            "Sam giggles."

            sam "Of course not silly. I have another closet in my room. One closet wouldn't be enough."

            you "Wow that's a lot of clothes!"

            sam "Of course! Casual wear, party wear, clothing for cold weather, clothing for hot weather, school wear, swimsuits, etc."

            you "Ah.. I see."

            "Michelle snorts soflty off to the side."

            michelle "Sam really likes her clothing."
            
            sam "Yes I do!"

    #possible insertion of collab between Sam & Jordan or Maxi here. Add if you have time.

    "Sam looks at the closet and closes her eyes, reminiscing on her past."

    "You and Michelle share a glance as Sam does this and you both quietly tiptoe out of the room to let her process."

    # NOTE: Add different dialogues here based on the player's 'closet_choice' score!
    # Less than or equal to 0.5 is a bad dialogue ending
    # Greater than or equal to 0.5 is a good dialogue ending
    # also have a variable called good_closet_ending be either true or false
    # depending on the result here. This is so you can use that variable
    # in future story dialogue options and branches!

    scene sams house

    if closet_choice >= 0:
        show michelle smile at left

        michelle "We can talk now. Thanks for... doing this. Even though you haven't known us long."

        menu:
            "You guys came to me first!":
                you "Well you guys came to me first and offered to give me help with stuff so it's only natural that I help you out too!"

            "Of course! I love helping out my friends.":
                you "Of course! I love helping out my friends."

        "Michelle nods."

        michelle """Well thanks again. Some of our previous neighbors haven't been as... accepting.
        Anyway I better go back inside. It's getting dark and I wanna watch a movie with Sam before heading to bed. Talk later?"""

        you "Definitely!"
    
    else if closet_choice < 0:
        $ handled_closet_badly = True
        show michelle frown at left

        michelle "We can talk now. What was that?"

        menu:
            "What was what?":
                michelle "That! Why were you so rude?!"

                menu:
                    "Rude?":
                        you "What do you mean?"

                    "I'm sorry! I wasn't trying to be rude.":
                        you "I'm sorry! I wasn't trying to be rude! I just kept slipping up..."

                        michelle "Mhm. You definitely did. You have to make this up to Sam somehow."

                        #Add a thing here where the player has the option to make it up to Sam.
                        #If the player chooses not to then the story continues but Sam doesn't show up
                        #on stage during the pride festival event.
                        #Also all stuff involving Michelle & Sam is locked until the player makes it up to Sam

            "I don't know. I wasn't trying to be offensive.":

                michelle "Well you were! You have to make this up to Sam somehow!"
            
            "I dunno.":

                michelle "You don't know??? Questioning her about whether HER perception of her gender was correct?!"

                menu:
                    "Ah. Jeez. I didn't realize what I was doing...":

                        michelle "Clearly!"

                        michelle "You have to make this up to Sam somehow!"

                    "Well she's wrong!":
                        $ made_michelle_angry = True
                        #If the player chooses this option then Sam doesn't show up to the pride event either.
                        #Also all stuff involving Michelle & Sam is locked!

                        michelle "Get out."

                        michelle "NOW!"

    #Add player comments here!
    $ completed_recording_studio_workshop = True
    jump house_porch_options