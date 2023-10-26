label recording_studio(event="normal_visit"):

    scene recording studio

    if event == "normal_visit":
        "You see various people milling around the Recording Studio. There's nothing of interest going on."

    if event == "first_visit":
        "You see various people standing around. There's an androgenous looking person singing in a small soundproof room to the side and someone writing on a desk near the entrance to the studio."

        menu:
            "Approach the desk":
                "You get closer to the desk. A girl with piercings and bright hair turns to face you."
                menu:
                    "Hi! I'm [player_name]! I'm just wandering around.":
                        jordan "Oh hi! Pleased to meet you [player_name]! I'm Jordan! "
                        menu:
                            "Nice to meet you! Oh yeah what are your pronouns? I'm [player_pronouns].":
                                jordan "Oh I see! I use They/Them pronouns. Thanks for asking! How's your day been going?"
                                menu:
                                    "Mm thanks for letting me know! My day has been going good!":
                                        jordan "Of course! I wouldn't want you to use the wrong pronouns after all. Anyway I'm glad your day has been good! I'm just setting up for the workshop we're having soon."
                                        menu:
                                            "Workshop?":
                                                jordan "Yeah! We're gonna talk about writing music and stuff. It'll be blast! Max, who's in the Recording Room right now, is gonna talk too!"
                                                menu:
                                                    "Oooo thanks for leeting me know! Maybe I'll stop by.":
                                                        jordan "No problem! Hope to see you there!"
                                                        $ learned_about_recording_studio_workshop = True



                #Jordan

            "Approach the small room":
                "You go close to the small room."

                #Max


        #Have Max use Jordan's birth name here by accident. Show how Max apologizes and moves on. No need to make a big deal about it.


        #blah blah. If u visit here you see people making songs and stuff. like a non-binary singer and a pansexual lyricist.

        #they're having a workshop soon. After knowing this information if u visit
        #Sam and Michelle you end up giving them this information and then you all go to the workshop.

        if event == "sam_visit":
            "You and Sam & Michelle visit the workshop. Sam gains insight on incorporating her gender identity and stuff into her music. Everyone meets Max. Everyone meets Jordan. After the workshop, Sam expresses a desire to visit places from her past to reconnect with her past self. You accompany her & michelle on this journey."
            jump closet

    jump mall_location_options