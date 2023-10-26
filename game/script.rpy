# The script of the game goes in this file.


# The game starts here.
# default quest = Manager()

# define arrival = ( # Add your quests below, don't forget the commas !
#     Quest("intro01", _("Check out your new house"), _("Arrival"), "unlocked"), # By default the quests have the state "pending", but you can change it by adding a state keyword
#     Quest("intro02", _("Unpack your stuff"), _("Arrival"), "unlocked"),
#     Quest("intro03", _("Go to sleep"), _("Arrival"), "unlocked"),
#     # Quest("intro04", _("Show all the steps"), _("Introduction")),
#     # Quest("intro05", _("Displaying the in progress quest"), _("Introduction")),
#     # Quest("intro06", _("Manage the player's progress"), _("Introduction")),
#     )

# define chapter2 = (
#     Quest("gen01", _("Do something"), _("General")),
#     Quest("gen02", _("Do something else"), _("General")),
#     Quest("item1.1", _("Item 1"), _("Category 1")),
#     Quest("item1.2", _("Item 2"), _("Category 1")),
#     Quest("item1.3", _("Item 3"), _("Category 1")),
#     Quest("item2.1", _("Item 1"), _("Category 2")),
#     Quest("item2.2", _("Item 2"), _("Category 2")),
#     Quest("item2.3", _("Item 3"), _("Category 2")),
#     )

label start:
    #show screen diary_open_btn
    #$ quest.load(arrival)

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    #Overall notes. The players choices about discrimination and stuff throughout the story will affect the final ending. If the final ending turns out to be the pride parade the player's choices will be calculated and affect Sam's confidence.

    scene driving to player house
    with dissolve

    pause 3

    scene parked outside player house
    with fade

    pause 1.0

    #Play car door opening sound and player gets out. Then play
    #car door closing sound.

    show you at right

    #NOTE: Implement inventory later on!
    # "You stop at your new house and get out of your car."
    # $ jane_inv = Inventory("Jane")
    # $ cookbook = list()
    # $ eye = Item(name="Eyeball", desc="A human eyeball, how creepy!", value=250)
    # $ jane_inv.take(eye, 5)
    # show screen inventory_screen(jane_inv) 

    #$ can_visit_sam = False
    $ first_neighbor_visit = True
    $ unpacked = False
    $ has_slept = False
    $ peeked_through_window = False
    $ player_name = "You"
    $ player_pronouns = "They/Their"
    $ sam_welcome_to_neighborhood = False
    
    $ completed_recording_studio_workshop = False

    #Helping Sam variables
    $ helped_sam_rehearse = False
    $ helped_sam_outfit = False
    $ helped_sam_speech = False

    #Song
    $ sam_song = []
    $ sam_speech = []

    $ sam_dress = ""

    $ going_to_festival_with_sam = False
    
    jump house_porch_options



    #This ends the game.
    return