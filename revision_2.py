
# genz_slang = ['bestie', 'tea', 'cap', 'no cap', 'flex', 'fam', 'lit', 'sus', 'salty', 'GOAT', 'basic', 'extra', 'thirsty', 'savage', 'woke', 'shade', 'slay', 'snack', 'thicc', 'vibes', 'yeet', 'mood', 'clap back', 'squad', 'finesse', 'boujee', 'ratchet', 'bae', 'low key', 'high key', 'on fleek', 'turnt', 'fire']

# print(genz_slang)

# for slang in genz_slang:
#     print(slang)

# Tuples

# city = ('New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia', 'San Antonio', 'San Diego', 'Dallas', 'San Jose')

# friends = (
#     ('37.7749° N, 122.4194° W', 'San Francisco'),
#     ('34.0522° N, 118.2437° W', 'Los Angeles'),
#     ('40.7128° N, 74.0060° W', 'New York'),
#     ('41.8781° N, 87.6298° W', 'Chicago'),
# )

# print(city)
# print(friends)

# for c in city:
#     print(c)

# for f in friends:
#     print(f)

# Dictionaries

# Car = {
#     'Company': 'Lamborghini',
#     'Model': 'Aventador SVJ Convertible',
#     'Price': '$573,966',
# }

# print(Car)
# print(Car['Company'])
# print(Car['Model'])
# print(Car['Price'])

# print(Car.keys())
# print(Car.values())
# print(Car.items())

# Sets

# my_favorite_fruits = {'banana', 'watermelon', 'Mango', 'Grapes'}

# my_friend_favorite_fruits = {'banana', 'apple', 'orange', 'Grapes', 'Mango'}

# union_fruits = my_favorite_fruits.union(my_friend_favorite_fruits)
# print(union_fruits)

# intersection_fruits = my_favorite_fruits.intersection(my_friend_favorite_fruits)
# print(intersection_fruits)

# difference_fruits = my_favorite_fruits.difference(my_friend_favorite_fruits)
# print(difference_fruits)

player_1 = {
    'name': 'Lionel Messi',
    'position': 'Forward',
    'jersey_number': 30,
    'yards gained': 50,
    'touchdowns': 1,
}

player_2 = {
    'name': 'Cristiano Ronaldo',
    'position': 'Forward',
    'jersey_number': 7,
    'yards gained': 70,
    'touchdowns': 2,
}

player_3 = {
    'name': 'Neymar Jr',
    'position': 'Forward',
    'jersey_number': 10,
    'yards gained': 60,
    'touchdowns': 3,
}

players = [player_1, player_2, player_3]

# print(players)

player_2['jersey_number'] = 77

average_yards_gained = (player_1['yards gained'] + player_2['yards gained'] + player_3['yards gained']) / 3

print(average_yards_gained)