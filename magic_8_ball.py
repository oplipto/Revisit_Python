
import random

print("Welcome to the Magic 8 Ball!")

question = input("Ask the Magic 8 Ball a question: ")

answer = random.randint(1, 9)

if answer == 1:
    print("Yes - definitely.")

elif answer == 2:
    print("It is decidedly so.")

elif answer == 3:
    print("Without a doubt.")

elif answer == 4:
    print("Reply hazy, try again.")

elif answer == 5:
    print("Ask again later.")

elif answer == 6:
    print("Better not tell you now.")

elif answer == 7:
    print("My sources say no.")

elif answer == 8:
    print("Outlook not so good.")

elif answer == 9:
    print("Very doubtful.")

else:
    print("Error")



