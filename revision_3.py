
# import math

from functools import reduce

# Functional Programming

# 1. Pure Functions

# def calculate_circle_area(radius):
#     return math.pi * radius ** 2

# print(calculate_circle_area(10))

# A longer_than_five_minutes() function for filter().

# def translator(language):
#     translations = {
#         'spanish': {'hello': 'hola', 'goodbye': 'adiós', 'thank you': 'gracias'},
#         'french': {'hello': 'bonjour', 'goodbye': 'au revoir', 'thank you': 'merci'},
#         'italian': {'hello': 'ciao', 'goodbye': 'arrivederci', 'thank you': 'grazie'}
# }
    
#     def translate_word(word):
#         return translations[language][word]
    
#     return translate_word

# translate_to_spanish = translator('spanish')
# print(translate_to_spanish('hello'))

# A minutes_to_seconds() function for map().
# List of songs with their durations (in minutes)

playlist = [('What Was I Made For?', 3.42), ('Just Like That', 5.05), ('Song 3', 6.8), ('Leave The Door Open', 4.02), ('I Can\'t Breath', 4.47), ('Bad Guy', 3.14)]

# def minutes_to_seconds(songs):
#     return songs * 60

# seconds = map(minutes_to_seconds, [song[1] for song in playlist])

# print(list(seconds))

# An add_durations() function for reduce().

# def add_durations(total, duration):
#     return total + duration

# total_duration = reduce(add_durations, [song[1] for song in playlist])

# print(total_duration)

numbers = [57, 10, 82, 36, 89, 46, 13, 23, 92, 48]
even = []
for number in numbers:
    if number % 2 == 0:
        even.append(number)
even_numbers = [number for number in numbers if number % 2 == 0]
print(even_numbers)



