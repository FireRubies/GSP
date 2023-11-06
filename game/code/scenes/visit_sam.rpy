label visit_sam(event="normal_visit"):

    scene sams house

    if event == "normal_visit":
        
        if completed_recording_studio_workshop:
            menu:
                "Talk to Sam about how her song is going":
                    sam "Sam says it's going well blah blah blah. She mentions there's a Pride event coming up soon and that she wants to perform the song she's been working on with Michelle there."
                    menu:
                        "Help Sam":
                            "You decide to help Sam"
                            show sam smile
                            sam "Great! Thanks so much! "

                            show sam neutral
                            you "Of course! How can I help?"

                            show sam smile
                            sam "Well right now I think I need help with rehearsing, choosing an outfit, and writing some sort of speech."

                            menu:
                                "Let's do some rehearsing first.":
                                    you "Let's do some rehearsing first."
                                    
                                    sam "Sounds good to me!"

                                    jump sam_rehearsal

                        "Don't help Sam":
                            "Choose to not help Sam."

                "Chitchat":
                    "You visit Sam and Michelle. You chit-chat for a bit and then head back to your house."

    if event == "recording_studio_workshop":
        #blah blah blah. convince Sam & M to attend recording studio workshop.
        "meep"
        call recording_studio(event="sam_visit")

    if event == "after_journey":
        "You & Sam & M return to Sam's house after the journey. Sam reflects on her experiences and thanks you for giving her inspiration."

        #Here the player can suggest that Sam collaborates with either Jordan or Max.
        #This decision also affects the main storyline.
        $ completed_recording_studio_workshop = True
    
    jump house_porch_options