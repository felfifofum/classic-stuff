class Zombie():

    def __init__(self, zombieName):
        self.name = zombieName
        self.health = 100
        self.legs = 2
        self.arms = 2

    def set_name(self):
        self.name = zombieName

    def get_info(self):
        print("Your zombie's name: ", self.name)
        print("Your zombie's health is,", self.health)
        print("Your zombie has,",self.legs, "legs")
        print("Your zombie has,",self.arms, "arms")
        print()

    def attack(self):
        print(self.name, "has MADE an attacked!")

        print()
        self.health = self.health - 10 ##could be random number

        if self.arms > 0:
              self.arms = self.arms - 1

        else:
              print("No arms left to obliterate!")

    def regenerate(self):
        print(self.name, "has been revived!")

        print()

        self.health = self.health + 30

        if self.health > 100:

            self.health = 100

zombie1 = Zombie("")

#main program

zombieName = input("Enter a name for the ultimate destructor!: ")

print()
zombie1.set_name()
zombie1.get_info()

while True:
    print()
    print("1 to attack")
    print("2 to regenerate")
    print("3 to display zombie details")
    print()
    choice = int(input("Enter option: "))
    print()

    if choice == 1:
        
        zombie1.attack()
        zombie1.get_info()

    elif choice == 2:
        zombie1.regenerate()
        zombie1.get_info()

    elif choice == 3:
        zombie1.get_info()

    


        
