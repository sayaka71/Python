# practice class
# URL: https://realpython.com/python3-object-oriented-programming/
# 2021.06.03
# @sayapy

#-------------------------<Yadon Class>-------------------------#
# Parent class
class Ydn:
    
    '''気分によってmessageを変えるヤドン'''
    def __init__(self, name="Yadon", age=26):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"{self.name} is {self.age} years old."

    def say_yaan(self, feel="happy"):
        if feel == "happy":
            feel = "YaaaaaaaaaN!!"
            return f"{self.name} says {feel}."
        elif feel == "Piyo":
            return f"{self.name} says {feel}."
        else:
            feel = "Yan..."
            return f"{self.name} says {feel}."

ydn = Ydn()
print(ydn)
print(ydn.say_yaan(), "\n")

#-------------------------<Hiyoko Class>-------------------------#
# Child class (super()!!)
class Hiyoko(Ydn):
    # super()
    def say_yaan(self, feel="Piyo"):
        return super().say_yaan(feel)

hyk = Hiyoko("Hiyoko", 23)
print(hyk)
print(hyk.say_yaan(), "\n")

#-------------------------<Practice>-------------------------#
# Practice class
class Car:
    """
    車の色と名前を答えるCarクラス　練習問題
    URL: https://realpython.com/python3-object-oriented-programming/
    """
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def out(self):
        print("The {} car has {} miles.".format(self.color, self.mileage))

blue_car = Car("blue", "20,000")
red_car = Car("red", "30,000")

blue_car.out()
red_car.out()   

# Practice inherit
class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old."

    def speak(self, sound):
        return f"{self.name} says {sound}."

class GoldenRetriever(Dog):
    # super()
    def speak(self, sound="Bark"):
        return super().speak(sound)

gld = GoldenRetriever("GoldenRetriever", 10)
print("\n", gld.speak())