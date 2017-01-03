class Introduce:
    def setname(self, name):
        self.name = name
    def intro(self):
        print('I am %s , who call me?'% self.name)
ace = Introduce()
ace.setname('Ace')
ace.intro()


class Ball:
    def __init__(self,name):
        self.name = name
    def kick(self):
        print('I am %s , who call me?'% self.name)
b = Ball('potato')
b.kick()
