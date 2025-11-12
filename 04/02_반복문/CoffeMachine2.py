class CoffeeMachine2:
    def __init__(self, price=300):
        self.total = 0
        self.price = price

    def insert_money(self, amount):
        self.total += amount
        print(f"{amount}원을 넣으셨습니다. (총 {self.total}원)")

    def dispense(self):
        if self.total > self.price:
            change = self.total - self.price
            print(f"커피 나왔습니다 ☕️ 거스름돈은 {change}원입니다.")
        elif self.total == self.price:
            print("커피 나왔습니다 ☕️ 거스름돈은 없습니다.")
        else:
            print(f"금액이 부족합니다. {self.price - self.total}원이 더 필요합니다.")
        self.total = 0
