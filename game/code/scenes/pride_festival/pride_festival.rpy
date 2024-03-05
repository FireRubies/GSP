label pride_festival:
    if going_to_festival_with_sam:
        "You go over to Sam's house."
        
        show sam smile
        sam "You ready?"

        you "Yup! Where's Michelle?"

        sam "Oh she's just finishing up her makeup inside."

        you "Ah I see. Well you look great! The [sam_dress] really suits you!"

        sam "Aw well thanks for helping me pick it out!"

        "Mi emerges from the house."

        show michelle at left
        michelle "Hi [player_name]!"

        menu:
            "Hi! Nice outfit!":
                you "Hi! Nice outfit!"

                show michelle smile at left
                michelle "Aw thanks!"

            "Hi!":
                you "Hi!"

        
        "Michelle goes over to Sam and hugs her."

        you "Aww. You both look great together!"

        sam "Thanks!"

        michelle "Thanks!"

        sam "So I guess we're going now! Let's get in the car."

        "You all go to the garage and pile into the car."

        scene driving to player house
        with dissolve

        pause 3

        scene pride festival
        with fade

        pause 1.0

        show sam smile
        sam "So we're here! What do we wanna do now?"

        michelle "Hmm. I'm not sure. There's so much stuff! What do you think [player_name]?"

        jump pride_festival_options

    if not going_to_festival_with_sam:
        
        scene driving to player house
        with dissolve

        pause 3

        scene pride festival
        with fade

        pause 1.0

        "You arrive at the festival. There are booths lining the streets, crowded with people."

        jump pride_festival_options
        