class Planet:
    def __init__(self, name, radius, age):
        self.name = name
        self.radius = radius
        self.age = age

    def __str__(self):
        return f'Name: {self.name}, Radius: {self.radius}m, Age: {self.age} years'


class Moon(Planet):
    def __init__(self, name, radius, age, moon_place):
        super().__init__(name, radius, age)
        self.moon_place = moon_place

    def __str__(self) :
        return f'{super().__str__()}\n {self.name} orbit place: {self.moon_place}'

class Sateline(Planet):
    def __init__(self, name, radius, age, sateline_company, sateline_channels):
        super().__init__(name, radius, age)
        self.sateline_company = sateline_company
        self.sateline_channels = sateline_channels

    def __str__(self):
        return f'{super().__str__()} \n {self.name}\'s company: {self.sateline_company}, Connected channels: {self.sateline_channels}'


#if __name__ == '__main__':
print('Initiate objects')
Earth = Planet('Earth', 911231, 2000000)
Moon = Moon('Moon`',33424, 3443232, 1)
Jeycob = Sateline('Jeycob', 13, 23, 'NASA', [1231, 3423])
print('Done')
print('print objects')
print(Earth)
print(Moon)
print(Jeycob)
