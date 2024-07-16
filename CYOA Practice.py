print ('''
       F-16

,-----.
\======'.
 \  {}   '.
  \   \/ V '.
   \  || |   '._                                 _,cmmmnc,_
    \___68FS___\'-._=----+- _______________,.-=:3H)###C--  `c._
    :|=--------------`---"'`.   `  `.   `.   `,   `~""==="~`    `'-.___
  ,dH] '       =(*)=         :       ---==;=--;  .   ;    +-- -_ .-`
  :HH]_:______________  ____,.........__     _____,.----=-"~ `
  ;:""'"'----._.------\`  :          .   `.'`'"'"'"P
  |:      .-'==-.__)___\. :        .   .'`___L~___(
  |:  _.'`       '|   / \.:      .  .-`""`
  `'"'            `--'   \:    ._.-'
dew                      }_`============>-)
       ''')

# Intro
print ("Welcome to basic training ")
name = input("Please enter your name ")
training = input("Are you ready to continue " + name + "? Please write 'Yes' or 'No'. ").lower()
if training == "yes":
    airframe = input("What airframe would you like to learn? The F-16C, F-15C or the F-22A? ").lower()
    if airframe == "f-16c":
        viper_blocks = input("You can choose between Block 30 and 50. Which would you like? Write 30 or 50").lower()
        if viper_blocks == "30":
            print ("You are one mean dogfighter")
        elif viper_blocks == "50":
            print ("You've been assigned a F-16CM Block 50")
        else:
            print ("No airframe available")
    elif airframe == "f-15c":
        print ("Hop in, your Eagle is ready")
    elif airframe == "f-22a":
        print ("Watch the skies")
    else:
        print ("No wrong choice")

else:
    print ("Come back when you're ready.")