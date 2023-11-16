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
                "You get closer to the desk. A girl with piercings and bright hair turns to face you."
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

                show maxi neutral
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

                    maxi "Ah yeah there is! By the way Jordan use's They/Them pronouns."

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


        #Have Maxi use Jordan's birth name here by accident. Show how Maxi apologizes and moves on. No need to make a big deal about it.


        #blah blah. If u visit here you see people making songs and stuff. like a non-binary singer and a pansexual lyricist.

        #they're having a workshop soon. After knowing this information if u visit
        #Sam and Michelle you end up giving them this information and then you all go to the workshop.

    elif event == "sam_visit":
        "You and Sam & Michelle visit the workshop. Sam gains insight on incorporating her gender identity and stuff into her music. Everyone meets Max. Everyone meets Jordan. After the workshop, Sam expresses a desire to visit places from her past to reconnect with her past self. You accompany her & michelle on this journey."
        #"You and Sam & Michelle visit the workshop.
        #Sam gains insight on incorporating her gender identity and stuff into her music.
        #Everyone meets Maxi. Everyone meets Jordan. After the workshop, Sam expresses a desire to visit places from her past to reconnect with her past self. You accompany her & michelle on this journey."
        
        jump closet

    jump mall_location_options