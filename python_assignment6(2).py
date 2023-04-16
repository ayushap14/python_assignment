class Dog:
    def __init__(self, name, age, coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color

    def description(self):
        print(f"{self.name} is {self.age} years old.")

    def get_info(self):
        print(f"{self.name} has {self.coat_color} coat color.")


class JackRussellTerrier(Dog):
    def __init__(self, name, age, coat_color):
        super().__init__(name, age, coat_color)

    def hunting(self):
        print(f"{self.name} is a Jack Russell Terrier and is a skilled hunter.")

    def energetic(self):
        print(f"{self.name} is a Jack Russell Terrier and is highly energetic.")


class Bulldog(Dog):
    def __init__(self, name, age, coat_color):
        super().__init__(name, age, coat_color)

    def loyal(self):
        print(f"{self.name} is a Bulldog and is known for its loyalty.")

    def stubborn(self):
        print(f"{self.name} is a Bulldog and can be stubborn at times.")


# Create objects and implement the above functionalities
dog1 = JackRussellTerrier("Jackie", 5, "white")
dog1.description()
dog1.get_info()
dog1.hunting()
dog1.energetic()

dog2 = Bulldog("Buddy", 7, "brown")
dog2.description()
dog2.get_info()
dog2.loyal()
dog2.stubborn()
