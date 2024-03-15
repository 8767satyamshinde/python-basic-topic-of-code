#You can use double or single quotes:
print("1.Hello")
print('2.Hello')


print("3.")
var = "satyam"
var1 = "22"
print(var1)
print(type(var1))
print(var + "  " + var1 )


print("4. how to use format")
print('your name is ',var)
#print("your name is {}  And your age is {}".format(var,var1))
print(f"your name is {var}  And your age is {var1}")  # format string


print("5. position of give data of :")
a = "Hello, World!"
print(a[1])  #Get the character at position 1 (remember that the first character has the position 0):


print("6. loop in banana like this below :")
for x in "banana":
  print(x)



#Check String
print("8. Check String")
txt = "The best things in life are free!"
print("free" in txt)


#Check if not  String
print("9. Check if not String")
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")



print("13.    The strip() method removes any whitespace from the beginning or the end:")
a = "      Hello, World!   "
print(a.strip()) # returns "Hello, World!"


print("14. The split() method splits the string into substrings if it finds instances of the separator:")
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']


#15. String Concatenation
a = "Hello"
b = "World"
c = a + b
print("15. Concatenation concept :",c)


#16. To add a space between them, add a " ":
b = "World"
c = a + "  " + b
print("16. To add a space between them, add a " ": ",c)
