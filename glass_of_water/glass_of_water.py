class Glass:
    def __init__(self, capacity):
        self.capacity = capacity
        self.amount = 0

    def pour_in(self, amount:int) -> None:
        self.amount += (
            amount
            if self.amount + amount <= self.capacity
            else (self.capacity - self.amount)
        )

    def pour_out(self, amount:int) -> None:
        self.amount -= amount if amount <= self.amount else self.amount
