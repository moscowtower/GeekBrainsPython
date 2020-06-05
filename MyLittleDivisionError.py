class MyLittleDivisionError(ZeroDivisionError):
    def __init__(self, dividend, devisor, message='Делить на ноль можно только если ты инженер'):
        self.dividend = dividend
        self.devisor = devisor
        self.message = message
        super().__init__(self.message)
        if self.devisor == 0:
            print(self.message)


mlde = MyLittleDivisionError(5, 0)
non_mlde = MyLittleDivisionError(5, 1)