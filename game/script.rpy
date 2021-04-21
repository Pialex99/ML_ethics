# The script of the game goes in this file.

# define the main characters
define narrator = Character("Narrator", color="#ffffff")
define me = Character("Me", color="#c8c8ff")

# for the jail case
define officer = Character("Swiss justice system officer")

# for the deepfake case
define friend0 = Character("ML enthousiastic friend")
define friend1 = Character("Another ML enthousiastic friend")
define friend2 = Character("Still another ML enthousiastic friend")
define friend3 = Character("Fourth ML enthousiastic friend")


label start:

menu:

    "Introduction":
        jump introduction

    "Jail":
        jump jail

    "Deepfake":
        jump deepfake

    "Quit":
        return
        
        
label introduction:

    # quick welcome
    narrator "Hello you, machine learning student !" 
    narrator "This game is here to make you aware of the ethical dilemmas that can arise from machine learning uses. It is very important to be aware of them early in your machine learning journey and we thank you for choosing to play this game, you rock !"
    narrator "The game will consist in a short introduction to why it is important to learn about machine learning ethics and the consequences of not paying attention to it."
    narrator "Later, you will impersonate a machine learning scientist confronted with some ethical dilemmas and you will make a series of choices regarding each situation to explore their consequences. Let’s start !"
    # introduction start
    narrator "As you have learned during these first few weeks of lecture, machine learning is a very powerful tool to give predictions from some data given to the algorithm, or to explain the relationship between the input data and the response variable(s). It is used in more and more areas of life and helps a lot of people !"
    narrator "However, the algorithm stays a black box and it is hard to trust it for important decisions, since its outputs are given without any explanations. Indeed, an ML algorithm doesn’t explain its reasoning !"
    narrator "For instance, should you invest a million swiss francs in a particular firm blindfolded only because an algorithm told you so ?"
    narrator "In some cases, using the outputs goes even beyond the fear of losing a lot of money and can severely impact the lives of countless people, if not considered with caution."
    narrator "A very important thing to pay attention to is design flaws that could bias the model towards a certain part of the population. Indeed, if the model is trained on certain biased data, the results will also be biased."
    narrator "For example, regarding medical imaging like X-rays, the training set consists mostly of caucasian males."
    narrator "But if the patient that requires medical imaging is black or female, can you still trust the results ? Can a female chest X-ray scan be interpreted using a model trained on male chest X-ray scans ? We have to be careful here."
    
    # put a video here
    
    narrator "Another very current example is oximetry of covid patients in the hospitals. When patients arrive at the emergency room because they can’t breath due to a covid infection, their blood oxygen level is measured with a little device called an oximeter."
    narrator "If their oxygen level is below a certain threshold, they are admitted and treated, otherwise they are sent home. However, this little device works less well in black people and tends to send them home even if they are in the need of a treatment ! This discrimination can endanger their lives."
    narrator "These issues can be solved by carefully considering all the possible consequences during the design process and this is also true for machine learning algorithms. They need to be carefully designed and the data carefully processed to avoid biases like the ones described previously."
    narrator "However, it can even go further in ethical problems and create usages against human rights such as in the Uighurs case."
    narrator "Indeed, the Chinese police are using machine learning to track the Uighurs ethnicity with an algorithm that can determine with 97 percent accuracy if a person is part of the Uighur community or not based on facial recognition."
    narrator "This is used to set off alerts to the police if many Uighurs are seen together for example and in general to track and persecute this community. Even if the facial recognition model was perhaps created with the best of intentions, it is enough to create a democracy disaster if it falls in the wrong hands."
    narrator "Now, you should see better why machine learning should be used with caution and why thinking about ethics, and not only the scientific part, is crucial while designing models."
    narrator "Next, you will be put in the shoes of a machine learning scientist who encounters such problems and see how your reactions affect the consequences."
    narrator "Ready ? Let’s go, choose a case study !"


    jump start

label jail:

    # context and first encounter
    narrator "You finally got your EPFL diploma and are now a computer scientist working freelance for companies. You are quite successful and get job offers all the time!"
    narrator "Actually, you are right now working on a super machine learning model for a big swiss company."
    narrator "You are at home alone and somebody knocks on the door."
    officer "Hey there, open up!"
    # me: choose to open the door or not (I'll do the choices later)
    officer "I work for the Swiss justice system and we have heard that your computing skills are amazing."
    officer "Switzerland wants you to build a machine learning model to help judges decide if a prisoner can be let go earlier or not. Prisons are overfilled, you understand..."
    officer "Your task would be to predict if a prisoner will behave well or not after his or her release. So we can let people go without them making harm out there hehe."
    officer "Do you accept to take on this task ? You would be paid very well and the country will thank you !"
    # me: choose to accept or not
    # if accept:
    officer "Great news ! You did the right choice, thank you !"
    officer "But be careful, we want a very accurate model ! Your country is counting on you. I'll send you the data later by mail. Bye then !"
    narrator "The officer leaves without giving you a chance to ask more questions."
    narrator "You are still confused by this encounter and decide to make tea. You receive any email a few minutes later."
    narrator "In the email, you get the dataset to train your model. It contains a lot of previous cases of prisoners and if they relapsed or not after being let go of jail."
    narrator "You have a lot of information about the prisoners, including the color of their skin, their age, gender, ethnicity, country of birth, sexual orientation, religion, etc."
    narrator "Do you decide to include this information in the model or not ?"
    # to see together if we can choose all or nothing, or by a case to case basis, to complete



    jump start 


label deepfake:

    show friends happy

    friend0 "Hey ! Since we are all interested in ML why don't we make a small competition together ?"

    friend1 "Yeah ! Great idea !!"
    friend2 "We could compete with a game like chess or something like that ?"
    friend3 "Or since the classes are prerecorded, we could train models to make deepfakes of the teachers"

    "All together" "Oh yes ! Great idea !!"

    me "Sure but we have to agree that we will keep the resulting videos between us, ok ?"

    "EveryBody" "Yeah sure"

    friend0 "Cool, so it is settled. Lets meet in a few weeks to share our results."

    narrator "During the development, you wonder if you should make the generated videos undisguisable from a true video"

    menu :
        "Yes, undisguisable":
            narrator "You work very hard and the results are stunning ! Well done !"
            narrator "Unfortunalty, even with all the energy you put in it, your program doesn't seems to want to generate perfect videos."
            narrator "With all the time you have invested in it, you have noticed that it allways include a ring on the right middle finger of everybody in the videos and you can't figure out why it does that."
            $ detail = "ring"

        "No, add a small detail to recognize the generated videos":

            menu :
                narrator "You decide to automaticaly add a small detail. Which one do you want ?"
            
                "Add a ring on every fingers":
                    $ detail = "rings"

                "Add a hat on everybody's head":
                    $ detail = "hat"
                    
                "Add a earring to everybody":
                    $ detail = "earring"
            

    narrator "A few weeks laters..."

    narrator "You and your friends regroup to watch the results. Most of your friends’ work are not really convincing but yours and one of your friends’ are both awesome and so you decide to vote on who should win..."
    narrator "It is very close but you win the bet !!"

    show mad friend
    narrator "Your final opponent is mad at you and out of an angry outburst he/she puts your work online !!!"
    
    show angry you
    me "You delete the video right now !!"
    hide angry you

    narrator "However it has been online so it is already too late and so nothing else can be done."

    "Soon after..."

    show enterprise
    "Enterprise" "We are an advertisement company and we saw your deepfake video online and it is very impressive."
    "Enterprise" "We can make you rich if you give us your code you used for it. Are you interrested ?"

    menu :
        "Do you accept the offer ?"
        
        "Yes":
            show you rich 
            narrator "You are now rich !!"

        "No":
            narrator "The enterprise then contacts your friends."
            "Enterprise" "We saw your deepfake video online and it is very impressive. We were wondering if you could sell us the code for it ?"
            "Enterprise" "You will be nicely paid !!"
            "Your friends" "Sure, here it is !"

            narrator "You friends are now rich and your code is gone without your censent."
            "Too bad ..."

    show you dubious
    narrator "At the next election, you realise that something is off with one of the videos about the election." 
    
    show politician
    "Politian" "We will make Switzerland great again by \"curing\" every homosexual person !!"

    show you watching video
    narrator "You decide to rewatch the video and realise that it includes the [detail] that your algorithm creates."
    
    show you shocked
    me "No doubts, the video has been created by my program !!!"
    
    jump start

