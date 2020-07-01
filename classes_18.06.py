class Fruit:
    def __init__(self, name, color, flavor, poison):
        self.fruit_name = name
        self.fruit_color = color
        self.fruit_flavor = flavor
        self.poison = poison
    
    def info(self):
        print(f"Name:{self.fruit_name}, color:{self.fruit_color}, flavor:{self.fruit_flavor}, Poison:{self.poison}")

    def is_ediable(self):
        if self.poison == True:
            print("dont eat me")
        else:
            print("eat plz me")
        


fruit1 = Fruit("лимон","желтый","кислый",False)
fruit2= Fruit("watermelon","green","sweet",False)
fruit1.info()
fruit2.info()
fruit1.is_ediable()












        
    