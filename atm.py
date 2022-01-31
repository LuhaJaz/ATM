class ATM(object):
    def __init__(self, cardNumber, pinNumber):
        self.cardNumber= cardNumber
        self.pinNumber= pinNumber

    def withdrawel(self):
        print(" Cash Withdrawed")

    def balancenq(self):
        print("Cash Balanced")


cash=ATM("1948031984", "12498")
cash.withdrawel()