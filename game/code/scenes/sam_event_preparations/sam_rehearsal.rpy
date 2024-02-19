label sam_rehearsal:
    play music "sunny.mp3" loop
    $ sam_song = []

    "You and Sam rehearse for a bit."

    $ helped_sam_rehearse = True

    stop music fadeout 1.0

    show sam smile
    sam "Great thanks! Let's go pick out an outfit!"

    jump sam_outfit