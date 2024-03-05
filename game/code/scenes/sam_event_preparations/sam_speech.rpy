label sam_speech:
    sam "Okay so let's make it line by line."


    # Add lots of custom stuff here. The options for dialogue change
    #based on the player's choices and stuff!

    menu:
        "Hello everyone! Welcome to the annual Pride Festival!":
            $ sam_speech += ["Hello everyone! Welcome to the annual Pride Festival!"]
        "Welcome everyone!":
            $ sam_speech += ["Welcome everyone!"]

    menu:
        "It's great you're all here!":
            $ sam_speech += ["It's great you're all here!"]
        "I'm glad you're all here!":
            $ sam_speech += ["I'm glad you're all here!"]

    menu:
        "Should we get this party started?":
            $ sam_speech += ["Should we get this party started?"]
        "Let's make some noise and get partying!" :
            $ sam_speech += ["Let's make some noise and get partying!"]

    $ helped_sam_speech = True

    sam "Yay! Thanks! We got through everything! I feel really prepared for the pride festival now!"

    show sam smile 

    sam "Hey do you wanna go to the festival with me and Mi?"

    menu:
        "Yes":
            $ going_to_festival_with_sam = True
            you "Yeah sure! That sounds like a blast! When are we leaving?"

            sam "Just let us know when you're ready."
        "No":
            you "Thanks for the offer! I'm gonna take my own car though."

            show sam sad 
            sam "Oh okay."

            show sam smile
            "Well we'll see you there!"

    jump house_porch_options
    
    #Put thing here. Work on the actual parade scene! Have lots of events
    #info sessions, etc.