import random
class notrandom:
    def __init__(self):
        pass
    def weightedChoice(choices):
        one = [1, 60]
        two = [2, 20]
        three = [3, 10]
        choice = random.randint(1, 100)
        if choice <= 60:
            return one[0]
        elif choice <= 80:
            return two[0]
        else:
            return three[0]

            
    

    

        