label quiz:
    "A quiz on terms and such"

    "You arrive at the quiz booth. Would you like to start the quiz?"

    if not done_museum:
        "It's recommended that you visit the museum before doing the quiz."

    menu:
        "Start the quiz":
            $ done_quiz = True
            label lgbtqia_plus_quiz:

        "Leave the booth":
            jump pride_festival_options
    $ total_points = 0

    menu:
        "Question 1: What does LGBTQIA+ stand for?"

        "Liberation, Gender, Bisexuality, Transcendence, Queerness, Intersectionality, Allies, Acceptance":
            "Incorrect"
        "Lesbian, Gay, Bisexual, Transgender, Queer/Questioning, Intersex, Asexual, and more":
            "Correct"
            $ total_points += 1
        "Limited, Gendered, Biased, Transformed, Queer, Individual, Aware, Accepted":
            "Incorrect"
        "None of the above":
            "Incorrect"
    menu:
        # Question 2
        "Question 2: What is the significance of the Stonewall Riots in LGBTQIA+ history?"

        "An isolated incident with no impact on LGBTQIA+ rights":
            "Incorrect"
        "A celebration of LGBTQIA+ culture":
            "Incorrect"
        "A turning point, leading to increased visibility and activism for LGBTQIA+ rights":
            "Correct"
            $ total_points += 1
        "None of the above":
            "Incorrect"
    menu:
        # Question 3
        "Question 3: What is gender dysphoria?"

        "Distress due to a mismatch between a person's gender identity and sex assigned at birth":
            "Correct"
            $ total_points += 1
        "Feeling comfortable with one's gender identity":
            "Incorrect"
        "A mental disorder unrelated to gender identity":
            "Incorrect"
        "None of the above":
            "Incorrect"
    menu:
        # Question 4
        "Question 4: What is the meaning of the Pride flag's colors?"

        "Each color represents different aspects of the LGBTQIA+ community":
            "Correct"
            $ total_points += 1
        "It symbolizes specific gender identities":
            "Incorrect"
        "It has no specific meaning":
            "Incorrect"
        "None of the above":
            "Incorrect"
    menu:
        # Question 5
        "Question 5: What does 'coming out' refer to in LGBTQIA+ context?"

        "The process of revealing one's sexual orientation or gender identity":
            "Correct"
            $ total_points += 1
        "The process of keeping one's identity hidden":
            "Incorrect"
        "A celebration of LGBTQIA+ culture":
            "Incorrect"
        "None of the above":
            "Incorrect"
    menu:
        # Question 6
        "Question 6: What does the term 'cisgender' mean?"

        "A person whose gender identity matches the sex assigned at birth":
            "Correct"
            $ total_points += 1
        "A person attracted to multiple genders":
            "Incorrect"
        "A gender-neutral term for individuals in the LGBTQIA+ community":
            "Incorrect"
        "None of the above":
            "Incorrect"
    menu:
        # Question 7
        "Question 7: What is a 'safe space' in the LGBTQIA+ context?"

        "An environment where LGBTQIA+ individuals feel accepted and supported":
            "Correct"
            $ total_points += 1
        "A restricted area for LGBTQIA+ individuals only":
            "Incorrect"
        "A term used to describe LGBTQIA+ clubs":
            "Incorrect"
        "None of the above":
            "Incorrect"
    menu:
        # Question 8
        "Question 8: What does the acronym 'HIV' stand for?"

        "Human Immunodeficiency Virus":
            "Correct"
            $ total_points += 1
        "Human Immunization Virus":
            "Incorrect"
        "Hormonal Immunization Variant":
            "Incorrect"
        "None of the above":
            "Incorrect"
    menu:
        # Question 9
        "Question 9: What does 'allyship' mean in the LGBTQIA+ community?"

        "Supporting and advocating for the rights of LGBTQIA+ individuals":
            "Correct"
            $ total_points += 1
        "Opposing the rights of LGBTQIA+ individuals":
            "Incorrect"
        "Being neutral toward LGBTQIA+ issues":
            "Incorrect"
        "None of the above":
            "Incorrect"
    menu:
        # Question 10
        "Question 10: What is 'gender expression'?"

        "How a person presents their gender through appearance and behavior":
            "Correct"
            $ total_points += 1
        "A medical term for gender identity":
            "Incorrect"
        "An outdated term related to gender":
            "Incorrect"
        "None of the above":
            "Incorrect"
    menu:
        # Question 11
        "Question 11: What is the purpose of International Transgender Day of Visibility?"

        "To celebrate transgender people and raise awareness of discrimination faced by them":
            "Correct"
            $ total_points += 1
        "To exclude transgender individuals from public view":
            "Incorrect"
        "To promote cisgender rights":
            "Incorrect"
        "None of the above":
            "Incorrect"
    menu:
        # Question 12
        "Question 12: What does 'non-binary' mean in terms of gender identity?"
        
        "Identifying outside the traditional binary of male or female":
            "Correct"
            $ total_points += 1
        "Identifying as both male and female":
            "Incorrect"
        "Having no gender identity":
            "Incorrect"
        "None of the above":
            "Incorrect"
    menu:
        # Question 13
        "Question 13: What does the acronym 'LGBTQIA+' stand for?"

        "Lesbian, Gay, Bisexual, Transgender, Queer/Questioning, Intersex, Asexual, and more":
            "Correct"
            $ total_points += 1
        "Limited, Gendered, Biased, Transformed, Queer, Individual, Aware, Accepted":
            "Incorrect"
        "None of the above":
            "Incorrect"
    menu:
        # Question 14
        "Question 14: What does 'drag' refer to in LGBTQIA+ culture?"

        "A form of entertainment where individuals dress in clothing typically associated with another gender":
            "Correct"
            $ total_points += 1
        "A religious practice in LGBTQIA+ communities":
            "Incorrect"
        "A form of protest against LGBTQIA+ rights":
            "Incorrect"
        "None of the above":
            "Incorrect"
    menu:
        # Question 15
        "Question 15: What is 'conversion therapy'?"
        
        "A harmful practice aiming to change a person's sexual orientation or gender identity":
            "Correct"
            $ total_points += 1
        "A form of LGBTQIA+ counseling":
            "Incorrect"
        "An acceptance program for LGBTQIA+ individuals":
            "Incorrect"
        "None of the above":
            "Incorrect"

    "Quiz complete! Your total points: [total_points]"

    # Add logic to determine the player's score based on total_points
    if total_points >= 15:
        "You're very knowledgeable about LGBTQIA+ information!"
    elif 10 <= total_points < 15:
        "You have a decent understanding of LGBTQIA+ information."
    else:
        "There's more to explore! Keep learning about LGBTQIA+ information."

    jump pride_festival_options


                    
    