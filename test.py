def c_skills():
    restart = False
    skill_points = 60
    c_skill = {'One-Hand' : 0, 'Two-Hand' : 0, 'Fisticuffs' : 0, 'Marksmanship' : 0, 'Stamina' : 0, 'Agility' : 0}
    for skill in c_skill:
            skill_entry = int(raw_input('How many points would you like to add to ' + skill + '? '))
            if skill_entry > skill_points:
                print "You don't have enough points!"
                print "Let's try this again."
                restart = True
                if restart == True:
                    c_skills()
            else:    
                c_skill[skill] = skill_entry
                skill_points = skill_points - skill_entry
                print 'You have', skill_points, 'points left.'

c_skills()