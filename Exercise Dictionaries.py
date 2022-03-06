#1 Create a user profile for your new game. This user profile will be stored in a dictionary with keys: 'age', 'username', 'weapons', 'is_active' and 'clan'
user_profile = {'username': 'PG',
                'age': 25,
                'weapons' : ['katana', 'shuriken', 'kunai'],
                'is_active' : True,
                'clan' : 'oskomixereca'}

print(f'1)\n{user_profile}')

#2 iterate and print all the keys in the above user.
print('\n2)')
for k in user_profile.keys():
    print(k)

#3 Add a new weapon to your user
user_profile.update({'weapons':['katana', 'shuriken', 'kunai', 'bet']})
print(f'\n3)\n{user_profile["weapons"]}')

#4 Add a new key to include 'is_banned'. Set it to false
user_profile['is_banned'] = False
print(f'\n4) \n{user_profile}')

#5 Ban the user by setting the previous key to True
user_profile.update({'is_banned' : True})
print(f'\n5) \n{user_profile}')

#6 create a new user2 my copying the previous user and update the age value and username value.
user_profile2 = user_profile
user_profile2.update({'username' : 'Julia',
                      'age': 22,
                      'weapons' : ['spoon', 'cat', 'shoe']})
print(f'\n6) \n{user_profile2}')