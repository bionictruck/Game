import json
from character import c_name, c_skills

print 'Welcome to <The World>!'

while True:
    try:
        restart = False
        char_choice = raw_input("Would you like to (C)reate a new character or (L)oad an existing one? ").lower()
        if char_choice == 'c':
            cname = c_name()
            # cstory = c_story()
            print 'You have 40 skill points available to customize your character.'
            print 'Points must be distributed between 6 skills. Each already has 50 points.'
            print 'One-Hand - One handed weapons such as daggers and short swords'
            print 'Two-Hand - Two handed weapons such as long swords or sledge hammers'
            print 'Fisticuffs - Straight up fighting with fists'
            print 'Marksmanship - How well you shoot a gun or bow'
            print 'Agility - How quickly you can avoid getting hit'
            print 'Stamina - How many hit points you have'
            cskill = c_skills()
        else:
            print "That is an invalid selection, try again."
    except:
        break

    save_c = raw_input('Would you like to save your character? ').lower()
    if save_c == 'y':
        char_info = [cname, cskill]
        json.dump(char_info, open("save.txt", 'w'))
        print "Character saved!"
        break
    else:
        restart = True
        if restart == True:
            c_skills()