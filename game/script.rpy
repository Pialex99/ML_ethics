# The script of the game goes in this file.

define narator = Character("Narator", color="#ffffff")

define me = Character("Me", color="#c8c8ff")
define friend = Character("ML enthousiastic friend")
define firend = Character("Another ML enthousiastic friend")
define firend2 = Character("Still another ML enthousiastic friend")
define firend3 = Character("Fourth ML enthousiastic friend")


label start:

menu:

    "Deepfake":
        jump deepfake

    "Quit":
        return

label deepfake:

    show friends happy

    friend "Hey ! Since we are all interessted in ML why don't we make a small competition together ?"

    firend "Yeah ! Great idea !!"
    firend2 "We could compete with a game like chess or something like that ?"
    firend3 "Or since the classes are prerecorded, we could train models to make deepfakes of the teachers"

    "All together" "Oh yes ! Great idea !!"

    jump start
