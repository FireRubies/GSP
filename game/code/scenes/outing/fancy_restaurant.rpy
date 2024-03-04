label fancy_restaurant:
    scene fancy restaurant

    if visited_recording_studio:

        "The soft clinking of silverware and hushed conversations create a pleasant ambiance as you savor your meal. Suddenly, you spot Liam and Jordan across the room, smiles lighting up their faces." 

        show liam neutral at right
        show jordan smile at left
        "They wave you over, and a warmth spreads through you. It looks like that conversation at the recording studio left a good impression."

        menu:
            "Join them for dinner":
                "You make your way over, a mix of nerves and excitement in your stomach."
                
                jordan "Hey, so glad you decided to join us!"

                show liam smile
                liam "Yeah, felt like fate seeing you here. Care to pull up a chair?" 
                you "Wouldn't miss it for the world."

                show liam neutral
                show jordan neutral
                jordan "So, we were just talking about... have you seen that new documentary? 'Beyond the Binary' or something?"
                you "I haven't, actually. Is it any good?"

                show liam smile
                liam "It's really swaggy. Explores how gender isn't always as clear-cut as people like to think."
                jordan "Yeah, made me question a lot of things I took for granted."

                jordan "So, what should we feast on? I'm in the mood for something adventurous."
                liam "I've heard their mushroom risotto is amazing. Unless you're feeling more of a classic steak vibe?"
                you "Honestly, it all sounds delicious. Surprise me!"

                liam "Ooh, that smells amazing! Did everyone order something different?"
                jordan "I couldn't resist the mushroom risotto. And they have those decadent truffle fries..."
                you "Well, I hope you're willing to share a bite. My steak looks awesome, but variety is the spice of life!"

                jordan "Anyway, back to that documentary - 'Beyond the Binary'? It really got me thinking."
                you "How so?"
                liam "Well, it showed how people all over the world express their gender in such unique ways. Not just the typical 'he' or 'she' thing."
                jordan "Exactly! And it made me realize how limiting those boxes can be."

                you "You know, it got me thinking about pronouns... I've met some folks who use 'they/them', and the documentary explained why that's important."
                liam "Definitely! It's all about respecting how a person identifies. Some people don't fit neatly into 'he' or 'she', and that's totally valid."
                jordan "Right, and using the pronouns someone chooses shows that you see them for who they really are."

                menu fancy_restaurant_dinner_convo_options:
                    "Can you explain more about that?":
                        liam "Well, think of it like this: if someone's name is Charlotte, but you keep calling them 'Josie'... it feels wrong, right?"
                        jordan "Exactly! Pronouns are kind of like a part of someone's name. It's how they want to be addressed."
                        you "That makes a lot of sense."

                    "Have any of your friends experienced that... the wrong pronouns thing?":
                        jordan "Actually, yeah. Remember Sarah from our summer camp a few years back?"
                        you "Oh yeah, Sarah! What about her?"
                        liam "Well, back then she went by 'she/her', but recently she came out as non-binary and uses 'they/them' now."
                        jordan "At first, some people messed up and used her old pronouns by accident. She told me it felt like... being erased."
                        show jordan frown
                        show liam frown

                        menu: 
                            "That's really tough to hear.":
                                jordan "Yeah, it was. But it also made me realize how important it is to get pronouns right. It's about respecting who someone is."

                            "Did people start getting it right eventually?":
                                
                                show jordan smile
                                show liam smile
                                liam "It took time and a few reminders, but yeah. Now it feels natural. Sarah seems much happier too."

                            "Is there a way to know someone's pronouns without asking directly?":
                                jordan "Sometimes people put them in social media bios, or wear pins with their pronouns. But it's always best to just ask respectfully."

                    "I'm still learning, but I want to get it right.":
                        jordan "That's awesome! One cool thing is to ask people what their pronouns are, or let them know yours when you introduce yourself."
                        liam "It just makes everyone feel more comfortable and included."

                show jordan smile
                show liam smile
                jordan "The film also showed how some cultures have traditionally recognized more than two genders. Makes you wonder how much of our thinking is just... what we're used to."
                liam "Right? Like, why do we automatically sort everything into pink and blue, girls and boys... it feels so limiting sometimes."

                menu:
                    "It's like everyone has to fit into these boxes.":
                        jordan "Exactly! And if you don't fit neatly, people get uncomfortable. It shouldn't be that way."
                        jordan "It makes me think how those boxes affect everything - how we dress, what jobs are 'okay', even how we're supposed to act. "

                    "I've never really thought about that before.":
                        liam "A lot of people don't. That's kind of the problem, right? We accept things without questioning why."
                        jordan "Maybe someday, those boxes won't matter so much. People can just... be themselves."

                    "Do you think things are changing?":
                        jordan "Slowly. I see more people speaking up, being who they are, even if it doesn't match the old rules." 
                        liam "It gives me hope. Even just talking about this stuff feels like a small step in the right direction."

                show jordan neutral
                show liam neutral
                "Honestly, watching it made me question my own assumptions a bit. How we label ourselves, how we present ourselves..."
                jordan "It definitely forces some self-reflection, doesn't it?"

                menu:
                    "I'm still figuring out who I am.": 
                        liam "That's totally normal, especially at our age. It's a journey, not a destination, right?"
                        jordan "And it's okay to take your time. Explore different things, see what feels right." 

                    "What if what feels right goes against what people expect?":
                        show jordan frown
                        show liam neutral

                        jordan "That's a tough one. But shouldn't being true to yourself matter more than what others think?"
                        liam "Easier said than done sometimes. But I think finding people who support you, no matter what, makes a huge difference."

                    "Does the documentary talk about that... about finding your people?":
                        liam "Kind of. It shows how people who felt different formed communities and supported each other."
                        jordan "Maybe there are groups like that online, or even in our town. Places where you can connect with people who get it." 

                "The waiter comes by to clear the plates."

                liam "Well, that gives me a lot to think about."
                show jordan smile
                jordan "Me too. I guess the best thing is to keep talking, keep learning, right?"
                show liam smile
                you "Definitely. Thanks for the awesome conversation, guys."
                jordan "Anytime."

            "Politely decline":
                "You offer a friendly smile and a wave, but decide to continue your meal alone."
                you "Thanks for the offer, but I think I'll enjoy my solo dinner tonight. Maybe another time!"

    else:
        "The soft clinking of silverware and hushed conversations create a pleasant ambiance as you savor your meal."

        you "Maybe I can have dinner with some friends here later. That'd be nice."

        "With a full stomach you head out of the restaurant."

    jump house_porch_options 