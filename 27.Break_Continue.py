#Pass
fruits = ["cherry","apple","apple", "banana", "cherry", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)

###########################3
print("\n")
# continue
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

  ##########################3
print("\n")
  ######################3
for x in range(6):
  if x == 3:
    break
  print(x)

  ##########################3
print("\n")
  ######################3
for x in range(6):
  if x == 3:
    continue
  print(x)