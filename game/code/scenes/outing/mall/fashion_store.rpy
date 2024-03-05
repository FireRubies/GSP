label fashion_store:
    scene fashion store
    "The racks of the fashion store burst with color and texture. Dresses shimmer, suits look sharp, and shelves overflow with accessories."
    show jay smile at center

    if completed_recording_studio_workshop:
        "You see Jay running their fingers over a silky dress, then pausing by a rack of tailored suits. A sparkle catches in their eye."
    else:
        "You see someone running their fingers over a silky dress, then pausing by a rack of tailored suits. A sparkle catches in their eye."

    "You leave as to not interrupt them."

    jump mall_location_options