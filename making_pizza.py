from random import randint

class Die():
    def __init__(self,times,side=6):
        self.times=times
        self.side=side

    def roll_die(self):
        while(self.times):
            x=randint(1,self.side)
            print("The number you roll is: "+ str(x))
            self.times-=1
        
shaizi=Die(10)
shaizi.roll_die()

        