label mall_location_options:

    scene mall

    menu:
        "Grocer":
            jump grocer 

        "Recording Studio":
            if visited_recording_studio == False:
                call recording_studio(event="first_visit") from _call_recording_studio
            jump recording_studio

        "Fashion Store":
            jump fashion_store

        "Gym":
            jump gym

        "Salon":
            jump salon

        "Go Home":
            jump house_porch_options