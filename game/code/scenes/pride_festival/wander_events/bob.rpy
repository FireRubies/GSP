label bob:

    #NOTE: Fill this in with LGBTQIA+ lessons and stuff later maybe?

    $ wanderable_places.remove("bob")

    if going_to_festival_with_sam:
        show sam at right
        show michelle at center

        "While wandering around the festival grounds with Sam and Michelle, you spot a guy waving at you enthusiastically."

        sam "Hi, I'm Sam."

        michelle "Hey there, I'm Michelle."

        sam "Hey, isn't that Bob from our art class?"

        michelle "Oh yeah, I think it is! Let's go say hi!"

        "You approach Bob and engage in a conversation."
        scene pride festival plaza
        show bob

        #NOTE: Maybe show a Bob character here????
        bob "Hey, it's great to see you all here! How's the festival been treating you?"

        sam "It's been amazing! We've been having a blast."

        michelle "Definitely, there's so much energy here."

        bob "I know right! Pride festivals always bring out the best vibes, don't they?"

        "After exchanging contact information with Bob, you continue to explore the festival together with Sam and Michelle."
    else:
        "As you wander around the festival grounds, you notice a guy smiling at you from a nearby booth."
        scene pride festival plaza
        show bob

        bob "Hey there! I'm Bob. Mind if I join you for a stroll around the festival?"

        bob "Of course! It's awesome meeting new people who share the love for pride festivals! How's your experience been so far?"

        menu:
            "It's been amazing!":
                you "It's been amazing! I've been having a blast. There's always so much energy here."

                bob "I know right! Pride festivals always bring out the best vibes, don't they?"

                bob "That sounds amazing! Mind if I take a group photo of you to capture this moment?"

                "You and Bob take a selfie together, capturing the joyful atmosphere of the pride festival."

            "Ehhh.":
                you "Ehhh. It hasn't been that good so far."

                bob "Oh I'm sorry to hear that! Well I hear there's a performance soon that'll knock everyone's socks off!"

                you "Oh?"

                bob "Yeah someone named Sam is performing! Weird. Someone in my art class is named Sam."

                you "Oh yeah that's... interesting. Well I'll see you there maybe?"

                bob "Yeah! I'll definitely be there!"

    jump pride_festival_options