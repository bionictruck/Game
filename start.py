import character

c_name = ''

print 'Welcome to <The World>!'
char_choice = raw_input("Would you like to (C)reate a new character or (L)oad an existing one? ").lower()

if char_choice == 'c':
    character.c_create()
else:
    end