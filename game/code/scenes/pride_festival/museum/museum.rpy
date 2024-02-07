label museum:
    "A place showcasing LGBTQ+ history and stuff."

    menu museum_options:
        "History Section":
            jump lgbtqia_plus_history
        "Art Section":
            jump lgbtqia_plus_art
        "Important Info Section":
            jump lgbtqia_plus_important_info
        "Leave the museum":
            $ done_museum = True
            jump pride_festival_options

        #TODO: Achievements
            #Achievement for visiting each of the three different sections.
            #Achievement for going through every exhibit!!!