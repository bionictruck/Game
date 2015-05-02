def c_name():
    while True:
        try:
            c_name = raw_input("Enter a name: ")
            if len(c_name) > 2:
                print "Hello " + c_name + ", prepare for your adventure." + "\n"
                return c_name
            else:
                print "Sorry the name must contain at least 2 characters"
        except:
            break

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
    restart = False
    skill_points = 40
    c_skill = {'One-Hand' : 50, 'Two-Hand' : 50, 'Fisticuffs' : 50, 'Marksmanship' : 50, 'Stamina' : 50, 'Agility' : 50}
    for skill in c_skill:
            skill_entry = int(raw_input('How many points would you like to add to ' + skill + '? '))
            if skill_entry > skill_points:
                print "You don't have enough points!"
                print "Let's try this again."
                restart = True
                if restart == True:
                    c_skills()
            else:    
                c_skill[skill] = skill_entry + c_skill[skill]
                skill_points = skill_points - skill_entry
                print 'You have', skill_points, 'points left.'
    return c_skill