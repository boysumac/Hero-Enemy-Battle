

# create battle between two python_version_tuple

import random
from characters import my_super_hero
from characters import villan_one
from characters import villan_two

print (my_super_hero['name'])
print (villan_one['name'])
print (villan_one['equipment'])


print (my_super_hero['name'], "has", my_super_hero['health'], "health points")
print (villan_one['name'], "has", villan_one['health'], "health points")

# assign random attack damage for super hero and villan one 

while my_super_hero['health'] > 0 and villan_one['health'] > 0:
    super_hero_damage = random.choice(my_super_hero['attacks'])
    villan_one_damage = random.choice(villan_one['attacks'])

# print the random attack and damage to super hero and villan one    
    
    print(f"{my_super_hero['name']} attacked {villan_one['name']} with {super_hero_damage [0]} for {super_hero_damage [1]} damage")
    print(f"{villan_one['name']} attacked {my_super_hero['name']} with {villan_one_damage [0]} for {villan_one_damage [1]} damage")
 
 # Calculate the remainig life of super hero and villan one  
    
    my_super_hero['health'] -= villan_one_damage[1]
    villan_one['health'] -= super_hero_damage[1]

 # Print the remaining life of super hero and villan one
    print (f"{my_super_hero ['name']} has {my_super_hero ['health']} life remaining")
    print (f"{villan_one ['name']} has {villan_one ['health']} life remaining")

  # Check if super hero or villan one is dead

    if my_super_hero['health'] <= 0:
        print(f"{my_super_hero['name']} has died and {villan_one['name']} wins")
    if villan_one['health'] <= 0:   
        loot = (list(villan_one['equipment']))
        
        my_super_hero['equipment'].add(loot[0])
        print(f"{villan_one['name']} has died and {my_super_hero['name']} wins")
        print(f"{my_super_hero['name']} looted {loot} from {villan_one['name']}")
# Add villan one equipment to super hero equipment
       
        
        

# assign random attack damage for super hero and villan two 
while my_super_hero['health'] > 0 and villan_two['health'] > 0:
    super_hero_damage = random.choice(my_super_hero['attacks'])
    villan_two_damage = random.choice(villan_two['attacks'])

# print the random attack and damage to super hero and villan two     
    
    print(f"{my_super_hero['name']} attacked {villan_two['name']} with {super_hero_damage [0]} for {super_hero_damage [1]} damage")
    print(f"{villan_two['name']} attacked {my_super_hero['name']} with {villan_two_damage [0]} for {villan_two_damage [1]} damage")

# Calculate the remainig life of super hero and villan two 
    
    my_super_hero['health'] -= villan_two_damage[1]
    villan_two['health'] -= super_hero_damage[1]

 # Print the remaining life of super hero and villan two
    print (f"{my_super_hero ['name']} has {my_super_hero ['health']} life remaining")
    print (f"{villan_two ['name']} has {villan_two ['health']} life remaining")

  # Check if super hero or villan two is dead

    if my_super_hero['health'] <= 0:
        print(f"{my_super_hero['name']} has died and {villan_two['name']} wins")
    if villan_two['health'] <= 0:    
        print(f"{villan_two['name']} has died and {my_super_hero['name']} wins")


#def battle():
   
pass