label finished_game:
    "Thanks for playing! I really appreciate it! :D"
    "Now you can either look at the credits for the game or just go back to the menu. The choice is yours."

    menu:
        "Main Menu":
            $ MainMenu(confirm=False)
            
        "Credits":
            $ credits_speed = 25
            image credits_image = "credits_image.jpg"
            play music "menu.mp3"
            scene black
            show credits_image at Move((0.5, 1.0), (0.5, -1.0), credits_speed, xanchor=0.5, yanchor=0) with Pause(credits_speed+10)