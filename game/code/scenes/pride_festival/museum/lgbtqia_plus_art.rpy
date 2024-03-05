label lgbtqia_plus_art:
    #TODO: Achievement for going through all the art options.

    scene museum
    
    menu:
        "The Transformation":
            show the transformation
            '''"Lili Elbe was a Danish transgender artist who is best known for her pioneering gender confirmation surgeries in the early 20th century.
            The Transformation is not a traditional performance piece, but a documentation archive that shows the process of Elbe's transition,
            from the early stages of hormone therapy to the final surgery that would complete her transformation.
            It was later used as a base for the movie, Danish Girl (2015). The Transformation piece is both intimate and confrontational,
            as Elbe uses her own body to challenge traditional gender norms and explore the limits of medical and social definitions of gender." 
            
            Nicolene, Burger, “Transgender Art - Experiencing Gender Through Trans Art.” Art in Context. June 5, 2023. URL: https://artincontext.org/transgender-art/
            '''

            if not seen_the_transformation:
                $ seen_the_transformation = True
                $ art_lover.add_progress(1)
                $ renpy.block_rollback()

        "Self Portrait":
            show self portrait
            '''"Claude Cahun was a French artist who is best known for their self-portrait photographs, which often explored themes of gender and identity.
            This particular painting, Self-Portrait, depicts the artist in a suit and tie, with short hair and a stern expression.
            The androgynous appearance of the figure challenges traditional gender norms, and suggests a rejection of binary gender categories.
            The stark, black-and-white palette further emphasizes the artist's uncompromising and defiant stance." 
            
            Nicolene, Burger, “Transgender Art - Experiencing Gender Through Trans Art.” Art in Context. June 5, 2023. URL: https://artincontext.org/transgender-art/
            '''

            if not seen_self_portrait:
                $ seen_self_portrait = True
                $ art_lover.add_progress(1)
                $ renpy.block_rollback()

        "The Pride Flag":
            show pride Flag

            """The pride flag has gone through many interations over the years to keep up with the changing landscape of the LGBTQIA+ community.
            Instead of just being only a rainbow flag it now includes the trans flag in it! The Pride Flag will definitely evolve even more as time goes on.
            """

            if not seen_the_pride_flag:
                $ seen_the_pride_flag = True
                $ art_lover.add_progress(1)
                $ renpy.block_rollback()

        "Back to the main museum area":
            jump museum_options

    jump lgbtqia_plus_art