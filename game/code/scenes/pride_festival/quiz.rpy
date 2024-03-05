label quiz:

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
            "Incorrect. LGBTQIA+ stands for Lesbian, Gay, Bisexual, Transgender, Queer/Questioning, Intersex, Asexual, and more"
        "Lesbian, Gay, Bisexual, Transgender, Queer/Questioning, Intersex, Asexual, and more":
            "Correct"
            $ total_points += 1
        "Limited, Gendered, Biased, Transformed, Queer, Individual, Aware, Accepted":
            "Incorrect. LGBTQIA+ stands for Lesbian, Gay, Bisexual, Transgender, Queer/Questioning, Intersex, Asexual, and more"
        "None of the above":
            "Incorrect. LGBTQIA+ stands for Lesbian, Gay, Bisexual, Transgender, Queer/Questioning, Intersex, Asexual, and more"
    menu:
        # Question 2
        "Question 2: What is the significance of the Stonewall Riots in LGBTQIA+ history?"

        "An isolated incident with no impact on LGBTQIA+ rights":
            "Incorrect. The significance of the Stonewall Riots in LGBTQIA+ history is that it was a turning point, leading to increased visibility and activism for LGBTQIA+ rights"
        "A celebration of LGBTQIA+ culture":
            "Incorrect. The significance of the Stonewall Riots in LGBTQIA+ history is that it was a turning point, leading to increased visibility and activism for LGBTQIA+ rights"
        "A turning point, leading to increased visibility and activism for LGBTQIA+ rights":
            "Correct"
            $ total_points += 1
        "None of the above":
            "Incorrect. The significance of the Stonewall Riots in LGBTQIA+ history is that it was a turning point, leading to increased visibility and activism for LGBTQIA+ rights"
    menu:
        # Question 3
        "Question 3: What is gender dysphoria?"

        "Distress due to a mismatch between a person's gender identity and sex assigned at birth":
            "Correct"
            $ total_points += 1
        "Feeling comfortable with one's gender identity":
            "Incorrect. Gender dysphoria is distress due to a mismatch between a person's gender identity and sex assigned at birth"
        "A mental disorder unrelated to gender identity":
            "Incorrect. Gender dysphoria is distress due to a mismatch between a person's gender identity and sex assigned at birth"
        "None of the above":
            "Incorrect. Gender dysphoria is distress due to a mismatch between a person's gender identity and sex assigned at birth"
    menu:
        # Question 4
        "Question 4: What is the meaning of the Pride flag's colors?"

        "Each color represents different aspects of the LGBTQIA+ community":
            "Correct"
            $ total_points += 1
        "It symbolizes specific gender identities":
            "Incorrect. Each color of the pride flag represents different aspects of the LGBTQIA+ community"
        "It has no specific meaning":
            "Incorrect. Each color of the pride flag represents different aspects of the LGBTQIA+ community"
        "None of the above":
            "Incorrect. Each color of the pride flag represents different aspects of the LGBTQIA+ community"
    menu:
        # Question 5
        "Question 5: What does 'coming out' refer to in LGBTQIA+ context?"

        "The process of revealing one's sexual orientation or gender identity":
            "Correct"
            $ total_points += 1
        "The process of keeping one's identity hidden":
            "Incorrect. It's the process of revealing one's sexual orientation or gender identity"
        "A celebration of LGBTQIA+ culture":
            "Incorrect. It's the process of revealing one's sexual orientation or gender identity"
        "None of the above":
            "Incorrect. It's the process of revealing one's sexual orientation or gender identity"
    menu:
        # Question 6
        "Question 6: What does the term 'cisgender' mean?"

        "A person whose gender identity matches the sex assigned at birth":
            "Correct"
            $ total_points += 1
        "A person attracted to multiple genders":
            "Incorrect. Cisgender means a person whose gender identity matches the sex assigned at birth"
        "A gender-neutral term for individuals in the LGBTQIA+ community":
            "Incorrect. Cisgender means a person whose gender identity matches the sex assigned at birth"
        "None of the above":
            "Incorrect. Cisgender means a person whose gender identity matches the sex assigned at birth"
    menu:
        # Question 7
        "Question 7: What is a 'safe space' in the LGBTQIA+ context?"

        "An environment where LGBTQIA+ individuals feel accepted and supported":
            "Correct"
            $ total_points += 1
        "A restricted area for LGBTQIA+ individuals only":
            "Incorrect. It's an environment where LGBTQIA+ individuals feel accepted and supported"
        "A term used to describe LGBTQIA+ clubs":
            "Incorrect. It's an environment where LGBTQIA+ individuals feel accepted and supported"
        "None of the above":
            "Incorrect. It's an environment where LGBTQIA+ individuals feel accepted and supported"
    menu:
        # Question 8
        "Question 8: What does the acronym 'HIV' stand for?"

        "Human Immunodeficiency Virus":
            "Correct"
            $ total_points += 1
        "Human Immunization Virus":
            "Incorrect. It stands for Human Immunodeficiency Virus"
        "Hormonal Immunization Variant":
            "Incorrect. It stands for Human Immunodeficiency Virus"
        "None of the above":
            "Incorrect. It stands for Human Immunodeficiency Virus"
    menu:
        # Question 9
        "Question 9: What does 'allyship' mean in the LGBTQIA+ community?"

        "Supporting and advocating for the rights of LGBTQIA+ individuals":
            "Correct"
            $ total_points += 1
        "Opposing the rights of LGBTQIA+ individuals":
            "Incorrect. It means supporting and advocating for the rights of LGBTQIA+ individuals"
        "Being neutral toward LGBTQIA+ issues":
            "Incorrect. It means supporting and advocating for the rights of LGBTQIA+ individuals"
        "None of the above":
            "Incorrect. It means supporting and advocating for the rights of LGBTQIA+ individuals"
    menu:
        # Question 10
        "Question 10: What is 'gender expression'?"

        "How a person presents their gender through appearance and behavior":
            "Correct"
            $ total_points += 1
        "A medical term for gender identity":
            "Incorrect. Gender expression is how a person presents their gender through appearance and behavior"
        "An outdated term related to gender":
            "Incorrect. Gender expression is how a person presents their gender through appearance and behavior"
        "None of the above":
            "Incorrect. Gender expression is how a person presents their gender through appearance and behavior"
    menu:
        # Question 11
        "Question 11: What is the purpose of International Transgender Day of Visibility?"

        "To celebrate transgender people and raise awareness of discrimination faced by them":
            "Correct"
            $ total_points += 1
        "To exclude transgender individuals from public view":
            "Incorrect. It's to celebrate transgender people and raise awareness of discrimination faced by them"
        "To promote cisgender rights":
            "Incorrect. It's to celebrate transgender people and raise awareness of discrimination faced by them"
        "None of the above":
            "Incorrect. It's to celebrate transgender people and raise awareness of discrimination faced by them"
    menu:
        # Question 12
        "Question 12: What does 'non-binary' mean in terms of gender identity?"
        
        "Identifying outside the traditional binary of male or female":
            "Correct"
            $ total_points += 1
        "Identifying as both male and female":
            "Incorrect. It means identifying outside the traditional binary of male or female"
        "Having no gender identity":
            "Incorrect. It means identifying outside the traditional binary of male or female"
        "None of the above":
            "Incorrect. It means identifying outside the traditional binary of male or female"

    menu:
        # Question 13
        "Question 14: What does 'drag' refer to in LGBTQIA+ culture?"

        "A form of entertainment where individuals dress in clothing typically associated with another gender":
            "Correct"
            $ total_points += 1
        "A religious practice in LGBTQIA+ communities":
            "Incorrect. In LGBTQIA+ culture 'drag' a form of entertainment where individuals dress in clothing typically associated with another gender"
        "A form of protest against LGBTQIA+ rights":
            "Incorrect. In LGBTQIA+ culture 'drag' a form of entertainment where individuals dress in clothing typically associated with another gender"
        "None of the above":
            "Incorrect. In LGBTQIA+ culture 'drag' a form of entertainment where individuals dress in clothing typically associated with another gender"
    menu:
        # Question 14
        "Question 15: What is 'conversion therapy'?"
        
        "A harmful practice aiming to change a person's sexual orientation or gender identity":
            "Correct"
            $ total_points += 1
        "A form of LGBTQIA+ counseling":
            "Incorrect. It's a harmful practice aiming to change a person's sexual orientation or gender identity"
        "An acceptance program for LGBTQIA+ individuals":
            "Incorrect. It's a harmful practice aiming to change a person's sexual orientation or gender identity"
        "None of the above":
            "Incorrect. It's a harmful practice aiming to change a person's sexual orientation or gender identity"

    "Quiz complete! Your total points: [total_points]"

    # Add logic to determine the player's score based on total_points
    if total_points >= 14:
        "You're very knowledgeable about LGBTQIA+ information!"
    elif 10 <= total_points < 14:
        "You have a decent understanding of LGBTQIA+ information."
    else:
        "There's more to explore! Keep learning about LGBTQIA+ information."

    jump pride_festival_options