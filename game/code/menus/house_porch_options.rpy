label house_porch_options:

    scene player house porch

    menu:
        "Go inside":
            jump inside_house_options
        
        "Visit Sam" if has_slept and not first_neighbor_visit:
            if learned_about_recording_studio_workshop and not completed_recording_studio_workshop:
                menu:
                    "Tell Sam & Michelle about the workshop.":
                        call visit_sam(event="recording_studio_workshop")
                        
                    "Keep it to yourself.":
                        jump visit_sam
            jump visit_sam
        
        "Say hi to neighbor" if first_neighbor_visit:
            $ first_neighbor_visit = False
            jump say_hi_to_neighbor

        "Go on an outing" if has_slept:
            menu:
                "Park":
                    jump park

                "Mall":
                    jump mall_location_options

                "Fancy Restaurant":
                    jump fancy_restaurant

                "Nevermind":
                    jump house_porch_options

        "Attend the pride festival" if helped_sam_speech and helped_sam_outfit and helped_sam_rehearse:
            jump pride_festival