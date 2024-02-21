label group_meditation:

    scene group meditation

    if going_to_festival_with_sam:
        show michelle at right
        show sam at center

        sam "What's this?"

        michelle "It looks like some kind of meditation area."

        show liam
        liam "Hey guys! Yeah this is the meditation room! Wanna try it out?"

        menu:
            "Yes":
                $ wanderable_places.remove("group_meditation")
                play music "wandering.mp3"
                menu:
                    "Done Meditating":
                        stop music fadeout 1.0
                        menu:
                            "That was nice!":
                                liam "I'm glad you liked it!"
                            
                            "Awesome! I feel so relaxed.":
                                liam "I'm delighted you found it relaxing."

                        sam "Yeah it was great!"

                        "Michelle nods and smiles at Liam."

            "No":
                liam "Aw okay. Well it'll be here if you ever wanna use it!"

    else:

        you "Hmm. What's this?"

        show liam
        liam "Hey [player_name] Yeah this is the meditation room! Wanna try it out?"

        menu:
            "Yes":
                $ wanderable_places.remove("group_meditation")
                play music "wandering.mp3"
                menu:
                    "Done Meditating":
                        stop music fadeout 1.0
                        menu:
                            "That was nice!":
                                liam "I'm glad you liked it!"
                            
                            "Awesome! I feel so relaxed.":
                                liam "I'm glad it was relaxing for you!"

                liam "I'm glad you liked it!"

            "No":
                liam "Aw okay. Well it'll be here if you ever wanna use it!"

    jump pride_festival_options