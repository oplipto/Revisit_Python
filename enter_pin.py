
# pin = 2345

# while True:
#     user_input = int(input("Enter your 4 digit pin: "))
#     if user_input == pin:
#          print("Pin accepted")
#          break
#     else:
#         print("Invalid pin. Please try again.")


number = 0

while number < 10:
    print(number)
    number += 1
    if number == 11:
        break
    else:
        print("We are done.")