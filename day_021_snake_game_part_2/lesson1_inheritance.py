class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale.")

# Fish inherits attributes and methods from Animal class
class Fish(Animal):
    def __init__(self):
        # Trigger a call to the super class you're drawing from
        super().__init__()

    def breathe(self):
        # Calling the super class works, but you can also bring more functionality into the method - like 'doing this underwater'.
        super().breathe()
        print("doing this underwater.")

    def swim(self):
        print("moving in water.")

nemo = Fish()
nemo.breathe()