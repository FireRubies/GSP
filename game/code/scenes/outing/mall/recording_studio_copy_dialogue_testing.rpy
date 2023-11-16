label recording_studio_copy(event="normal_visit"):

    scene recording studio

    if event == "sam_visit":
        label dialogue_testing:
            
            scene recording studio
            $ player_name = "You"
            $ player_pronouns = "They/Their"
            
            menu dialogue_testing_options:
                "Dialogue testing menu"
                "Descriptive Dialogue":
                    #"You and Sam & Michelle visit the workshop.
                    #Sam gains insight on incorporating her gender identity and stuff into her music.
                    #Everyone meets Maxi. Everyone meets Jordan. After the workshop, Sam expresses a desire to visit places from her past to reconnect with her past self. You accompany her & michelle on this journey."
                    
                    "You bring Sam & Michelle to the Recording Studio."

                    show sam smile at left
                    show michelle smile at right

                    sam "Ohhhh this place! I didn't know they had workshops!"

                    michelle "Ooo me neither! Hopefully this'll help!"

                    sam "I bet it will! The people here are great!"

                    you "Hehe. I'm glad you're excited!"

                    show jordan smile at center
                    "Sam rushes over to the desk where Jordan is."

                    sam "Hey Jordan! Long time no see!"

                    jordan "Hey Sam! How are you?"

                    sam "I'm good! I just learned from my friend [player_name] here that you're doing some kind of workshop?"

                    "Sam bounces up and down excitedly."

                    jordan "Yup! We were actually just about to start so you came just in time!"

                    michelle "Yay!"

                    sam "Yay yay! Hehe I one upped your yay!"

                    show michelle frown
                    michelle "Aw darn."

                    sam "Aw don't be sad Mi. I retract my yay."

                    show michelle smile
                    michelle "Yay!"

                    sam "Yayayay!"

                    "Michelle gives Sam a look."

                    sam "Oh. Hehe. Sorry Mi!"

                    michelle "It's okay heh. You know I could never be mad at you."

                    sam "Aww. Ah okay we got sidetracked. The workshop!"

                    jordan "Hehe. Yay! Yes the workshop! Thanks for bringing these two [player_name]!"

                    you "Yeah no problem! Sam was looking for some inspiration so this seemed perfect!"

                    jordan "Great!"

                    jordan "MAXI YOU READY?"

                    maxi "YEAH YEAH. NO NEED TO YELL!"

                    jordan "Ah okay well it sounds like everyone is ready! Let's start!"

                    jump dialogue_testing_options

                "Simple Dialogue":
                    #"You and Sam & Michelle visit the workshop.
                    #Sam gains insight on incorporating her gender identity and stuff into her music.
                    #Everyone meets Maxi. Everyone meets Jordan. After the workshop, Sam expresses a desire to visit places from her past to reconnect with her past self. You accompany her & michelle on this journey."
                    
                    "You bring Sam & Michelle to the Recording Studio."

                    show sam smile at left
                    show michelle smile at right

                    sam "Ohhhh this place! I didn't know they had workshops!"

                    michelle "Ooo. Cool!"

                    you "Hehe. I'm glad you're excited!"

                    show jordan smile at center
                    "Sam rushes over to the desk where Jordan is."

                    sam "Hey Jordan!"

                    jordan "Hey Sam! How are ya?"

                    sam "I'm good! I just learned from my friend [player_name] here that you're doing some kind of workshop?"

                    jordan "Yup! We were actually just about to start so you came just in time!"

                    michelle "Yay!"

                    jordan "Hehe. Yay indeed! Thanks for bringing these two [player_name]!"

                    you "Yeah no problem! Sam was looking for some inspiration so this seemed perfect!"

                    jordan "Great! Well let's start!"

                    jump dialogue_testing_options

    jump mall_location_options