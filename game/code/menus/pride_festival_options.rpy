menu pride_festival_options:
    "Wander around" if not done_wander:
        jump wander
        # random encounters
    "Go to a booth" if not done_quiz or not done_museum:
        menu:
            "The Quiz" if not done_quiz:
                jump quiz
            "The Musuem" if not done_museum:
                jump museum
                
    "The Stage" if done_quiz and done_wander and done_museum:
        jump stage