class Robot:
    def __init__(self, name, build):
        self.name = name
        self.build = build
        self.position = [0,0]

        print(f'My name is {self.name}, and my build is {self.build}.')
    def walk(self, x):
        self.position[0] = self.position[0] + x
        print('New Position:', self.position)


class RobotDog(Robot):
    def makeNoise(self):
        print('Woof Woof')


junie = RobotDog('Junie', '4ls')
junie.walk(7)
junie.makeNoise()