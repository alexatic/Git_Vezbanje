class Hero:
    '''

A hero who is allergit to peanuts

    '''
    def __init__(self,name):
        self.name = name
        self.health = 100
    def eat(self,food):
        if(food == 'peanut'):
            self.health -=100
        elif (food == 'apple'):
            self.health +=20

Boban = Hero('Boban')
print (Boban.name)
print (Boban.health)
Boban.eat('apple')
print (Boban.health)
Boban.eat ('peanut')
print (Boban.health)
Boban.eat('apple')
print(Boban.health)
input()






