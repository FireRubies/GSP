label visit_sam(event="normal_visit"):

    scene sams house

    if event == "normal_visit":
        if completed_recording_studio_workshop:
            if not handled_closet_badly and not made_michelle_angry:
                menu sam_event_preparations_menu:
                    "Talk to Sam about how her song is going":
                        show sam smile
                        sam "It's been going well! Thanks for asking!"

                        you "Of course!"

                        sam "Oh yeah there's a Pride event coming up soon.
                        I was thinking of performing the song I've been working on with Mi there.
                        I could use some help with the preparations though.
                        Would you mind helping a neighbor out?"

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

            elif handled_closet_badly or made_michelle_angry:
                menu:
                    "Apologize to Sam" if handled_closet_badly and not made_michelle_angry:
                        show sam frown at left
                        
                        you """Hey uh. I just wanted to apologize for earlier. I don't know what came over me.
                        I. I just wasn't thinking...
                        I realize how offensive my words were now."""

                        show sam neutral

                        sam "It's okay... just don't do it again!!!! Seriously!"

                        you "Yes mam!"

                        $ handled_closet_badly = False

                    "Apologize to Sam & Michelle" if handled_closet_badly and made_michelle_angry:
                        show sam frown at left
                        show michelle frown at center

                        you """Hey uh. I just wanted to apologize for earlier. I don't know what came over me.
                        I. I just wasn't thinking...
                        I realize how offensive my words were now."""

                        show sam neutral

                        sam "It's okay... just don't do it again!!!! Seriously!"

                        you "Yes mam!"

                        michelle "Hmph. Well... if Sam forgives you that's good enough for me..."

                        $ handled_closet_badly = False
                        $ made_michelle_angry = False

                jump sam_event_preparations_menu

        else:
            "You hang out with Sam and Michelle and chat for a bit. Then you head back home."

    if event == "recording_studio_workshop":
        show michelle at right
        show sam at left

        you "Hey guys!"

        show michelle smile
        michelle "Hi!"

        show sam smile
        "Sam waves at you."

        sam "What's up?"

        you "Ah well I just went to the mall and I guess there's some kind of workshop happening there at the Recording Studio.
        I figured I'd let you guys know about it and see if you wanted to come."

        sam "Oooo that sounds great! When is it?"

        you "Mmm I uh. I didn't actully check but Jordan said it was starting soon."

        show sam frown
        sam "Ah okay then we gotta hurry! Let's go!"

        call recording_studio(event="sam_visit") from _call_recording_studio_1
        
    
    jump house_porch_options