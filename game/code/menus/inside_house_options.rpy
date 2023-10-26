label inside_house_options:

    scene player house inside
    with dissolve

    menu:
        "Leave house":
            jump house_porch_options
    
        "Unpack" if not unpacked:
            $ unpacked = True
            "You unpack all your stuff"
            jump inside_house_options

        "Sleep" if unpacked and not has_slept:
            "You plop down on your bed and fall fast asleep."
            if not has_slept:
                $ has_slept = True
                $ first_neighbor_visit = False
                jump sam_welcome_to_neighborhood

            "You plop down on your bed and fall fast asleep."
            jump inside_house_options

        "Relax" if unpacked:
            "You spend a bit of time lounging around your house."
            jump inside_house_options

        "Clean" if unpacked:
            "You take out a broom and sweep down your whole house."
            jump inside_house_options