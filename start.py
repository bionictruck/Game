from character import c_name, c_story, c_skills

print 'Welcome to <The World>!'

while True:
    try:
        char_choice = raw_input("Would you like to (C)reate a new character or (L)oad an existing one? ").lower()
        if char_choice == 'c':
            cname = c_name()
            cstory = c_story()
            print 'You have 60 skills points available to customize your character.'
            print 'Points must be distributed between 6 skills.'
            print 'One-Hand - One handed weapons such as daggers and short swords'
            print 'Two-Hand - Two handed weapons such as long swords or sledge hammers'
            print 'Fisticuffs - Straight up fighting with fists'
            print 'Marksmanship - How well you shoot a gun or bow'
            print 'Agility - How quickly you can avoid getting hit'
            print 'Stamina - How many hit points you have'
            cskill = c_skills()
            break
        else:
            print "That is an invalid selection, try again."
    except:
        break

print cname
print cstory
print cskill