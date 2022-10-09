# create battle between super hero and villan

import random

from characters import my_super_hero
from characters import villan_one
from characters import villan_two
from characters import villan_three

# Print intial super hero and villan health

print (my_super_hero['name'], "begins with", my_super_hero['health'], "health points")
print (villan_one['name'], "begins with", villan_one['health'], "health points")

# Assign random attack damage for super hero and villan one 

def random_attack_damage_1 ():
    while my_super_hero['health'] > 0 and villan_one['health'] > 0:
        super_hero_damage = random.choice(my_super_hero['attacks'])
        villan_one_damage = random.choice(villan_one['attacks'])

#Print random attack damage   
        print(f"{my_super_hero['name']} attacked {villan_one['name']} with {super_hero_damage [0]} for {super_hero_damage [1]} damage")
        print(f"{villan_one['name']} attacked {my_super_hero['name']} with {villan_one_damage [0]} for {villan_one_damage [1]} damage")  

# Calculate and print the remainig life of super hero and villan one  
        villan_one['health'] -= super_hero_damage[1]   
        print (f"{villan_one ['name']} has {villan_one ['health']} life")
        if villan_one ['health'] >= 0:
            my_super_hero['health'] -= villan_one_damage[1]
            print (f"{my_super_hero ['name']} has {my_super_hero ['health']} life")
        else:
            print (f"{my_super_hero ['name']} has {my_super_hero ['health']} life")
# Check if super hero or villan one is dead
def check_if_dead_1():
    if villan_one['health'] <= 0:
        print(f"{villan_one['name']} is dead and {my_super_hero['name']} wins")
   
    elif my_super_hero['health'] <= 0:
        print(f"{my_super_hero['name']} has died and {villan_one['name']} wins")

# Superhero loots equipment if villon dies
def loot_equipment_1():
    if villan_one['health'] <= 0:
        my_super_hero['equipment'].update(villan_one['equipment'])
        print(f"{my_super_hero['name']} has looted {villan_one['equipment']} from {villan_one['name']}")
        print(f"{my_super_hero['name']} has {my_super_hero['equipment']} equipment")

#random_attack_damage_1()
#check_if_dead_1()
#loot_equipment_1()

def random_attack_damage_2():
    while my_super_hero['health'] > 0 and villan_two['health'] > 0:
        super_hero_damage = random.choice(my_super_hero['attacks'])
        villan_two_damage = random.choice(villan_two['attacks'])

# Print random attack damage   
        print(f"{my_super_hero['name']} attacked {villan_two['name']} with {super_hero_damage [0]} for {super_hero_damage [1]} damage")
        print(f"{villan_two['name']} attacked {my_super_hero['name']} with {villan_two_damage [0]} for {villan_two_damage [1]} damage")  

# Calculate and print the remainig life of super hero and villan two
        villan_two['health'] -= super_hero_damage[1]   
        print (f"{villan_two ['name']} has {villan_two ['health']} life")
        
        if villan_two ['health'] >= 0:
            my_super_hero['health'] -= villan_two_damage[1]
            print (f"{my_super_hero ['name']} has {my_super_hero ['health']} life")

        else:
            print (f"{my_super_hero ['name']} has {my_super_hero ['health']} life") 
        
# Check if super hero or villan two is dead
def check_if_dead_2():
    if villan_two['health'] <= 0:
        print(f"{villan_two['name']} is dead and {my_super_hero['name']} wins")
   
    elif my_super_hero['health'] <= 0:
        print(f"{my_super_hero['name']} has died and {villan_two['name']} wins")

# Superhero loots equipment if villon dies
def loot_equipment_2():
    if villan_two['health'] <= 0:
        my_super_hero['equipment'].update(villan_two['equipment'])
        print(f"{my_super_hero['name']} has looted {villan_two['equipment']} from {villan_two['name']}")
        print(f"{my_super_hero['name']} has {my_super_hero['equipment']} equipment")

# random_attack_damage_2()
# check_if_dead_2()
# loot_equipment_2()

# Assign random attack damage for super hero and villan three 

def random_attack_damage_3():
    while my_super_hero['health'] > 0 and villan_three['health'] > 0:
        super_hero_damage = random.choice(my_super_hero['attacks'])
        villan_three_damage = random.choice(villan_three['attacks'])

#Print random attack damage   
        print(f"{my_super_hero['name']} attacked {villan_three['name']} with {super_hero_damage [0]} for {super_hero_damage [1]} damage")
        print(f"{villan_three['name']} attacked {my_super_hero['name']} with {villan_three_damage [0]} for {villan_three_damage [1]} damage")  

# Calculate and print the remainig life of super hero and villan three 
        villan_three['health'] -= super_hero_damage[1]   
        print (f"{villan_three ['name']} has {villan_three ['health']} life")
        if villan_three ['health'] >= 0:
            my_super_hero['health'] -= villan_three_damage[1]
            print (f"{my_super_hero ['name']} has {my_super_hero ['health']} life")
        else:
            print (f"{my_super_hero ['name']} has {my_super_hero ['health']} life")
# Check if super hero or villan three is dead
def check_if_dead_3():
    if villan_three['health'] <= 0:
        print(f"{villan_three['name']} is dead and {my_super_hero['name']} wins")
   
    elif my_super_hero['health'] <= 0:
        print(f"{my_super_hero['name']} has died and {villan_three['name']} wins")

# Superhero loots equipment if villon dies
def loot_equipment_3():
    if villan_three['health'] <= 0:
        my_super_hero['equipment'].update(villan_three['equipment'])
        print(f"{my_super_hero['name']} has looted {villan_three['equipment']} from {villan_three['name']}")
        print(f"{my_super_hero['name']} has {my_super_hero['equipment']} equipment")

#random_attack_damage_3()
#check_if_dead_3()
#loot_equipment_3()

def run_battle ():
    random_attack_damage_1()
    check_if_dead_1()
    loot_equipment_1()
    random_attack_damage_2()
    check_if_dead_2()
    loot_equipment_2()
    random_attack_damage_3()
    check_if_dead_3()
    loot_equipment_3()  
    
run_battle ()



