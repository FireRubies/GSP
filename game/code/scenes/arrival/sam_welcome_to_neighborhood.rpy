label sam_welcome_to_neighborhood:
    "You wake up and stretch your legs. Birds are chirping. You glance at your phone and see that it's 10 am. You begrudgingly get out of bed and start getting ready for the day. Then, as you're tying your shoes you hear a knock on your door and murmured whispers."

    menu:
        "Open the door":
            "You open the door."
            jump opened_door

        "Finish tying your shoes":
            "You finish tying your shoes and then you open the door."
            jump opened_door

label opened_door:
    if peeked_through_window:
        "You hesitantly open the door and see the two girls you saw last night standing there. You beckon them inside."
    else:
        "You hesitantly open the door and see two girls standing there. You beckon them inside."

    scene player house inside

    show sam at left
    show michelle at center

    sam "Hey! It's nice to meet you! Welcome to the neighborhood!"

    "You do a quick double-take. That's a deep voice. Hm. Well whatever."

    you "Thanks! It's nice to meet you too!"
    
    sam "Of course! Oh by the way I'm Sam! I use She/Her pronouns."

    michelle "Oh and em. I-. I'm Michelle. em. S-she/her."

    you "It's nice to meet you too Michelle!"

    you "Oh where are my manners? I forgot to introduce myself!"

    $ player_name = renpy.input("What is your name?", length=10).strip()

    menu:
        "What are your pronouns?"

        "She/Her":
            $ player_pronouns = "She/Her"
            $ player_pronoun_subjective = "she"
            $ player_pronoun_objective = "her"

        "He/Him":
            $ player_pronouns = "He/Him"
            $ player_pronoun_subjective = "he"
            $ player_pronoun_objective = "his"

        "They/Their":
            $ player_pronouns = "They/them"
            $ player_pronoun_subjective = "they"
            $ player_pronoun_objective = "their"

    sam "It's nice to meet you [player_name]! Thanks for telling us your pronouns are [player_pronouns]!"

    if player_pronouns == "She/Her":

        show michelle pout
        sam "It's good to have another lady around!"
        
        show michelle blush
        sam "Aw don't worry Mi! Girlfriends for life!"

        "Sam boops Michelle on the nose."

        show michelle neutral
        sam "Anywayyyyy. If you ever need anything [player_name] then just come over and ask! Oh and here's a map of the town! We circled some of our favorite places for you!"

        you "I'll definitely keep that in mind. Thanks so much!"
    else:
        sam "If you ever need anything [player_name] then just come over and ask!"
        
        you "I'll definitely keep that in mind. Thanks so much!"

    you "Oh yeah. Is there anything I can help you guys with? I just got here so I don't really have anything to do."

    "Sam looks at Michelle with questioning eyes. Michelle nods a bit."

    sam "well... there is one thing. So I like writing and performing music, it's kinda random but I've been having a bit of writer's block lately."

    you "Hmmmmm I see."

    menu:
        "Are there any major aspects of your life that you could integrate into your songs?":
            show sam nervous
            sam "I mean I could make a song about being trans I guess?"

            show michelle smile
            you "Yeah that would work! It could be educational too!"

            show sam neutral
            "Sam glances at Michelle."

            show sam smile
            sam "Yes I think that's a good idea. Mi could help too! She loves educating people about this stuff and she's great at it!"

            show michelle blush
            michelle "T-thanks Sam."

            sam "Of course Mi!"

            "You can't help but smile at Sam & Michelle's wholesomeness."

            sam "Well I guess we'll go start working on that! Thanks for helping me brainstorm [player_name]!"

            you "No problem! Anytime! It was nice meeting you both!"

            show sam smile
            sam "It was nice meeting you too!"

            show michelle smile
            "Michelle nods, agreeing with Sam."

            "Then they walk out and go back to their house."

            $ sam_welcome_to_neighborhood = True
            jump inside_house_options
            

            #questions for craig:
                #allow players to do bad things?
                #where are requirements for presentation?

        




    
