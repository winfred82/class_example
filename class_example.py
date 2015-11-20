class Musician(object):
    def __init__(self, sounds):
        self.sounds = sounds

    def solo(self, length):
        for i in range(length):
            print(self.sounds[i % len(self.sounds)])
        

class Bassist(Musician): # The Musician class is the parent of the Bassist class
    def __init__(self):
        # Call the __init__ method of the parent class
        super(Bassist,self).__init__(["Twang", "Thrumb", "Bling"])

class Guitarist(Musician):
    def __init__(self):
        # Call the __init__ method of the parent class
        super(Guitarist,self).__init__(["Boink", "Bow", "Boom"])

    def tune(self):
        print("Be with you in a moment")
        print("Twoning, sproing, splang")


class Drummer(Musician):
    """docstring for Drummer"""
    def __init__(self):
        super(Drummer, self).__init__(["Boink", "Bow", "Boom"])
        

class Band(Musician):
    """docstring for Band"""
    def __init__(self):
        super(Band, self).__init__()

    def hire_musican():
        pass
    def fire_musican():
        pass

    def play():
        drummer=Drummer()
        drummer.solo(4)
        
        

if __name__ == '__main__':
    drummer=Drummer()
    drummer.solo(4)
    print drummer.sounds