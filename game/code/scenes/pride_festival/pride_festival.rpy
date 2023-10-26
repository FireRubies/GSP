label pride_festival:
    if going_to_festival_with_sam:
        "You go over to Sam's house."
        
        #Make sure Sam's avatar changes so she's wearing a red dress!
        show sam red dress
        show sam smile
        sam "You ready?"

        you "Yup! Where's Michelle?"

        sam "Oh she's just finishing up her makeup inside."

        you "Ah I see. Well you look great! The [sam_dress] really suits you!"

        sam "Aw well thanks for helping me pick it out!"

        "Mi emerges from the house."

        show michelle
        michelle "Hi [player_name]!"

        menu:
            "Hi! Nice outfit!":
                you "Hi! Nice outfit!"

                show michelle smile 
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