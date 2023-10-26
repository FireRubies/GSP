label sam_outfit:

    show sam neutral

    scene fashion store

    sam "So I was thinking something really colorful."

    #Add more dresses. MAYBE also have dresses impacted by player choices.

    menu sam_outfits:
        "Green dress":
            show green dress
            menu:
                "Choose this dress":
                    $ sam_dress = "green dress"
                "Choose another dress":
                    scene fashion store
                    jump sam_outfits

        "Red dress":
            show red dress
            menu:
                "Choose this dress":
                    $ sam_dress = "red dress"
                "Choose another dress":
                    scene fashion store
                    jump sam_outfits

    scene fashion store

    sam "[sam_dress]"

    sam "Thanks for helping me choose a dress! Now onto the speech!"

    $ helped_sam_outfit = True

    jump sam_speech