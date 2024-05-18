
height = int(input("Enter your Height: "))

credits = int(input("Enter your Credits: "))

if height >= 137 and credits >= 10:
    print("You can ride the Cyclone!")

elif credits > 10 and height < 137:
    print("Sorry, you are too short to ride the Cyclone.")

elif height >= 137 and credits < 10:
    print("Sorry, you do not have enough credits to ride the Cyclone.")

else:
    print("Sorry, you don't meet the requirements to ride the Cyclone.")