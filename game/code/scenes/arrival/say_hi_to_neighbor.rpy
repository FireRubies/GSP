label say_hi_to_neighbor:

    scene sams house
    with dissolve

    "You approach your neighbor's house.  As you get close to the house you hear sobbing coming from inside the house, and the sound of someone speaking, likely trying to comfort the crying person."

    menu:
        "Peek through the window":
            scene peeking through window
            "You see a girl with her arm wrapped around another girl who's weeping. The sad girl is holding a blank piece of sheet music. There's a guitar in the corner of the room."
            $ peeked_through_window = True
            $ nosy_neighbor.grant()
            jump house_porch_options

        "Back off and go back to your house":
            "You back off and go back to your house"
            $ knower_of_boundaries.grant()
            jump house_porch_options