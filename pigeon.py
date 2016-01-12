import random

class Pigeon:
    """A Pigeon """

    def __init__(self, name, tribe, color, fly = True):
        self.name = name
        self.tribe = tribe
        self.color = color
        self.fly = fly

    def canFly(self):
    	if self.fly == True:
    		return "This pigeon is good to fly"
    	else:
    		return "This bird is grounded!"

    def __str__(self):
        return "Hello my name is %s, I am from tribe %s, I am %s" %(self.name, self.tribe, self.color)


def PigeonMission():
    pigeonName = input("Select a pigeon from the Pigeoncove to fly a mission:  ").lower()
    count = pigeonNum

    for bird in pigeonCove:
        if pigeonName == bird.name:
            if bird.fly == True:
                print("Hurray watch it fly!")
                count-= 1
                if PigeonAdventure() == 3:
                    bird.fly = False
                break
            else:
                print("This bird is grounded!")
                count-= 1
                break
    if count == pigeonNum:
        print("Sorry that pigeon is not in your cove")


def PigeonAdventure():
    return random.randrange(0,9)





Roger = Pigeon("roger", "Speckle Beak", "Gray")
Mary  = Pigeon("mary", "BobbleHead", "White")
Squawk = Pigeon("squawk", "3 Toe", "Black")
Bobbette = Pigeon("bobette", "4 Toe", "Brown")

pigeonCove = [Roger, Mary, Squawk, Bobbette]
pigeonNum = len(pigeonCove)

for pigeon in pigeonCove:
	print(pigeon)
	print(pigeon.canFly(), "\n")



print("There are " + str(pigeonNum) + " pigeons in the cove right now")

PigeonMission()
PigeonAdventure()



	
