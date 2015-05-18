import json
from character import c_name, c_skills

print 'Welcome to <The World>!'

### Ask the user if they like to Create or Load a character
while True:
    char_choice = raw_input("Would you like to (C)reate a new character or (L)oad an existing one? ").lower()
    ### If creating, run through the c_name and c_skills in character.py
    if char_choice == 'c':
        cname = c_name()
        # cstory = c_story()
        cskill = c_skills()
        break
    print "That is an invalid selection, please try again."

### Saving the character
while True:
    save_c = raw_input('Would you like to save your character? (Enter Y or N) ').lower()
    #### If Y the dump character to save.txt
    if save_c == 'y':
        char_info = [cname, cskill]
        json.dump(char_info, open("save.txt", 'w'))
        print "Character saved!"
        break
    ### If the value is not Y or N, prompt to create the character again
    print "Please create your character again."
    c_name()
    c_skills()

