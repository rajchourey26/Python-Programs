class Dog:
    def __init__(self, name):
        self.name = name  # Give the dog a name

    def bark(self):       # The method (action)
        print(f"{self.name} says Woof!")

# --- This is the part that makes it "talk" ---
my_dog = Dog("Rocky")    # Create an instance (the "object")
my_dog.bark()            # Call the method
