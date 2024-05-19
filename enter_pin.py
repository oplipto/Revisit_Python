
# pin = 2345

# while True:
#     user_input = int(input("Enter your 4 digit pin: "))
#     if user_input == pin:
#          print("Pin accepted")
#          break
#     else:
#         print("Invalid pin. Please try again.")


# number = 0

# while number < 10:
#     print(number)
#     number += 1
#     if number == 11:
#         break
#     else:
#         print("We are done.")


guess = 0

while guess != 10:
    guess = int(input("Guess a number between 1 and 10: "))
    if guess != 10:
        print("Try again.")
    else:
        print("You guessed it right!")
        break


