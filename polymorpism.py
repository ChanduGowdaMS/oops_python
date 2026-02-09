class Payment:
    def pay(self):
        return "payment done:"
class GooglePay(Payment):
    def pay(self, amount):
        return f"payment done using Google pay: {amount}"
class PhonePe(Payment):
    def pay(self, amount):
        return f"payment done using Phone pay: {amount}"
class CreditCard(Payment):
    def pay(self, amount):
        return f"payment done using Credit card: {amount}"

p1 = Payment()
p2 = GooglePay()
p3 = PhonePe()
p4 = CreditCard()

print(p1.pay())
print(p2.pay(100))
print(p3.pay(300))
print(p4.pay(400))
