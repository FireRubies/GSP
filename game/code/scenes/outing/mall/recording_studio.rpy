label recording_studio(event="normal_visit"):

    scene recording studio

    if event == "normal_visit":
        "You see various people milling around the Recording Studio. There's nothing of interest going on."

    elif event == "first_visit":

        $ visited_recording_studio = True

        $ approached_desk = False
        $ approached_room = False

        $ learned_jordans_pronouns = False

        "You see various people standing around. There's an androgenous looking person singing in a small soundproof room to the side and someone writing on a desk near the entrance to the studio."

        menu recording_studio_options:
            "Approach the desk" if not approached_desk:
                $ approached_desk = True

                show jordan neutral
                "You get closer to the desk. A girl with piercings and pretty hair turns to face you."
                menu:
                    "Hi! I'm [player_name]! I'm just wandering around.":
                        jordan "Oh hi! Pleased to meet you [player_name]! I'm Jordan!"
                        menu:
                            "Nice to meet you too! Oh yeah what are your pronouns? I'm [player_pronouns].":
                                jordan "Oh I see! I use They/Them pronouns. Thanks for asking! How's your day been going?"
                                $ asking_for_pronouns.grant()
                                $ learned_jordans_pronouns = True

                            "Nice to meet you too!":

                                jordan "How's your day been going?"

                        you "Good thanks for asking! How about you?"

                        show jordan smile
                        jordan "Good, good! I'm just setting up for the workshop we're having soon."

                        you "Workshop?"

                        jordan "Yeah! We're gonna talk about writing music and stuff. It'll be blast! Maxi, who's in the Recording Room right now, is gonna talk too!"

                        you "Oooo thanks for letting me know! Maybe I'll stop by."

                        jordan "No problem! Hope to see you there!"
                        $ learned_about_recording_studio_workshop = True
                        jump recording_studio_options


                #Jordan

            "Approach the small room" if not approached_room and approached_desk:
                $ approached_room = True

                show maxi neutral at left
                "You go close to the small room. You see a androgenous looking figure inside the room."

                "The person inside the room turns to look at you."

                maxi "Hello! Can I help you with something?"

                you "Yeah! I was just talking with emmm."

                maxi "Jake? Er. Sorry. Jordan?"
                
                if learned_jordans_pronouns:
                    you "Yeah Jordan! They were nice. You're Maxi right? Apparently there's a workshop here soon. Figured I'd see if you knew about it."

                    show maxi smile
                    maxi "Yes I'm Maxi! Pleased to meet you... ermm."

                    you "Ah where are my manners. I'm [player_name], [player_pronouns]."

                    maxi "Thanks! I'll start over, pleased to meet you [player_name]! Anyway the workshops, I help lead them with Jordan. Sh- They're really talented!"

                else:
                    you "Yeah Jordan! She was nice. Oh I'm [player_name] by the way.
                        Anyway apparently there's a workshop here soon. Figured I'd see if anyone else knew about it."

                    maxi "Ah yeah there is! By the way Jordan uses They/Them pronouns."

                    you "Ah okay, thanks for letting me know! Oh, and I use [player_pronouns] pronouns. You're Max right?"

                    maxi "Yes I'm Maxi! My pronouns are He/Him. And don't worry about the mixup, as long as you make an effort to use the right pronouns it's okay.
                        As for the workshop. They're great. I help lead them with Jordan. They're really talented!"

                you "Oh awesome! I might bring some friends by then. I just moved here recently so it's nice to see that the community is so nice!"

                show maxi smile
                maxi "Oh well welcome to the area! And yeah that would be nice! The more the merrier!"

                jump recording_studio_options

                #Maxi

            "Leave the studio" if approached_desk:
                pass

    elif event == "sam_visit":
        #"You and Sam & Michelle visit the workshop.
        #Sam gains insight on incorporating her gender identity and stuff into her music.
        #Everyone meets Maxi. Everyone meets Jordan.
        #After the workshop, Sam expresses a desire to visit places from her past
        #to reconnect with her past self.
        #You accompany her & michelle on this journey."

        show sam smile at left
        show michelle at right

        sam "Phew. I haven't run that much in a while!"

        "Michelle just stands there panting."

        you "Y. Yeah that was quite the run!"

        show jordan smile at center

        jordan "Hey [player_name] you made it! Ooo and you brought Sam and ooooo Sam do you have a girlfriend now?"

        sam "Yup! That's Michelle! It's been a bit Jordan! How have you been?"

        jordan "I've been good! Lots of work- shops though. Hehe."

        "Sam giggles quietly."

        sam "It's good to see you haven't changed."

        jordan "Hehe. Well I do believe it's time for the workshop!"

        "Jordan claps their hands together."

        jordan "Maxiiiiiiiii!"

        show maxi at right
        "A confused looking Maxi emerges from the the small room off to the side."

        maxi "Yes Jordan?"

        jordan "It's time for the workshop!"

        menu:
            "Yay!":
                jordan "That's the right kinda energy! Yay!"

                sam "Yay!"

                michelle "Yay!"

                maxi "..."
            "Say nothing":
                pass

        jordan "Okay so Sam is there something specific you want help on?"

        sam "Well I'm trying to write a song that incorporates aspects of my life into it.
        Specifically gender identity stuff."

        "Maxi smiles in approval."

        jordan "That's a good idea!"

        sam "Yeah well I have [player_name] to thank for that!"

        jordan "Well it takes multiple eggs to make an omelet! I think...
        Anyway collaboration is great!"

        sam "Yeah! Mi is helping with the lyrics. I just can't think of what specifically to put in them.
        I mean there's so much stuff and I only get about 2 minutes."

        jordan "Hmmmm."

        maxi "Do you have any places that are of significance of you that relate to that?"

        "Sam thinks for a moment."

        sam "Yeah. Lots! So you think I should go there and get some inspiration?"
        
        show maxi smile
        maxi "Exactly!"

        jordan "Great idea Maxi! And oooo it looks like someone else has arrived!"

        "Liam waves at everyone."

        liam "Heyo! I was just walking around the mall and figured I'd see what was going on here.
        Oh. Names Liam by the way."

        jordan "Welcome Liam! We're doing a workshop at the moment. Me and my friend Maxi here
        try to help people with lyrics, music theory, etcetera."

        liam "Oh I see. Well I don't really do much music stuff but that sounds cool!"

        michelle "It is!"

        liam "Nice! Thought so! Well what are you guys talkin' about now?"

        jordan "We were just helping Sam and Michelle on their song."

        liam "What kinda song?"

        sam "It's like a personal gender identity educational motivational... thing."

        "Michelle nods."

        michelle "Yup that's it!"

        "Liam chuckles."

        liam "Sounds swaggy!"

        menu:
            "Swaggy?":
                liam "Yeah!"

            "Blank stare":
                "Liam looks at you as you stare at him."

                liam "What? Is it the swaggy? It just means cool basically. I heard it recently and can't stop saying it!"

        michelle "Heh. That's pretty swaggy indeed!"

        sam "The swaggiest!"

        "Liam giggles."

        liam "Yall are funny. I like that."

        "Sam looks at her watch."

        sam "Well we gotta run though if we wanna get through all of the memorable places today!
        It was nice meeting you Sam and Maxi, and catching up with you Jordan of course."

        "Michelle agrees with two thumbs up."

        maxi "It was our pleasure!"

        "Jordan nods."

        liam "Nice meeting you too Sam and Michelle!"

        jordan "Come back soon!"

        sam "Definitely! We need to catch up more!"
        #This line sets up the Fancy Restuarant scene later down the line. The player can choose to go to the fancy restaurant
        #with Sam and Michelle and then Sam mentions bringing Jordan along because the more and the merrier and also Sam wants to
        #catch up with Jordan. This dinner will give you more insight into Michelle as Sam and Jordan are busy talking. Show a lot
        #about Michelle here. About her past and stuff. Make it cool and insightful and yeahhhh yay

        sam "Okay so hmmm. I-. I guess we can go to my old school first..."

        michelle "You sure?"

        "Sam nods."

        michelle "Okay then. Let's go."
        
        jump middle_school

    jump mall_location_options