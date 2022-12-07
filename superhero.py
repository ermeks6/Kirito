class SuperHero:
    people = 'people'

    #(2)
    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.health_points  = health_points
        self.nickname = nickname
        self.superpower = superpower
        self.catchphrase = catchphrase


    def n(self):
        print(f'Wanted: {self.name}')


    def h(self):
        self.health_points *= 2


    def __str__(self):
        return f'Nickname: {self.nickname}' \
               f'Power: {self.superpower}' \
               f'Health: {self.health_points}'


    def __len__(self):
        return len(self.catchphrase)


hero = SuperHero('Kirigaya', 'Kirito\n', 'fencing\n', 14000, 'Я скорее погибну вместе с другим человеком, чем буду просто стоять и смотреть, как он погибает один')
hero.n()
hero.h()
print(hero)
print(f'Catchphrase: {len(hero.catchphrase)}')