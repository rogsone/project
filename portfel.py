class zamalo(Exception):
    pass
class Portfel:
    def __init__(self, money = 00):
        self.money = money
    def add_money(self, amount):
        if amount <= 0:
            return
        self.money += amount

    def use_money(self, amount):
        if amount <= 0:
            return
        if amount > self.money:
            raise zamalo
        else:
            self.money -= amount

    def get_money(self):
        return self.money