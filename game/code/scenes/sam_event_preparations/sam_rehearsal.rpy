label sam_rehearsal:
    play music "sunny.mp3" loop
    $ sam_song = []

#Change the song lyric optionsbased on what choices
#the player has made in the story so far.
#So when Sam makes a choice that affects the story add a thing to the array.
    sam "[sam_song]"

    $ helped_sam_rehearse = True

    stop music fadeout 1.0

    show sam smile
    sam "Great thanks! Let's go pick out an outfit!"

    jump sam_outfit