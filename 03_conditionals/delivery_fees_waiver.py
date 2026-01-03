order_amount = int(input("Enter order amount: "))

print(f"Order amount: {type(order_amount)}")
delivery_fee = 0 if order_amount >= 300 else 30