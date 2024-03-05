label middle_school:
    scene middle school

    show sam frown at left
    show michelle at right
    "You & Sam & M visit Sam's middle school. She talks about being bullied and stuff."

    sam "Ah this place."

    "Michelle hugs Sam tightly."

    menu:
        "Do nothing":
            "You stand there awkwardly, unsure of what to do."

        "Ask what's wrong":
            you "What's wrong?"

            sam """Mm. Just reminiscing...

            I first came out here...

            I should've waited I think.

            Granted then I wouldn't have met Mi so I guess it was the right decision."""

            show michelle smile

    sam """Anyway... yeah. I got bullied here a lot.
    Some people just didn't understand who I was,

    others... others just thought there was something wrong with me,
    and others were just mean..."""

    "Sam walks inside the school and we follow her."

    scene lockers

    "Sam stares at her locker. Faded writing says things like 'tranny' and 'ur a man'."
    "You notice Sam's eyes start to water."

    menu:
        "Hug Sam":
            "You reach out and wrap your arms around Sam. Michelle soon joins you in hugging Sam."

            "As you both hug her she breaks down into tears."

            "After a while she stops crying."

            sam "T-thank you both... I. I needed that."
            $ hug_it_out.grant();

        "Stare at the locker too":
            "You stare at the locker and hear Sam breaking down into tears. You look at see Michelle hugging her."

            "After a while she stops crying."

            sam "S-. Sorry about that. I didn't mean to breakdown like that."

    sam "I-. I'd thought I'd gotten over all this stuff but I guess I didn't."

    sam "Well... onto the hospital I guess?"

    menu:
        "Move on to the hospital":
            you "Yeah if you're feeling up to it."

            show sam smile
            sam "Yeah. It's all uphill from here!"

            michelle "That's my girl."

        "Wait for a bit":

            "You wait for Sam to calm down quickly, then you head to the hospital."
            #NOTE: Branching path here. Help Sam overcome her past. She'll do this anyway with the song but
            #helping her out early will result in a more confident/powerful song :3

            #NOTE: After helping Sam have there be yet another branching path! woot! Maybe make this a different
            #line? like... the player can go to the playground or something after looking at the lockers
            #with Sam and then that's where you discover the kid? Yeah.
            #Have a child character be here. Give the player the option to sidetrack a bit and help the child
            #with issues at their school relating to inclusivity later!!! as in only visit for this storyline
            #now but after the sam visiting stuff unlock the ability to travel to the hospital and the school
            #in the menu!

    jump hospital
            


    