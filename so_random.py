
import random
from functools import reduce

prefixes = ['Mystic', 'Golden', 'Dark', 'Shadow', 'Silver']
suffixes = ['storm', 'song', 'fire', 'blade', 'whisper']

def create_fantasy_name(list_1, list_2):
  return random.choice(list_1) + ' ' + random.choice(list_2)

def capitalize_suffix(name):
  return name.capitialize()

suffix_list = [create_fantasy_name(prefixes, suffixes) for i in range(10)]

random_name = random.choice(suffix_list)

def fire_in_name(name):
  return 'fire' in name.lower()

def concatenate_names(acc, name):
  return acc + ' ' + name

def display_name_info():
  print('Random name:', random_name)
  for name in suffix_list:
    print(name)
  print('Name contains "fire":', fire_in_name(random_name))
  print('All names:', reduce(concatenate_names, suffix_list))

display_name_info()
  


  

  