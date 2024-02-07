label lgbtqia_plus_important_info:
    #TODO: Achievement for going through all the important info options.

    menu:
        "Choose a topic to learn about:"

        "Respecting Pronouns":
            "Respecting preferred pronouns (like they/them) is crucial for inclusivity."
            if not seen_respecting_pronouns:
                $ seen_respecting_pronouns = True
                $ important_info_lover.add_progress(1)

        "Heteronormativity":
            "Society's assumption of heterosexuality as the default can be excluding."
            if not seen_heteronormativity:
                $ seen_heteronormativity = True
                $ important_info_lover.add_progress(1)

        "Gender Dysphoria":
            "Some transgender individuals experience distress due to a misalignment between their gender identity and sex assigned at birth."
            if not seen_gender_dysphoria:
                $ seen_gender_dysphoria = True
                $ important_info_lover.add_progress(1)

        "Bi/Pan/Polysexuality":
            "Attraction to multiple genders differs from bisexuality's historical binary understanding."
            if not seen_bi_pan_polysexuality:
                $ seen_bi_pan_polysexuality = True
                $ important_info_lover.add_progress(1)

        "Asexuality":
            "A spectrum where individuals experience little or no sexual attraction."
            if not seen_asexuality:
                $ seen_asexuality = True
                $ important_info_lover.add_progress(1)

        "LGBTQ+ Youth Homelessness":
            "Disproportionately high due to family rejection."
            if not seen_lgbtq_youth_homelessness:
                $ seen_lgbtq_youth_homelessness = True
                $ important_info_lover.add_progress(1)

        "Microaggressions":
            "Subtle, often unintentional, discriminatory remarks or actions."
            if not seen_microaggressions:
                $ seen_microaggressions = True
                $ important_info_lover.add_progress(1)

        "Legal Protections":
            "Many countries lack explicit laws protecting LGBTQ+ individuals from discrimination."
            if not seen_legal_protections:
                $ seen_legal_protections = True
                $ important_info_lover.add_progress(1)

        "Elders in the Community":
            "Older LGBTQ+ individuals faced greater discrimination and unique challenges."
            if not seen_elders_in_community:
                $ seen_elders_in_community = True
                $ important_info_lover.add_progress(1)

        "Global Variances":
            "LGBTQ+ rights and acceptance vary significantly worldwide."
            if not seen_global_variances:
                $ seen_global_variances = True
                $ important_info_lover.add_progress(1)

    menu lgbtqia_plus_important_info_options:
        "Back to the main museum area":
            jump museum_options

    #Add an achievement for getting all the exhibit achievements.