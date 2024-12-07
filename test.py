from random import shuffle

class test:
    def __init__(self, name, power = 0, toughness = 0):
        self.name = name
        self.power = power
        self.toughness = toughness
    
    def __str__(self):
        return f'{self.name}, {self.power}, {self.toughness}'

    def sayHi(self):
        print(f'My name is {self.name}')

library = (
    ["wow"] * 1 + 
    ["beee"] * 2 +
    ["wahooo"] * 3
)

array = [test("Forest", power = 0, toughness=5), test("Mountain", toughness=3)]
print(array)

def find(player):
    # opponent = [other_player for other_player in array if other_player != player]
    for other_player in array:
        if other_player != player:
            other_player.sayHi()

find(array[1])

# array.remove(mountains[0])
# print(array)
# array.append(mountains[0])
# print(array)

# opponent = [other_player for other_player in self.players if other_player != player]
# opponent.remove_creature()