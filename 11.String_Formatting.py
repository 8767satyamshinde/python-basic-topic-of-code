#Use the format() method to insert numbers into strings:
age = 36
txt = "My name is John, and I am {}"
print(f"My name is John, and I am {age}")
print(txt.format(age))


quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))
print(f"I want {quantity} pieces of item {itemno} for {price} dollars.")