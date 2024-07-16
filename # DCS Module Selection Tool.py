# DCS Module Selection Tool
# print ('''
#               F-16

# ,-----.
# \======'.
#  \  {}   '.
#   \   \/ V '.
#    \  || |   '._                                 _,cmmmnc,_
#     \___68FS___\'-._=----+- _______________,.-=:3H)###C--  `c._
#     :|=--------------`---"'`.   `  `.   `.   `,   `~""==="~`    `'-.___
#   ,dH] '       =(*)=         :       ---==;=--;  .   ;    +-- -_ .-`
#   :HH]_:______________  ____,.........__     _____,.----=-"~ `
#   ;:""'"'----._.------\`  :          .   `.'`'"'"'"P
#   |:      .-'==-.__)___\. :        .   .'`___L~___(
#   |:  _.'`       '|   / \.:      .  .-`""`
#   `'"'            `--'   \:    ._.-'
# dew                      }_`============>-))
#        ''')

# Intro
print ("Welcome to the DCS Module Selector")
mission_type = input ("What kind of scenario do you want to practice today? A/A, A/G or not sure? ").lower()
if mission_type == "a/a":
    print ("Recommended modules include: F-15C, F-16C, F-22A")
    CAP_Preface = input ("Do you want to engage primarily in BVR engagements? Yes or No? ").lower()
    if CAP_Preface == "yes":
        stealth = input ("Do you want stealth? Yes or No? ").lower()
        if stealth == "yes":
            print ("Recommend you select F-22A")
        elif stealth == "no":
            print ("Recommend you select F-15C Module")
        else:
            print ("Does not recognize input, try again")
elif mission_type == "a/g":
    print ("""Recommended modules include:
           Fixed Wing: A-10CII, AV-8B, F-15E, F-16C, 
           Rotary Wing: AH-64D, OH-58D, UH-1H""")
elif mission_type == "not sure":
    MultiRoleChallenge = input ("Are you looking for multi-role?").lower()
    if MultiRoleChallenge == "yes":
        print ("I would recommend F-15E or the F-16C")
    else:
        print ('''There are two tracks to follow:
               For Fixed Wing, I would recommend the A-10CII, the AV-8B
               For Rotary Wing, I would recommend the AH-64D, OH58D, or the UH-1H''')
else:
    print ("Input not recognized")