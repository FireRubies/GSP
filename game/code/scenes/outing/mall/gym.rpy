label gym:
    scene gym

    "The rhythmic clang of weights and the hum of treadmills fill the air."

    show alex neutral at left 
    "A muscular figure in a wheelchair sits in front of the squat rack, a heavily loaded barbell across their shoulders."

    "They take a deep breath... and up!" 

    show alex frown
    "Their arms tremble, determination in their eyes.  This weight won't defeat them."

    "You approach cautiously, unsure how to address them."

    menu:
        "Just offer to join in":
            you "Hey, that looked intense! Mind if I work out with you?"
            alex "Sure!  Always up for a workout buddy."

            # Workout together, potential for neutral conversation that hints towards the player learning more...
            you "So, what's your usual routine? I'm into trying arms and shoulders today."
            alex "Nice! I'm actually focusing on chest and triceps.  Want to try alternating sets on the bench?"

            menu:
                "Sounds good":
                    show alex neutral
                    alex "Cool!  Let's warm up, and then we can see where your starting weight is."

                    # ... A few minutes of warm-ups  ...
                    alex "Alright, feeling loose? Let's load up the bar and try a few reps to gauge your strength."
                    
                    "You do some reps."

                    you "That felt... heavier than I expected."
                    alex "No worries, happens to everyone!  Maybe drop the weight a bit, or I can spot you?"

                    menu gym_workout:
                        "I want to try it myself":
                            alex "You got this!  Want to drop down a few pounds, or stick with it and give it another go?"

                            menu:
                                "Lower the weight a bit":
                                    alex "Smart move! Better to build up gradually than risk injury."
                                    # ... Adjust the weight, player does another set ...

                                "I'll try again with this weight":
                                    show alex smile 
                                    alex "I like your determination!   Remember, focus on your form!"  
                                    # ... Player does another set ... 

                            # ... After the set ...
                            you "Okay, that felt better!"
                            alex "Nice work! See, a little adjustment can make a big difference."

                            you "Yeah I guess so! Thanks!"

                        "A spotter would be great, actually":
                            alex "Sure thing!  Let's get you set up."
                            show alex smile
                            alex "Good form!  Now breathe deep... and push!"

                            # ... Player does the set with Alex's help ... 
                            alex "And there you go!  See? You had it in you all along."
                            you "Thanks, that definitely felt easier with you there."

                            menu:
                                "Could I try it solo?":
                                    alex "Absolutely!  I'm always here if you need me again though."

                                    "You try it solo."

                                    menu:
                                        "That was way better!":
                                            alex "See? Told you could do it!  Let's add a bit more weight for your next set."

                                        "Hmm, still a bit tough...":
                                            alex "No worries, we can keep this weight for a few sets. Getting the form right is key." 

                                        "Actually, I think I'm done with bench press for today":
                                            show alex smile
                                            alex "Totally fine!  Wanna try some incline dumbbell press?  Or something totally different?"

                                        "How can I improve for doing it myself?":
                                            alex "Good question!  Let's focus on your breathing and keeping those shoulders tight..." 

                                    "You spend more time working out. Eventually you get exhausted and decide to leave." 

                "Maybe another time, I don't want to interrupt your flow":
                    alex "No worries! How about we grab some dumbbells and work on our arms together then?"

                    show alex smile
                    alex "Let's head over to that rack.  What are you thinking - bicep curls, shoulder presses...?"
                    you "Actually, I'd love some ideas.  I'm still figuring all this stuff out."
                    alex "Happy to help! Let's go through a few basic movements, and then we can build a little arm workout for you."

                    "A short while later..."

                    alex "That was really good! It was nice working out with you!"

                    you "Same!"

                "I'm actually pretty new to all this... mind giving me some tips?":
                    show alex smile
                    alex "Absolutely! Always happy to help. What are you interested in working on?"

                    "I don't think I can legally offer excercise advice. Sorry!"

                    jump gym_workout


        "Try to subtly guess their gender": 
            you "Excuse me... sir?  Or ma'am?  I love your energy, would you mind if I join you?"
            show alex frown
            alex "Doesn't matter much, but 'he' works. And yeah, go for it. What's on your workout plan?"

            menu:
                "I... just wasn't sure. You're pretty strong...":
                    alex "Thanks.  Gets me a lot of weird looks in the changing room sometimes, but whatever. Can't change who I am, you know?"

                "Society has some messed-up ideas about bodies...":
                    alex "Right?  Like, who gets to decide these rules anyway? Just makes me wanna push harder."

                    you "Yeah I get that. You here to workout?"

                    alex "Yeah of course! You?"

                    you "I'm into trying arms and shoulders today."
                    alex "Nice! I'm actually focusing on chest and triceps.  Want to try alternating sets on the bench?"
                    show alex neutral
                    alex "Cool!  Let's warm up, and then we can see where your starting weight is."

                    alex "Alright, feeling loose? Let's load up the bar and try a few reps to gauge your strength."

                    you "That felt... heavier than I expected."
                    alex "No worries, happens to everyone!  Maybe drop the weight a bit, or I can spot you?"

                    jump gym_workout

                "Sorry if that was awkward. Let's just focus on the workout":
                    alex "No worries. It happens. So, what do you want to hit today?"
                    you "I'm into trying arms and shoulders today."
                    alex "Nice! I'm actually focusing on chest and triceps.  Want to try alternating sets on the bench?"
                    show alex neutral
                    alex "Cool!  Let's warm up, and then we can see where your starting weight is."

                    alex "Alright, feeling loose? Let's load up the bar and try a few reps to gauge your strength."

                    you "That felt... heavier than I expected."
                    alex "No worries, happens to everyone!  Maybe drop the weight a bit, or I can spot you?"

                    jump gym_workout

        "Wait and listen for clues":

            "A voice calls out: 'Hey mam, need a spotter for that next set?'"
            show alex frown
            alex "Ah, thanks! And sure, come on over. It would be sir by the way. But please don't call me sir."
            show alex neutral
            "The voice goes silent."
            show alex smile
            alex "Ah don't worry about it. It happens all the time."
            alex "Nice to meet another gym enthusiast!"

            menu:
                "Go over and say hi":
                    menu:
                        "Hi! Nice to meet you! I'm [player_name]":
                            alex "Nice to meet you too.  So, ready to join this workout party?"
                            you "Yeah!"
                            you "I was thinking trying arms and shoulders."
                            alex "Nice! I'm actually focusing on chest and triceps.  Want to try alternating sets on the bench?"
                            show alex neutral
                            alex "Cool!  Let's warm up, and then we can see where your starting weight is."

                            alex "Alright, feeling loose? Let's load up the bar and try a few reps to gauge your strength."

                            you "That felt... heavier than I expected."
                            alex "No worries, happens to everyone!  Maybe drop the weight a bit, or I can spot you?"

                            jump gym_workout

                        "Cool to meet another gym enthusiast!": 

                            show alex smile
                            alex "That's what I said! Hehe. So what are you planning to work on today?"
                            you "I was thinking trying arms and shoulders."
                            alex "Nice! I'm actually focusing on chest and triceps.  Want to try alternating sets on the bench?"
                            show alex neutral
                            alex "Cool!  Let's warm up, and then we can see where your starting weight is."

                            alex "Alright, feeling loose? Let's load up the bar and try a few reps to gauge your strength."

                            you "That felt... heavier than I expected."
                            alex "No worries, happens to everyone!  Maybe drop the weight a bit, or I can spot you?"

                            jump gym_workout

                "Just leave":
                    pass

    jump mall_location_options