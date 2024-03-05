label lgbtqia_plus_history:
    
    scene museum

    menu lgbtqia_plus_history_options:
        "The Stonewall Riots (June 28, 1969)":
            "In 1969, a riot at the Stonewall Inn (later known as the Stonewall Riots) became a
            turning point. Though few records of the actual raid and riots that followed exist, the
            oral history of that time has been captured by the participants -- both those who
            rioted and the police."

            "The Stonewall Riots ignited after a police raid took place at the
            Stonewall Inn. The tension from ongoing harassment galvanized
            the LGBTQ community to riot for six days. The protest through the streets of New
            York City is memorialized as the annual Gay Pride parades that are now celebrated
            around the world. "
            if not seen_stonewall_riots:
                $ seen_stonewall_riots = True
                $ history_lover.add_progress(1)
                $ renpy.block_rollback()

            jump lgbtqia_plus_history_options

        "Harvey Milk (1930-1978)":
            "When he won the election to the San Francisco Board of Supervisors in 1977, Harvey
            Milk made history as the first openly gay elected official in California, and one of the
            first in the United States. His camera store and campaign headquarters at 575 Castro
            Street (and his apartment above it)"
        
            "were centers of community activism for a wide
            range of human rights, environmental, labor, and neighborhood issues. During his
            tenure as supervisor, he helped pass a gay rights ordinance for the city of San
            Francisco that prohibited anti-gay discrimination in housing and employment."
            if not seen_harvey_milk:
                $ seen_harvey_milk = True
                $ history_lover.add_progress(1)
                $ renpy.block_rollback()
            
            jump lgbtqia_plus_history_options

        "National March on Washington for Lesbian and Gay Rights (1979)":
            "Marches on Washington, D.C. can serve many functions: to protest peacefully, to
            make visible the commitment and volume of support behind a movement, to
            mobilize and nationalize otherwise more fractured, local efforts to organize."

            "The LGBTQ community and its allies have marched on the nation's capital on numerous
            occasions, beginning with a march and rally that took place on October 14, 1979. "
            if not seen_national_march:
                $ seen_national_march = True
                $ history_lover.add_progress(1)
                $ renpy.block_rollback()
            
            jump lgbtqia_plus_history_options

        "The HIV/AIDS Epidemic (1980s)":
            "The United States was the focal point of the HIV/AIDS epidemic of the 1980s. The
            disease was first noticed en masse by doctors who treated gay men in Southern
            California, San Francisco, and New York City in 1981. When cases of AIDS first
            emerged in the U.S.,"

            "they tended to originate among either men who had sex with
            other men, hemophiliacs, and heroin users. The prevalence of the disease among gay
            men in the U.S. in the 80s and 90s initially resulted in a stigma against homosexuals
            and a general fear and misunderstanding regarding how AIDS was spread."
            
            "However, as celebrities like Rock Hudson and Freddie Mercury revealed that they had the
            disease, and Magic Johnson came forward with HIV, and dedicated his retirement to
            educating others about the virus, attitudes began to change."
            if not seen_hiv_aids_epidemic:
                $ seen_hiv_aids_epidemic = True
                $ history_lover.add_progress(1)
                $ renpy.block_rollback()
            
            jump lgbtqia_plus_history_options

        "Don't Ask, Don't Tell and DOMA (1990s)":
            "In 1993, the “Don't Ask, Don't Tell” policy was instituted within the U.S. military,
            permitting gays to serve in the military but banning homosexual activity. President
            Clinton's original intention to revoke the prohibition against gays in the military was
            met with stiff opposition; this compromise, which led to the discharge"

            "of thousands of men and women in the armed forces, was the result. On April 25, an estimated
            800,000 to one million people participated in the March on Washington for Lesbian,
            Gay, and Bi Equal Rights and Liberation. The march was a response to “Don't Ask
            Don't Tell”, Amendment 2 in Colorado,"
            
            "and rising hate crimes and ongoing
            discrimination against the LGBT community. Amendment 2 in Colorado, sought to
            deny gays and lesbians protection against discrimination, claiming that such rights
            were 'special rights.' "

            "DOMA"

            "The Defense of Marriage Act (DOMA) was enacted in 1996 and defined marriage, at
            the federal level, as the union of one man to one woman. DOMA was primarily
            brought about by a fear that if states granted same-sex couples the right to marry, "

            "the federal government, and other states would have to honor those marriages. DOMA allowed states to refuse to recognize same-sex marriages granted under the laws of
            other states. While DOMA did not bar individual states from recognizing same-sex
            marriage, it imposed constraints on the benefits"

            "that all legally married same-sex couples could receive. These benefits included insurance benefits for government
            employees, social security survivors' benefits, immigration assistance, ability to file
            for joint bankruptcy, and the filing of joint tax returns, financial aid eligibility
            otherwise available"
            
            "to heterosexual married couples, and other laws that applied to
            heterosexual married couples"
            if not seen_dont_ask_dont_tell:
                $ seen_dont_ask_dont_tell = True
                $ history_lover.add_progress(1)
                $ renpy.block_rollback()
            
            jump lgbtqia_plus_history_options

        "Proposition 8 (2008-2013)":
            "Prop 8, was a California ballot proposition and a state constitutional amendment
            passed in the 2008 California state election. The proposition was created by
            opponents of same-sex marriage brought before the California Supreme Court."

            "As an amendment, it was ruled constitutional by the California Supreme Court in 2009.
            Among the advocates for Prop 8 were religious organizations, most notably the
            Roman Catholic church and the Church of Jesus Christ of Latter Day Saints."

            "Once Prop 8 had been upheld by the state courts, two same-sex couples filed a lawsuit
            against Prop 8 in the U.S. District Court for the Northern District of California
            in Hollingsworth v. Perry."

            "On June 26, 2013, the U.S. Supreme Court issued its decision in Hollingsworth v. Perry, ruling that proponents of initiatives like
            Proposition 8 did not possess legal standing to defend the resulting law in federal
            court."
            
            "Thus, Prop 8 was held unconstitutional and Governor Brown was free to
            permit same-sex marriages to recommence."
            if not seen_proposition_8:
                $ seen_proposition_8 = True
                $ history_lover.add_progress(1)
                $ renpy.block_rollback()

            jump lgbtqia_plus_history_options

        "Obergefell v Hodges - Marriage Equality (2015)":
            "2015 - The U.S. Supreme Court makes same-sex marriages legal in all 50 states in Obergefell v. Hodges."

            "The following is a quote from that decision: "

            '''“No union is more profound than marriage, for it embodies the highest ideals of
            love, fidelity, devotion, sacrifice, and family. In forming a marital union, two
            people become something greater than once they were.'''

            '''As some of the
            petitioners in these cases demonstrate, marriage embodies a love that may
            endure even past death. It would misunderstand these men and women to say
            they disrespect the idea of marriage. Their plea is that they do respect it, respect
            it so deeply that they seek to find its fulfillment for themselves.'''

            '''Their hope is not
            to be condemned to live in loneliness, excluded from one of civilization's oldest
            institutions. They ask for equal dignity in the eyes of the law. The Constitution
            grants them that right.”'''
            if not seen_obergefell_v_hodges:
                $ seen_obergefell_v_hodges = True
                $ history_lover.add_progress(1)
                $ renpy.block_rollback()

            jump lgbtqia_plus_history_options

        "Back to the main museum area":
            jump museum_options