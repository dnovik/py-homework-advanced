

# Базовые классы

class Farmer:

    def feed(self):
        Animal.eat(self)
        Animal.hungry = False

        return Animal.hungry


    def __init__(self):
        pass

class Animal:

    hungry = True
    color = 'white'
    weight = 100

    def eat(self):
        print('omn, omn, omn')
        

    def voice(self):
        pass

    def give_benefit(self):
        pass

    def __init__(self):
        pass

class Goose(Animal):
    color = 'white'
    name = None

    def voice():
        print('Krya, krya, krya')

    def give_benefit():
        print('Collert my eggs')

class Cow(Animal):
    name = None

    def give_benefit():
        print ('Take my milk')

    def voice():
        print('Muuuuuu')

class Sheep(Animal):
    color = 'white'
    name = None

    def voice():
        print('Beeeee')

    def give_benefit():
        print('Take all my wool')

class Chicken(Animal):
    color = 'white'
    name = None

    def voice():
        print('Ko-Ko-Ko-Ko')

    def give_benefit():
        print('Take my eggs')

class Goat(Animal):
    color = 'white'
    name = None

    def voice():
        print('Meeee')

    def give_benefit():
        print ('Take my milk')

class Duck(Animal):
    color = 'white'
    name = None

    def voice():
        print('krya-krya-krya')

    def give_benefit():
        print ('Take my eggs')


# Производные классы

class Goose_Grey(Goose):
    color = 'grey'
    name = 'Grey'
    weight = 7000

class Goose_White(Goose):
    name = 'White'
    weight = 8000

class Cow_Manya(Cow):
    name = 'Manyka'
    weight = 80000

class Sheep_Barashek(Sheep):
    name = 'Barashek'
    weight = 18000

class Sheep_Curly(Sheep):
    name = 'Curly'
    weight = 18000

class Chicken_CoCo(Chicken):
    name = 'Co-Co'
    weight = 1200

class Chiken_KuKaReKu(Chicken):
    name = 'Ku-Ka-Re-Ku'
    weight = 1200

class Goat_Horns(Goat):
    name = 'Horns'
    weight = 50000

class Goat_Hooves(Goat):
    name = 'Hooves'
    weight = 50000

class Duck_Kryakva(Duck):
    name = 'Kryakva'
    weight = 3000

# список домашних животных

animals = [Goose_Grey, Goose_White, Cow_Manya, 
Sheep_Barashek, Sheep_Curly, Chicken_CoCo, Chiken_KuKaReKu, 
Goat_Horns, Goat_Hooves, Duck_Kryakva]


# вычислим общий вес животных и самое тяжелое животное

total_wieght = 0
max_weight = 0

for animal in animals:
    total_wieght += animal.weight
    if max_weight < animal.weight:
        max_weight = animal.weight
        animal_name = animal.name

print(f'Общий вес всех животных {total_wieght}')
print(f'Самое тяжелое животное - это {animal_name} весом {max_weight}')


# покормим животных

for animal in animals:
    print(animal.name)
    Farmer.feed(animal)
    animal.voice()

# получим пользу от животных
for animal in animals:
    print(animal.name)
    animal.give_benefit()