label face_painting:

    $ wanderable_places.remove("face_painting")

    scene face painting

    if going_to_festival_with_sam:

        "Hm, check out that booth over there! Looks like they're doing face painting."

        menu:
            "Approach the booth":
                you "Let's go see what's happening at the face painting booth."
                sam "That sounds like fun! I've always wanted to get my face painted."
                michelle "Me too! It'll be a great way to get into the spirit of the festival."

            "Continue exploring the festival":
                "Actually, let's keep wandering around and see what else is going on."

        you "Hi!"

        jay "Hello!"

        menu:
            "Compliment the artwork":
                you "Wow, these designs are amazing! You all are so talented."
                jay "Thank you! We put a lot of love into our work."
                michelle "It's really impressive. I'm loving the sense of community here."
                sam "Definitely. It's inspiring to see everyone come together like this."

            "Express interest in getting your face painted":
                you "I've always wanted to try getting my face painted. Can I join in?"
                jay "Of course! We have plenty of designs to choose from."
                michelle "This is going to be so much fun!"
                sam "I can't wait to see how mine turns out."

            "Ask about the significance of the designs":
                you "These designs look so meaningful. Can you tell me about them?"
                jay "Absolutely! Each design here represents something special to the LGBTQ+ community."
                michelle "That's really beautiful. It's like wearing your pride on your face."
                sam "It's a great way to show solidarity and celebrate who we are."

        you "Hmm. What design to get..."

        menu:
            "Rainbow":
                you "I'm loving that rainbow design! Could I get that?"
                jay "Sure thing! Let's get started."
                michelle "That's going to look amazing on you!"
                sam "Definitely! Rainbows are always a good choice."

            "Alien":
                you "I think I want to go for something a bit more out of this world. How about an alien design?"
                jay "An alien design, huh? That sounds like fun! Let's get creative!"
                sam "Nice choice! Aliens are always a hit."

            "Heart":
                you "I'm feeling the love today. Can you paint a heart on my cheek?"
                jay "Of course! Hearts are always a classic choice. Let's make it extra special!"
                michelle "Aw, that's adorable! It's going to look great on you!"
                sam "Love it! Hearts are timeless."

            "Pride Flag":
                you "I want to show my pride loud and proud! Can you paint the pride flag on my face?"
                jay "Absolutely! Let's celebrate pride together!"
                show sam smile
                show michelle smile
                "Michelle and Sam smile."
                sam "Wooo!"

        you "This is going to look so cool! Thanks for doing this."

        michelle "Yeah thanks!"

        you "This turned out even better than I imagined!"
        jay "Yeah you look great!"

        menu:
            "Take a photo":
                you "This is too good not to capture! Let's take a photo together."
                jay "Absolutely! Strike a pose!"
                michelle "Say cheese, everyone!"
                sam "This is going to be a great memory!"

            "Decline the photo":
                you "I'm going to keep this moment just for me, but thanks for offering."
                jay "No problem! Enjoy the rest of the festival."
                michelle "We'll make sure to remember it for you!"
                sam "Let us know if you change your mind."

        "Feeling pumped and ready to show off my new face paint, I say goodbye to the Jay and head back into the festival with Sam & Michelle."

    else:

        you "Hm, check out that booth over there! Looks like they're doing face painting."

        menu:
            "Approach the booth":
                you "Let's go see what's happening at the face painting booth."

            "Continue exploring the festival":
                you "Actually, let's keep wandering around and see what else is going on."

        you "Hi!"

        jay "Hello!"

        menu:
            "Compliment the artwork":
                you "Wow, these designs are amazing! You all are so talented."
                jay "Thank you! We put a lot of love into our work."

            "Express interest in getting your face painted":
                you "I've always wanted to try getting my face painted. Can I join in?"
                jay "Of course! We have plenty of designs to choose from."

            "Ask about the significance of the designs":
                you "These designs look so meaningful. Can you tell me about them?"
                jay "Absolutely! Each design here represents something special to the LGBTQ+ community."

        you "Hmm. What design to get..."

        menu:
            "Rainbow":
                you "I'm loving that rainbow design! Could I get that?"
                jay "Sure thing! Let's get started."

            "Alien":
                you "I think I want to go for something a bit more out of this world. How about an alien design?"
                jay "An alien design, huh? That sounds like fun! Let's get creative!"

            "Heart":
                you "I'm feeling the love today. Can you paint a heart on my cheek?"
                jay "Of course! Hearts are always a classic choice. Let's make it extra special!"

            "Pride Flag":
                you "I want to show my pride loud and proud! Can you paint the pride flag on my face?"
                jay "Absolutely! Let's celebrate pride together!"

        you "This turned out even better than I imagined!"
        jay "Yeah, you look great!"

        menu:
            "Take a photo":
                "This is too good not to capture! Let's take a photo together."
                jay "Absolutely! Strike a pose!"

            "Decline the photo":
                "I'm going to keep this moment just for me, but thanks for offering."
                jay "No problem! Enjoy the rest of the festival."

        "Feeling pumped and ready to show off my new face paint, I say goodbye to Jay and head back into the festival."

    jump pride_festival_options