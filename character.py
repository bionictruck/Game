def c_name():
    ### Create the character name. Must be greater than 2 characters
        c_name = raw_input("Enter a name: ")
        if len(c_name) > 2:
            print "Hello " + c_name + ", prepare for your adventure." + "\n"
            return c_name
        print "Sorry the name must contain at least 3 characters"

# def c_story():
#     while True:
#         try:
#             story = raw_input("Add a backstory 500 characters or less. Press Enter to skip: " "\n")
#             if len(story) < 500:
#                 return 'Character Story: ' + story + "\n"
#             else:
#                 print "Backstory is restricted to 500 characters"
#         except:
#             break

def c_skills():
    skill_points = 40
    c_skill = {'One-Hand' : 50, 'Two-Hand' : 50, 'Fisticuffs' : 50, 'Marksmanship' : 50, 'Stamina' : 50, 'Agility' : 50}
    print 'You have 40 skill points available to customize your character.'
    print 'Points must be distributed between 6 skills. Each already has 50 points.'
    print 'One-Hand - One handed weapons such as daggers and short swords'
    print 'Two-Hand - Two handed weapons such as long swords or sledge hammers'
    print 'Fisticuffs - Straight up fighting with fists'
    print 'Marksmanship - How well you shoot a gun or bow'
    print 'Agility - How quickly you can avoid getting hit'
    print 'Stamina - How many hit points you have'
    ### For each skill in c_skills
    for skill in c_skill:
        ### Prompt the user for a value
        skill_entry = raw_input('How many points would you like to add to ' + skill + '? ')
        try:
            #### Convert to a numeric value
            skill_entry = int(skill_entry)
            ### If the value entered is greater than the points left, restart the iteration
            if skill_entry > skill_points:
                print "You don't have enough points!"
                print "Let's try this again."
                c_skills()
            ### Otherwise add the value to the skill and subtract it from the number of points left
            else:    
                c_skill[skill] = skill_entry + c_skill[skill]
                skill_points = skill_points - skill_entry
                print 'You have', skill_points, 'points left.'
            ### If the value is not numeric, assign a value of 0 to that skill
        except:
            print 'Assiging a value of 0 to ' + skill + '.'
            skill_entry = 0
    return c_skill

