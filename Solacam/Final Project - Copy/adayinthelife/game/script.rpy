# script of our game in this file.
# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"
image a happy = "happy1.png"
image a icecream = "cream1.png"
image a exc = "exc1.png"
image a angry = "angry1.png"
image a surp = "surp.png"
image a sad = "sadalex.png"
image a neu = "neu1.png"
image j angrycry = "angrycry.png"
image j cry = "cry.png"
image j exc = "excited.png"
image j happy = "jhappy.png"
image j neu = "neutral.png"
image j angry = "jang.png"
image j happycry = "happycry.png"
image j sad = "sad.png"
image j icecream = "jaqice.png"
image j surprised = "surprised.png"
image t happy = "terrahappy.png"
image t neutral = "terraneutral.png"
image t sad = "terrasad.png"
image b angry = "bullyang.png"
image b anghap = "bullyanghap.png"
image r happy = "erikhappy.png"
image r sad = "eriksad.png"
image r neutral = "erikneutral.png"
image m happy = "happyteach2.png"
image m neutral = "teachneutral.png"
image m angry = "teachangry.png"
image park bg = "park.jpg"
image classroom bg = "classroom.jpg"
image icecream bg = "icecream.jpg"
image movietheater bg = "movietheater.jpg"
image credits bg = "backgrounds.jpg"
# Declare characters used
define e = Character('Narrator', color="7D3C98")
define a = Character ('Alex', color = "4fd1d4")
define j =  Character ('Jaq', color = "ffc9c8")
define t = Character ('Tara', color = "ffff00")
define r = Character ('Erik', color = "1E8449")
define b = Character ('Bully', color = "E74C3C")
define m = Character ('Teacher', color = "D35400")
# The game starts here.
label start:
    play music "mainmus.mp3"
    scene park bg
    $ good_ending = 0
    $ bad_ending = 0
    e "The following game is based on user input but because this is only a demo only one character is currently available."
    e "However this character will still have multiple endings based on user input about conflicts dealing with mentalism,
       however the full game will be based on all forms of ableism."
    e "Ableism, is discrimination of against people with any type of disability."
    e "Mentalism, a specific form of ableism, is the discrimination against people with mental illnesses or disabilities." 
    e "Due to the fact that our game deals with heavy topics, we've decided to include trigger warnings due to mention of depression and
       imposter syndrome. As well as potential mentions of bullying."
    e "You will be playing as Alex." 
    show a neu at left
    a "Hi, I'm Alex, your average university student."
    e "The story will be following Alex and another student Jaq."
    hide a neu 
    show jhappy at left 
    e "This is Jaq another university student."
    j "But I'm not nearly as smart as anyone else here."
    hide jhappy
    e "Ah your first choice, do you want to tell Jaq that they're just as smart as everyone else or ignore their remark?"
    menu:
      "Jaq don't be ridiculous, you're very smart!":
        jump choice_yes 
        $ good_ending +=1
      "Whatever you say Jaq.":
        jump choice_no
        $ bad_ending += 1
label choice_no:
    show j sad at right
    j "Yeah you're right, I am kind of useless."
    show a neu at left
    a "Don't mention it."
    a "Are your classes okay?"
    j "Everyone else gets it. It's just me who doesn't understand."
    j "I don't even get the homework assignment. Can you help me?"
    hide a neu
    hide j sad
    menu:
        "Sure!":
           jump choice_datealready
           $ good_ending +=1
        "I can't.":
           jump choice_alexwhy
           $ bad_ending +=1
label choice_yes:
    show j sad at right
    j "Thanks Alex,but really I'm kind of useless."
    show a happy at left
    a "Don't mention it and you're not useless."
    a "Anyways,how are classes going for you?"
    j "Everyone else gets it. It's just me who doesn't understand."
    j "I don't even get the homework assignment. Can you help me?"
    hide a happy
    hide j sad
    menu:
        "Sure!":
           jump choice_datealready
           $ good_ending +=1
        "I can't.":
           jump choice_alexwhy
           $ bad_ending +=1
label choice_alexwhy:
    show j sad at right
    j "Oh okay then. I just thought..."
    j "Nevermind."
    show a neu at left
    a "Whatever."
    j "See you understand it. I'm so stupid, I shouldn't be in the program."
    hide a neu
    hide j sad
    e "They think they shouldn't be in the program? How will you react?"
    menu:
        "Jaq, I suck at it too. It's okay.":
            jump choice_continue
            $ good_ending += 1
        "Jaq,stop. You're just being dramatic.":
            jump choice_switch
            $ bad_ending += 1
label choice_datealready:
    show a happy at left
    a "Of course I'll help you!"
    show j sad at right
    j "I'm sorry to waste your time."
    j "It's because I'm stupid. I shouldn't be in the program."
    hide a happy
    hide j sad
    e "They think they shouldn't be in the program? How will you cheer them up?"
    menu:
        "Jaq, I suck at it too. It's okay.":
            jump choice_continue
            $ good_ending += 1
        "Jaq,stop. You're just being dramatic.":
            jump choice_switch
            $ bad_ending += 1
label choice_switch:
    show a angry at left
    a "You're just such a drama queen would you chill!?"
    show j sad at right
    j "I'm sorry!"
    hide a angry
    show a neu at left
    a "Whatever, let's just head to class,"
    j "Actually I think I'm going to skip to go rest instead."
    a "Skip?! But nothing could ever make you want to miss class usually."
    hide j sad
    hide a happy
    e "How are you going to make Jaq attend with you?"
    menu:
        "Come on, class is important. Plus we have a free period after.":
            jump choice_goodintentions
            $ good_ending += 1
        "I don't care, if you  miss class that's on you.":
            jump choice_dontcare
            $ bad_ending += 1
label choice_continue:
    show a happy at left
    a "Everyone finds it difficult. Anyone who says otherwise is a liar."
    show j happy at right
    j "But it always seems so easy for you."
    a "It's really not as easy as I make it seem."
    j "I'm sure you're just being nice."
    a "Come on, let's go to class!"
    hide j happy
    show j sad at right
    j "Actually I think I'm going to skip to go rest instead."
    a "Skip?! But nothing could ever make you want to miss class usually."
    hide j sad
    hide a happy
    e "How are you going to make Jaq attend with you?"
    menu:
        "Come on, class is important. Plus we have a free period after.":
            jump choice_goodintentions
            $ good_ending += 1
        "I don't care, if you  miss class that's on you.":
            jump choice_dontcare
            $ bad_ending += 1
label choice_dontcare:
    hide park bg
    scene classroom bg
    show r neutral at right
    r "Jaq didn't come to class today."
    r "That's so weird."
    show a neu at left
    a "Yeah, weird."
    a "I think I'll go check on them after."
    hide r neutral
    hide a neu
    hide classroom bg
    scene park bg
    show a neu at left
    a "You should've come to class."
    show j sad at right
    j "No I shouldn't have."
    a "Whatever, just stop that."
    hide a neu
    hide j sad
    e "It seems you've offended Jaq! What are you going to do?"
    menu:
        "Oh no, I care about you too!":
            jump choice_aw
            $ good_ending += 1
        "Stop it, you're being ridiculous.":
            jump choice_rude
            $ bad_ending += 1
label choice_goodintentions:
    hide park bg
    scene classroom bg
    show a exc at left
    a "We can rest after class. We can even get food!"
    show j happycry at right
    j "Is all you care about food?"
    a 'Yeah but not as much as you obviously.'
    hide j happycry
    show j sad at right
    j "Oh."
    hide j sad
    hide a exc
    e "It seems you've offended Jaq! What are you going to do?"
    menu:
        "Oh no, I care about you too!":
            jump choice_aw
            $ good_ending += 1
        "Stop it, you're being ridiculous.":
            jump choice_rude
            $ bad_ending += 1
label choice_rude:
    hide classroom bg
    scene park bg
    e "A bit later... After Class."
    show a neu at left
    a "So you want to go to the movies later?"
    show t neutral at right
    t "Sure."
    a "Cool Erik's going too."
    hide t neutral
    show j sad at right
    j "Leave me alone. Please."
    hide a neu
    show b anghap at left
    b "Shut up you twat."
    b "You can't do anything right, you're worthless."
    hide j sad
    show j cry at right
    e "Jaq is being bullied, are you going to step in or not?"
    hide j cry
    hide b anghap
    menu:
        "Hey! Stop that, leave them alone.":
            $ good_ending += 1
            jump choice_poorjaq
        "It's probably best to leave it.":
            $ bad_ending += 1
            jump choice_what
label choice_aw:
    hide classroom bg
    scene park bg
    e "A bit later... After Class."
    show a neu at left
    a "So you want to go to the movies later?"
    show t neutral at right
    t "Sure."
    a "Cool Erik's going too."
    hide t neutral
    show j sad at right
    j "Leave me alone. Please."
    hide a neu
    show b anghap at left
    b "Shut up you twat."
    b "You can't do anything right, you're worthless."
    hide j sad
    show j cry at right
    e "Jaq is being bullied, are you going to step in or not?"
    hide j cry
    hide b anghap
    menu:
        "Hey! Stop that, leave him alone.":
            $ good_ending += 1
            jump choice_poorjaq
        "It's probably best to leave it.":
            $ bad_ending += 1
            jump choice_what
label choice_what:
    show a neu at left
    a "It's not our place to step in."
    show t neutral at right
    t "You're kidding right?!"
    t "Hey you, leave them alone!"
    hide a neu
    show b angry at left
    b "What are you his mom?"
    b "Whatever, this isn't worth my time."
    hide b angry 
    show j cry at left
    hide t neu
    show t sad at right
    t "Jaq are you okay?!"
    j "It doesn't matter."
    t "Yes, it does."
    hide t sad
    hide j cry
    menu:
        "Want to come to the movies?":
            $ good_ending += 1
            jump choice_moviedate
        "We've got to go. We're seeing a movie.":
            $ bad_ending += 1
            jump choice_noalex
label choice_poorjaq:
    show b angry at left
    b "What are you his mom?"
    b "Whatever, this isn't worth my time."
    hide b angry
    show a neu at left
    a "Are you okay Jaq?"
    show j sad at right
    j "It doesn't matter."
    a "It does!" 
    j "I'm okay..."
    e "Do you want to invite Jaq to the movies?"
    hide j sad
    hide a neu
    menu:
        "Want to come to the movies?":
            $ good_ending += 1
            jump choice_moviedate
        "We've got to go. We're seeing a movie.":
            $ bad_ending += 1
            jump choice_noalex
label choice_noalex:
    hide park bg
    scene movietheater bg
    show r happy at right
    r "We should see a horror film!"
    show t happy at left
    t "We should see a rom-com!!"
    hide t happy
    show t sad at left
    t "Hey where's Jaq?"
    show a sad
    a "Uh..."
    a "They couldn't make it."
    hide movietheater bg
    show classroom bg
    hide r happy
    hide t sad
    hide a sad
    show a neu at left
    show j neu at right
    e "Time skip, yet again!"
    e "The next day, at school."
    j "Alex? Can I talk to you?"
    hide j sad
    hide a neu
    menu:
        "Listen to Jaq and Sympathize.":
            $ good_ending += 1
            jump choice_sympathy
        "Ignore.":
            $ bad_ending += 1
            jump choice_veryrude
label choice_moviedate:
    hide park bg
    show movietheater bg
    e "Later, at the movies."
    show r happy at right
    r "I say we watch a horror movie."
    show t happy at left
    t "We should watch a rom com."
    show j neu 
    j "I'm okay with anything." 
    hide r happy
    hide t happy
    hide j neu
    hide movietheater bg
    scene classroom bg
    e "Time skip, yet again!"
    e "The next day, at school."
    show j sad at right
    show a neu at left
    j "Alex? Can I talk to you?"
    hide j sad
    hide a neu
    menu:
        "Listen to Alex and Sympathize.":
            $ good_ending += 1
            jump choice_sympathy
        "Ignore.":
            $ bad_ending += 1
            jump choice_veryrude
label choice_veryrude:
    show a neu at left
    a "I've got to go to class, sorry Jaq."
    show j angry at right
    j "No!"
    j "I've been exhausted, but I haven't been able to sleep."
    j "I've been constantly anxious and lost interest in most things."
    j "Nothing really makes me happy."
    j"And before you go, I have a question for you!"
    hide j angry
    show j angrycry at right
    j "Do you even consider me your friend!?"
    hide j angrycry
    hide a neu
    if good_ending > bad_ending:
        show a exc at left
        a "Of course I consider you my friend!"
        hide a exc
        jump choice_yesss
    if bad_ending > good_ending:
        show a sad at left
        a "No, I hate you."
        hide a sad
        jump choice_nah
label choice_sympathy:
    show a neu at left
    a "What's up Jaq, what's wrong?"
    show j sad at right
    j "I think, there's something wrong with me."
    a "What do you mean?"
    j "Lately I haven't been myself."
    hide a neu
    show a sad at left
    j "I've been exhausted, but I haven't been able to sleep."
    j "I've been constantly anxious and lost interest in most things."
    j "Nothing really makes me happy."
    hide j sad
    show j cry at right
    a "Jaq, I'm be here for you."
    a "You don't always have to be happy."
    a "I'm always here for you to talk to."
    hide j cry
    show j sad at right
    j "... Thanks."
    hide j sad
    hide a sad
    hide classroom bg
    scene park bg
    e "Yet another time skip because we have no sense of time."
    e "Later, at the park. After spending quality time together..."
    show j sad at right
    show a happy at left
    a "Hanging out with you has been fun. Do you want to get ice cream?"
    j "Hey Alex, can I ask you something else?"
    j  "Do you consider us friends?"
    hide j sad
    hide a happy
    if good_ending > bad_ending:
        show a exc at left
        a "Of course I consider you my friend!"
        hide a exc
        jump choice_yesss
    if bad_ending > good_ending:
        show a sad at left
        a "No, I hate you."
        hide a sad
        jump choice_nah
label choice_nah:
    show j angrycry at right
    j "I should've known."
    j "Forget it, I'm sick of trying to be good enough for you."
    show t sad at left
    t "How could you, Alex?"
    t "Leave us alone!"
    show r sad 
    r "Don't bother talking to us."
    "Failure..."
    jump choice_credits
label choice_yesss:
    show a exc at left
    show j sad at right
    a "Jaq! Of course you're my friend!"
    a "You're amazing and so cool!"
    hide j sad
    show j happy at right
    a "In fact I consider you one of my best friends."
    a "You make me happy...So, I wanna do the same for you!"
    j "Thank you...Thank you so much Alex!"
    a "Do you want to go get ice cream?"
    j "YEAH!"
    hide park bg
    scene icecream bg
    hide j happy
    hide a exc
    show a icecream at left
    show j icecream at right  
    j "You know, Alex, sometimes i feel like...'I'm in a nightmare I cant wake up from'" 
    a "..." 
    j "..." 
    a "I-Is that a twilight zone reference" 
    j "haha yup. Nice catch!"
    a "hahaha. Cool!" 
    j "Hey Alex...Thanks again, for everything." 
    a "Of course."
    hide j icecream
    hide a icecream
    "Congrats!!"
    jump choice_credits
label choice_credits:
    hide icecream bg
    scene credits bg
    "Credits"  with dissolve
    "Solacam Inc."  with dissolve
    "Storyline by" with dissolve
    "Solana Martinez, Camille Sanchez and Ilana Grossman" with dissolve
    "Character Design by" with dissolve
    "Solana Martinez, Camille Sanchez and Ilana Grossman" with dissolve
    "Program: Ren'Py" with dissolve
return