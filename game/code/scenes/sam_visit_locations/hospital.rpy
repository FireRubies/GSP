label hospital:
    scene hospital
    #"Sam & M & you visit the hospital where Sam got her gender-affirming care"

    show sam neutral at left
    show michelle neutral at center

    sam "Here we are! This is where I got my HRT prescription and hopefully where I'll get my gender affirmation surgery."

    $ learned_about_hrt = False
    $ learned_about_gender_affirmation_surgery = False
    menu sam_hospital_menu:
        "HRT?" if not learned_about_hrt:
            $ learned_about_hrt = True

            sam "Yeah! It's Hormone Replacement Therapy. Basically I took estrogen to help better align my appearance with my gender identity."

            show sam smile 
            sam "It's been a crucial part of my transition."

            "Sam points at her chest."

            sam "It's how I got these."

            michelle "Yeah it's like a miracle drug! Although it really is just hormones."

            sam "Yeah. Hormones are really powerful! Mm. If only they hadn't messed me up in the first place..."

            sam "Anywayyyyyy"

            jump sam_hospital_menu

        "Gender Affirmation Surgery?" if not learned_about_gender_affirmation_surgery:
            $ learned_about_gender_affirmation_surgery = True

            sam "Yeah. It's just surgery that makes your body more stereotypically female."

            sam "There's stuff like FFS (Facial Feminization Surgery) which makes your face look more like that of a cisgender female and much more!"

            sam "I haven't gotten it yet because I can't afford it but hopefully I'll get it someday."

            michelle "Mm. And it's not required either. You don't need to do HRT or get surgery to be trans."

            show michelle smile 
            michelle "Remember it's about who you are, not what your body looks like. Most people just do it because it allows them to feel like their body actually reflects who they are."

            sam "Exactly. Thanks for the addendum Mi!"

            michelle "No problem!"

            jump sam_hospital_menu

        "Can we go inside?":
            sam "Yeah!"

    scene hospital reception

    show sam smile at left
    show michelle smile at center
    show jay neutral at right

    sam "Jay!!!!"

    show jay smile 
    jay "Sam! It's been a bit! Are you keeping up with your blood work?"

    sam "Of course of course! I've just been a bit busy. I have an appointment next week though."

    "Jay shuffles through some papers."

    jay "Oh. Indeed you do! Good good."

    jay "Hello to you too Michelle! Anddddddd."

    you "[player_name], pleased to meet you."

    jay "Ah thanks! Yes it's good to meet you too! Any friends of Sam are friends of mine!"

    "Jay glances at Sam as if asking her something. Sam gives a short nod."

    jay "It's been such a journey with you! It's been my pleasure to help another transperson find their way. Especially when they're someone as nice as you!"

    show sam blush 
    sam "Thanks Jay!"

    michelle "Aww someone's shy hehe."

    "Sam looks at her phone."

    sam "Well it was nice seeing you Jay but we gotta roll. It's almost dark!"

    jay "Aww okay. Come back soon!"

    sam "I will! You'll see me next week remember? We can talk more then!"

    michelle "Bye Jay!"

    you "Bye!"

    jay "Bye! Nice meeting you [player_name]!"

    you "Nice meeting you too!"

    scene hospital

    show sam blush at left
    show michelle smile at center

    sam "Soooo. Home now? We've still got one place to go!"

    michelle "Oh? Where?"

    show sam smile
    sam "It's a surprise!"

    you "Ooo okay! Sounds like fun!"

    jump closet



    #sam "Hi I'm Sam!"
    #michelle "Hi I'm Michelle!"
    #jay "Haiiii I'm Jay!"
    #You can change people's expressions by doing stuff like show sam smile or show jay smile or show sam blush or show sam neutral. Etc. Assume all characters can frown, smile, blush, and have a neutral expression.
    #You & Sam & Michelle arrive
    #You and Sam talk for a bit
    #Sam explains she got her HRT prescription here & surgery and stuff.
    #You all go inside.
    #Talk to Jay the receptionist (FTM, birth name is Caitlyn. Jay likes hiking and organizing outdoor LGBTQIA+ nature outings)
    #Jay talks about how it was nice to help out another trans person and mentions how nice Sam is.
    #Michelle agrees and they do a quick hug. Sam blushes.
    #Then you and Mi and Sam head back outside.



    #Maybe sprinkle some other stuff to educate people about HRT, gender affirmation surgery, and other important LGTBQIA+ topics. But don't put too much stuff in.
    #Possibly add a few branching paths here with different dialogue and such based off of user choices.
    #Regardless of the branching paths all of them end up with you and Sam & Michelle outside the hospital, ready to go back to Sam and Michelle's house.