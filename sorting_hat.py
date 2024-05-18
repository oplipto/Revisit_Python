

Gryffindor = 0
Hufflepuff = 0
Ravenclaw = 0
Slytherin = 0

question_1 = int(input('''Q1) Do you like Dawn or Dusk?
    1) Dawn
    2) Dusk
       : '''))

if question_1 == 1:
    Gryffindor += 1
    Ravenclaw += 1

elif question_1 == 2:
    Hufflepuff += 1
    Slytherin += 1

else:
    print("Invalid input")

question_2 = int(input('''Q2) When I’m dead, I want people to remember me as:
    1) The Good
    2) The Great
    3) The Wise
    4) The Bold
       : '''))

if question_2 == 1:
    Hufflepuff += 2

elif question_2 == 2:
    Slytherin += 2

elif question_2 == 3:
    Ravenclaw += 2

elif question_2 == 4:
    Gryffindor += 2

else:
    print("Invalid input")

question_3 = int(input('''Q3) Which kind of instrument most pleases your ear?
    1) The violin
    2) The trumpet
    3) The piano
    4) The drum
       : '''))

if question_3 == 1:
    Slytherin += 4

elif question_3 == 2:
    Hufflepuff += 4

elif question_3 == 3:
    Ravenclaw += 4

elif question_3 == 4:
    Gryffindor += 4

else:
    print("Invalid input")

result = max(Gryffindor, Hufflepuff, Ravenclaw, Slytherin)

if result == Gryffindor:
    print("You belong in Gryffindor!")

elif result == Hufflepuff:
    print("You belong in Hufflepuff!")

elif result == Ravenclaw:
    print("You belong in Ravenclaw!")

elif result == Slytherin:
    print("You belong in Slytherin!")

else:
    print("Invalid input")