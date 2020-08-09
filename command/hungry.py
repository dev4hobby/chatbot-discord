import random

class MealTime():
    def __init__(self):
        self.meal_count = 0
    
    def ask(self):
        if random.randint(0, 1) is 1:
            return '밥먹어.\n'
        else:
            return '굶어.\n'

    def please_feed_me(self):
        result = random.randint(0,4)
        msg = ''

        if result == 0:
            msg = '시켜먹어'
        elif result == 1:
            msg = '해먹어'
        elif result == 2:
            msg = '^^ㅗ'
        elif result == 3:
            msg = '시러'
        else:
            msg = '알겠어'

        if self.meal_count > 5:
            self.meal_count = 0
            return '작작해 ㅡ_ㅡㅗ'
        else:
            self.meal_count+=1
            return msg
