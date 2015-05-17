import json
from character import c_name, c_skills

print 'Welcome to <The World>!'


while True:
    char_choice = raw_input("Would you like to (C)reate a new character or (L)oad an existing one? ").lower()
    if char_choice == 'c':
        cname = c_name()
        # cstory = c_story()
        cskill = c_skills()
        break
    print "That is an invalid selection, please try again."

while True:
    save_c = raw_input('Would you like to save your character? ').lower()
    if save_c == 'y':
        char_info = [cname, cskill]
        json.dump(char_info, open("save.txt", 'w'))
        print "Character saved!"
        break
    print "Please create your character again."
    c_name()
    c_skills()

