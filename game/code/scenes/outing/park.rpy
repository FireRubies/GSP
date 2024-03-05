label park:
    scene park
    "You see a beautiful park."

    menu park_options:
        "Jog around":
            "You lace up your sneakers and set off on the jogging path.  Leaves crunch underfoot, and your breath plumes in the cool air."

        "Go for a bike ride":
            "The wind whips through your hair as you pedal down the bike trail.  Sunlight dapples through the trees."

        "Just relax":
            "You find a quiet spot beneath a shady tree.  Birdsong fills the air as you close your eyes and let the worries of the day melt away."

        "Leave the park":
            jump house_porch_options

    jump park_options

    #At the park you can
    # sit on a bench
    # jog around
    # bike
    # each action will randomly start a short event. Choosing from the list of characters each action has.
    # you can only find a character at the park if you've already met them in the game.
    # sitting on a bench
    # Jay, Bob, Rob
    # jogging
    # Sam, Michelle, Jordan
    # biking
    # Alex, Maxi, Liam

    jump house_porch_options