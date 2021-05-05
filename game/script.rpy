# The script of the game goes in this file.

# define the main characters
define narrator = Character("Narrator", color="#ffffff")
define me = Character("Me", color="#c8c8ff")

image me angry = im.FactorScale("Portraits/DF_Angry.png", 0.5)
image me confused = im.FactorScale("Portraits/DF_Confused.png", 0.5)
image me coy = im.FactorScale("Portraits/DF_Coy.png", 0.5)
image me happy = im.FactorScale("Portraits/DF_Happy.png", 0.5)
image me laugh = im.FactorScale("Portraits/DF_Laugh.png", 0.5)
image me neutral = im.FactorScale("Portraits/DF_Neutral.png", 0.5)
image me pouty = im.FactorScale("Portraits/DF_Pouty.png", 0.5)
image me sad = im.FactorScale("Portraits/DF_Sad.png", 0.5)
image me shocked = im.FactorScale("Portraits/DF_Shock.png", 0.5)
image me shy = im.FactorScale("Portraits/DF_Shy.png", 0.5)

# for the jail case
define officer = Character("Swiss penal facility representative")

# for the deepfake case
define friend0 = Character("Ester")
define friend1 = Character("Alex")
define friend2 = Character("Lea")

# for the google translate case
define boss = Character("Your boss")

image office = im.FactorScale("Backgrounds/personal room day.png", 0.7)
image house = im.FactorScale("Backgrounds/house a day.png", 0.7)
image coffee = im.FactorScale("Backgrounds/cafe a day.png", 0.7)
image school = im.FactorScale("Backgrounds/school hallway a evening.png", 0.7)

image tweet = im.FactorScale("tweet.png", 0.4)

label start:
    # $ gui.textbox_yalign = 1.0
    # $ gui.rebuild()
    # $ gui.SetPreference("textbox_yalign", 1.0)
    # $ gui.rebuild()
menu:

    "Short introduction":
        jump introduction

    "Jailbird case":
        jump jail

    "Deepfake case":
        jump deepfake

    "Hungarian-English translator case":
        jump translator

    "A few last words":
        jump end

    #"Credits": do later in a fancy style
        #jump credits

    "Quit":
        return

        

# INTRODUCTION
        
label introduction:
    # $ gui.textbox_yalign = 0.5
    # $ gui.rebuild()
    # $ gui.SetPreference("textbox_yalign", 0.5)
    # $ gui.rebuild()
    image ml = "machine-learning-in-healthcare.jpg"
    show ml with fade
    # quick welcome
    narrator "Hello, you, machine learning student !" 
    narrator "This game is here to make you aware of the ethical dilemmas that can arise from machine learning uses."
    narrator "It is very important to be aware of them early in your machine learning journey and we thank you for choosing to play this game, you rock !"
    narrator "The game will consist in a short introduction to why it is important to learn about machine learning ethics and the consequences of not paying attention to them."
    narrator "Later, you will impersonate a machine learning scientist confronted with some ethical dilemmas and you will make a series of choices regarding each situation to explore their consequences."
    
    # introduction start
    # I put another image here to emphasize the change
    hide ml
    image prog = "prog_img.jpg"
    show prog with fade

    narrator "As you have learned during these first few weeks of lecture, machine learning is a very powerful tool to give predictions based on some data, or to explain the relationship between the input data and the response variable(s)."
    narrator "It is used in more and more areas of life and helps a lot of people !"

    # black box
    narrator "However, the algorithm stays a black box and it is hard to trust it for important decisions, since its outputs are given without any explanations. Indeed, a machine learning algorithm doesn’t explain its reasoning !"
    narrator "For instance, should you invest a million swiss francs in a particular firm blindfolded only because an algorithm told you so ?"
    narrator "In some cases, using the outputs goes even beyond the fear of losing a lot of money and can severely impact the lives of countless people, if not considered with caution."
    narrator "A very important thing to pay attention to is design flaws that could bias the model towards a certain part of the population. Indeed, if the model is trained on certain biased data, the results will also be biased."
    
    hide prog

    image chest x ray = im.FactorScale("Lung_X-ray.jpg", 0.3)

    show chest x ray with fade

    # medical imaging
    narrator "For example, regarding medical imaging like X-rays, the training set consists mostly of caucasian males."
    narrator "If the patient that requires medical imaging is black or female, can you still trust the results ? Can a female chest X-ray scan be interpreted using a model trained on male chest X-ray scans ? We have to be careful here."
    
    hide chest 

    image oximeter = im.FactorScale("oximeter.jpg", 0.5)
    show oximeter with fade

    # about covid 
    narrator "Another very current example is oximetry of covid patients in the hospitals. When patients arrive at the emergency room because they can’t breath due to a covid infection, their blood oxygen level is measured with a little device called an oximeter."
    narrator "If their oxygen level is below a certain threshold, they are admitted and treated, otherwise they are sent home."
    narrator "However, this little device works not as well on black people and tends to send them home even if they are in need of a treatment ! This discrimination can endanger their lives."
    narrator "These issues can be solved by carefully considering all the possible consequences during the design process and this is also true for machine learning algorithms."
    narrator "Indeed, those need to be carefully designed and the data carefully processed to avoid biases like the ones described previously."
    
    narrator "The next video shows such a design flaw that can occur if we don't think about the possible biases before designing something first."
    $ renpy.movie_cutscene("video/Racist_Soap_Dispenser.webm")

    hide oximeter

    image uighur case = im.FactorScale("Uighur case.png", 0.5)
    show uighur case with fade
    
    # Uighur case
    narrator "But Machine learning can even go further in ethical problems and can be used to violate human rights such as in the Uighurs case !"
    narrator "Indeed, the Chinese police are using machine learning to track the Uighurs ethnicity with an algorithm that can determine with 97 percent accuracy if a person is part of the Uighur community or not based on facial recognition."
    narrator "This is used to set off alerts to the police if many Uighurs are seen together for example and in general to track and persecute this community."
    narrator "Even if the facial recognition model was perhaps created with the best of intentions, it is enough to create a social disaster if it falls in the wrong hands."

    hide uighur case 

    show ml with fade

    narrator "Now, you should see better why machine learning should be used with caution and why thinking about ethics, and not only the scientific part, is crucial while designing models."
    narrator "Next, you will be put in the shoes of a machine learning scientist who encounters such problems and see how your reactions affect the consequences."
    narrator "Ready ? Let’s go, choose a case study !"

    hide ml

    jump start


# JAILBIRD CASE STUDY 

label jail:
    show house with fade
    narrator "You finally got your EPFL diploma and are now a computer scientist working freelance for companies. You are quite successful and get job offers all the time !"
    narrator "Actually, you are right now working on a super machine learning model for a big swiss company."
    narrator "You are at home alone and somebody knocks on the door."
    officer "Hey there, open up!"

    menu :
        "Intrigued, I open the door":
            $ tries = 0
            jump jail_door 
        "No, I am too scared to open":
            jump jail_scared

    
label jail_scared:

    narrator "The officer waits for 5 minutes outside your door. Do you open now ?"

    menu :
        "Well yes, why not, now I open the door":
            $ tries = 1
            jump jail_door 
        "No thank you. I will wait for him to go away":
            jump jail_nodoor

label jail_nodoor:

    narrator "He still doesn't go away so you finally decide to open up."
    $ tries = 2
    jump jail_door


label jail_door:
    image officer angry = im.FactorScale("Sprite Male Dark Hair/Sprite Male Dark Hair Ang01.png", 0.5)
    image officer annoyed = im.FactorScale("Sprite Male Dark Hair/Sprite Male Dark Hair Ann01.png", 0.5)
    image officer neural = im.FactorScale("Sprite Male Dark Hair/Sprite Male Dark Hair Neu01.png", 0.5)
    if tries == 0:
        show officer neural with fade 
    elif tries == 1:
        show officer annoyed with fade
    else :
        show officer angry with fade

    officer "Hello, I work for the Swiss justice system and we have heard that your computing skills are amazing."
    officer "Switzerland wants you to build a machine learning model to help judges decide if a prisoner can be let go earlier or not. Prisons are overfilled, you understand..."
    officer "Your task would be to predict if a prisoner will behave well or not after his or her early release. This way, we can let people go without them making harm out there."
    officer "Do you accept to take on this task ? You would be paid very well and the country will thank you !"

    menu :
        "Yes, of course, let's do this ! It seems interesting and for the good cause.":
            jump jail_yes
        "No thank you, I sense a trap.":
            jump jail_no

label jail_no:
    image officer evil = im.FactorScale("Sprite Male Dark Hair/Sprite Male Dark Hair Sly01.png", 0.5)
    show officer evil
    officer "Okay I understand. I will still send you an email with the dataset in case you change your mind. We really want you to do it."
    narrator "The officer leaves and you are still thinking about it a few hours later."
    narrator "In the end, you decide to give it a shot. After all, you can still decide later if you send them your model or not. It is still interesting to try, even in your free time."
    jump jail_email

label jail_yes: 
    image officer happy = im.FactorScale("Sprite Male Dark Hair/Sprite Male Dark Hair Smi01.png", 0.5)
    show officer happy
    officer "Great news ! You did the right choice, thank you !"
    officer "But be careful, we want a very accurate model ! Your country is counting on you. I'll send you the data later by mail. Bye then !"
    narrator "The officer leaves without giving you a chance to ask more questions."
    jump jail_email

label jail_email:
    hide officer
    hide house
    show office with fade
    show me confused
    narrator "You are still confused by this encounter and decide to make tea. You receive an email a few hours later."
    narrator "In the email, you get the dataset to train your model. It contains a lot of previous cases of prisoners and if they relapsed or not after being let go of jail."
    narrator "You have a lot of information about the prisoners, like the crime they committed, how long they were in jail for, and, of course, if they relapsed after being let go or not."
    narrator "However, you also have some other information including the prisoners' age, gender, ethnicity, country of birth, sexual orientation, religion, etc."
    narrator "Do you decide to include this information in the model or not ?"
    show me neutral

    # maybe refine the choices later (give more options)
    menu :
        "Yes, I want to include all this information":
            jump jail_include 
        "No, I don't want to include any of that":
            jump jail_not_included

label jail_include:
    narrator "You work for days and finally made your model. It reaches an amazing accuracy of 95\%. You decide to present it to the officer."
    hide me
    show officer happy at right 
    officer "Thank you for your model, it is amazing and very accurate. We will use it. Congratulations on behalf of your country."
    show me happy at left 
    narrator "The officer leaves and you are feeling proud of your work."
    hide me
    hide officer

    hide office
    show coffee with fade
    narrator "A few months later, you learn that an inmate friend you know might be released earlier." 
    show me shocked
    narrator "However, the judge decides to keep him in jail. You are suprised because you know that the inmate would behave well if released."
    narrator "You try to understand why he's not released earlier. You give your friend's data to your model and play a bit with the input."
    narrator "At one point, you change your friend's skin color and discover that your model would have set him free !"
    show me sad
    narrator "You feel guilty and have great remorse..."

    jump jail_concl

label jail_not_included:
    narrator "You work for days and finally made your model. It is impartial and unbiased since you didn't include all the biased information. Well done!"
    narrator "You decide to give it to the officer since you are quite proud of your work and are confident that it will not bias a certain part of the population."
    hide me
    show officer annoyed
    officer "Well, thank you for your model. However, your accuracy is only 77\%, that is not very good. We noticed that you omitted a lot of that data. We want you to include it."
    officer "If you don't include it, we know some other people that could do that for us."

    menu: 
        "Okay, I decide to include it now to better the accuracy":
            jump jail_include
        "No, I don't want to do that":
            jump jail_nope

label jail_nope:
    hide officer
    narrator "You stood on your principles and didn't include biased data in your model, well done ! "
    narrator "However, sadly, Switzerland didn't want your model because they thought it had too low accuracy..."
    narrator "You are a bit disappointed but decide to move on to other projects."
    narrator "Indeed, you know that feeding biased input to the model could create problems."
    narrator "For example, two inmates identical in every way apart from the skin color could have a different treatment based on this sole factor."
    jump jail_concl


label jail_concl:
    hide me
    hide coffee
    hide office

    # I included a picture of a jail to show it's the conclusion
    image jail_image = "jail.jpg"
    show jail_image with fade

    narrator "This case hopefully showed you the dilemmas of including biased data in a machine learning model."

    # feedback loops
    narrator "We can also note that there is a big problem with the fact that if we make a decision to feed biased data to our model now, the model will output biased results."
    narrator "And then, if these results are used as input in the same model later, it creates a feedback loop which can be very problematic to stop !"
    narrator "For example in this case, if the model outputs results such that black people have a lesser chance of being released early, this newly-created data can be used as input to the model later on."
    narrator "It then creates a snowball effect and black people will be even less released early as time goes on, due to the biased model itself."

    # minority report
    narrator "To go even further, we can see how such a model could degenerate looking at the minority report movie."

    # TO DO: include a short movie extract ?

    narrator "In this movie, three humans called precogs are able to predict a crime before it happens and the police go on to arrest the people before they even commit the crime."
    narrator "A great way to maintain peace or an unjust way of arresting people when they haven’t done anything yet ? "
    narrator "The answer is not easy and is yours to think about !"

    hide jail_image
    jump start 


# DEEPFAKE CASE STUDY 

label deepfake:

    image class_room = im.FactorScale("Backgrounds/classroom a day.png", 0.7)
    show class_room with fade

    narrator "You are a student of the Machine Learning class at EPFL."
    narrator "One day after the class, you meet with some of your friends who also take the class."

    image friend0 happy = im.FactorScale("Female Dark Hair/sprite female dark hair Smi01.png", 0.6)
    image friend1 happy = im.FactorScale("Jean/jean_happy.png", 0.6)
    image friend2 happy = im.FactorScale("Coral/coral_happy.png", 0.6)

    show friend0 happy
    friend0 "Hey ! Since we are all interested in machine learning why don't we make a small competition together ?"
    hide friend0
    show friend1 happy 
    friend1 "Yeah ! Great idea !"
    hide friend1
    show friend2 happy
    friend2 "We could compete with a game like chess or something like that ?"
    hide friend2
    show friend0 happy 
    friend0 "Or since the classes are prerecorded, we could train models to make deepfake videos of the teachers, it could be fun !"

    show friend1 happy at left 
    show friend2 happy at right
    "All together" "Oh yes ! Great idea !"
    hide friend0
    hide friend1
    hide friend2

    show me happy
    me "Sure but we have to agree that we will keep the resulting videos between us, ok ?"
    hide me 
    show friend0 happy at right
    show friend1 happy
    show friend2 happy at left
    "Everybody" "Yeah sure"

    hide friend1
    hide friend2
    show friend0 happy at center with move 
    friend0 "Cool, so it is settled. Let's meet in a few weeks to share our results."
    hide friend0

    hide class_room
    show office with fade

    show me neutral
    narrator "During the development, you wonder if you should make the generated videos indistinguishable from a true video."

    menu :
        "Yes, indistinguishable":
            show me happy
            narrator "You work very hard and the results are stunning ! Well done !"
            show me angry
            narrator "Unfortunately, even with all the energy you put in it, your program doesn't seem to want to generate perfect videos."
            narrator "With all the time you have invested in it, you have noticed that it always includes a ring on the right middle finger of everybody in the videos and you can't figure out why it does that."
            $ detail = "ring"
            hide me

        "No, add a small detail to recognize the generated videos":
            show me coy
            menu :
                narrator "You decide to automatically add a small detail. Which one do you want ?"
                "Add a ring on everybody's finger":
                    $ detail = "rings"

                "Add a hat on everybody's head":
                    $ detail = "hat"
                    
                "Add an earring to everybody":
                    $ detail = "earring"
            hide me
            
    hide office
    show class_room with fade

    narrator "A few weeks later..."

    show friend0 happy at right
    show friend1 happy at left 
    show friend2 happy

    narrator "You and your friends get together to watch the results."
    narrator "Most of your friends’ work is not really convincing but yours and one of your friends’ is both awesome !" 
    narrator "You decide to vote on who should win..."
    hide friend0
    hide friend1
    hide friend2

    show me laugh 
    narrator "It is very close but you win the bet !"

    # TO DO: maybe put a deep fake video ? here or at the end somewhere ?

    image friend0 angry = im.FactorScale("Female Dark Hair/sprite female dark hair Ang01.png", 0.6)
    hide me
    show friend0 angry
    narrator "Your final opponent is mad at you and out of an angry outburst she puts your work online !"
    hide friend0
    show me angry
    me "You delete the video right now !"
    hide me angry

    narrator "However it has been put online so it is already too late. Nothing else can be done."

    hide class_room
    show house with fade
    "A few weeks later at your home ..."

    image company = im.FactorScale("Sprite Male Dark Hair/Sprite Male Dark Hair Sly01.png", 0.5)

    show company
    "The company" "We are an advertisement company and we saw your deepfake video online and it is very impressive."
    "The company" "We can make you rich if you give us your code you used for it. Are you interested ?"

    hide company 
    show me neutral 
    menu :
        "Do you accept the offer ?"
        
        "Yes":
            show me laugh
            narrator "You are now rich !!"
            hide me 
            hide house

        "No":
            hide me
            hide house
            show coffee with fade
            show company at right
            image friend0 neutral = im.FactorScale("Female Dark Hair/sprite female dark hair Neu01.png", 0.6)
            show friend0 neutral at left
            narrator "The company then contacts your friends."

            "The company" "We saw your deepfake video online and it is very impressive. We were wondering if you could sell us the code for it ?"
            "The company" "You will be nicely paid !"
            show friend0 happy at left
            friend0 "Sure, here it is !"

            narrator "You friends are now rich and your code is gone without your consent."
            "Too bad ..."
            hide company
            hide friend0
            hide coffee

    show office with fade
    show me neutral

    narrator "A few months later, during the election times, you find the video of a politician online."
    show me confused
    narrator "You realise that something is off with that video." 
    
    "Politician" "We will make Switzerland great again by \"curing\" every homosexual person !"

    narrator "You decide to rewatch the video and realise that it includes the [detail] that your algorithm creates."
    
    show me shocked
    me "No doubt possible, the video has been created by my program !"

    hide me 
    hide office

    show ml
    narrator "This case is here to show how even a model made \"for fun\" may be misused if it falls into the wrong hands. Caution is always required."
    hide ml
    jump start


# TRANSLATION CASE STUDY

label translator: 
    show office with fade 
    show me happy
    narrator "You finally got your EPFL diploma and are now a computer scientist working for a big translation company."
    narrator "You are in your office, enjoying a little break."

    image boss sly = im.FactorScale("Sprite Male Dark Hair/Sprite Male Dark Hair Sly01.png", 0.5)
    show me happy at left with move
    show boss sly at right
    boss "Hey you, we were given a new task. Since I see that you are free at the moment and that you took Machine Learning in school, it will be for you !"
    boss "The task is to translate from Hungarian to English using a machine learning approach. No need to know Hungarian, don't worry !"
    boss "You just have to feed the Hungarian books already translated in English to a machine learning model to do it for you. I trust you, we only have one week to do so !"
    me "Hum, okay, I will do that boss ! I am on it."
    hide boss 
    show me happy at center with move
    narrator "You look up a bit the available translated literature on the web. What do you decide to use ?"

    menu :
        "I take all the available dataset to have as much data as possible !":
            jump translator_all
        "I will only take recent translations to be sure.":
            jump translator_recent

label translator_all:     
    narrator "You take all the dataset you can get access to and make your model with it. It translates with a very good accuracy. Your hungarian friend confirms it. "
    narrator "You decide to give your model proudly to your boss, even a few days early. "
    show me laugh at left with move
    show boss sly at right
    me "There you go boss, as promised, your Hungarian-English translator based on machine learning. Even a few days early, ha ! "
    boss "Thank you, it has a very good accuracy ! Keep up the good work. "
    narrator "You are happy and move on to other tasks."
    hide me
    hide boss

    show tweet
    narrator "However, a few months later, you are browsing Twitter and suddenly you see a tweet on your feed that seems to be talking about your work ! "
    hide tweet

    show me sad
    narrator "You are shoked and a bit disappointed in yourself. You definitely did not see that coming. "

    jump translator_end

    # too complicated to put in place with the loops...

    #narrator "If you got the chance to go back in time and only use recent datasets, would you do so ? "
    #menu :
        #"Yes !":
            #jump translator_recent
        #"No, I keep my choice for a better performance.":
            #jump translator_end


label translator_recent:
    show me neutral
    narrator "You take only the recent dataset you can get access to (last 10 years) and make your model with it."
    narrator "However, you notice that the accuracy is not very good."
    narrator "Indeed, the dataset of recent translated Hungarian books to English is clearly not large enough for your needs. "
    narrator "Days pass and your model performance is not optimal. What do you do ?"

    menu :
        "I want to take all available dataset.":
            jump translator_all
        "I keep this and present it to my boss.":
            jump translator_present

label translator_present:
    show me neutral at left with move 
    image boss annoyed = im.FactorScale("Sprite Male Dark Hair/Sprite Male Dark Hair Ann01.png", 0.5)
    show boss annoyed at right 
    me "There you go boss, your Hungarian-English translator based on machine learning. "
    boss "Thank you for your work, but the accuracy is not very good. I think our competitors will destroy us." 
    show boss sly at right
    boss "Well still, let's present the model to our customer. Your job is now done !"
    narrator "You get no news from this project and move on to other tasks."
    hide boss 
    hide me 

    show tweet 
    narrator "A few months later, you are browsing Twitter and suddenly you see a tweet on your feed. "
    hide tweet

    show me happy
    narrator "Another competitor company must have chosen to take all the available dataset and is now paying the price on social media !"
    narrator "It looks like you did a good thing taking only the recent translations ! Even if the price to pay is thus a less good accuracy..."

    jump translator_end


label translator_end:
    hide me
    hide office

    # I included a different picture to show it's the conclusions. Nice ! 
    image translation_image = "translation.jpg"
    show translation_image with fade

    narrator "This case hopefully showed you how you should always be careful while selecting a dataset."
    narrator "Here, there is a trade-off between a good accuracy in translation (taking all the dataset) or unbiased data (only taking recent datasets)."
    narrator "Indeed, the Hungarian language doesn't have gendered pronouns in front of verbs and that is definitely something to consider in this task before jumping into it."
    narrator "Not knowing the Hungarian language, it is very hard to think about this fact beforehand, leading to a design flaw."
    narrator "Always try to think of potential biases that you could have in your model before starting a task !"

    hide translation_image
    jump start  


# CONCLUSIONS

label end:

    image ml = "machine-learning-in-healthcare.jpg"
    show ml with fade

    # thank you for playing
    narrator "You made it to the end of the game ! Well done !"
    narrator "You are hopefully now more aware of how machine learning use can give rise to ethical issues."
    narrator "It is very important to keep these issues in mind while working with machine learning and not only focus on the technical side."
    narrator "Thank you again for taking the time to learn about these very important issues, you rock !"

    jump resources

label resources:
menu:

    narrator "If you want to learn more about it and satisfy your thirst of knowledge, you can look at the following resources:"

    "1. A moral experiment about automated cars developed by MIT !":
        # $ webbrowser.open_new(self.url)
        $ OpenURL("https://www.moralmachine.net/")()
        jump resources
    "2. The paperclip game about how an AI can get out of control when instructed with a simple goal !":
        $ OpenURL("https://www.decisionproblem.com/paperclips/index2.html")()
        jump resources
    "3. A short quite funny video also about an AI getting out of control by Tom Scott !":
        $ OpenURL("https://youtu.be/-JlxuQ7tPgQ")()
        jump resources
    "I am okay thank you, bye !":
        hide ml
        jump start

