label wander:
    $ done_wander = True

    if len(wanderable_places) < 1:
        "You wander around but you can't find anything."
    else:
        $ renpy.jump(renpy.random.choice(wanderable_places))

    jump pride_festival_options