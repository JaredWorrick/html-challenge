
x = 5
if 2 * x > 10:
    print("Question 1 works!") # This is the output. 1 condition - 2 outcomes, simple if-else
else:
    print("oooo needs some work")

# 2. Question 2 works!
x = 5
# len() is what we use to find the length of things that are list-like ("iterable" is the official term)
# in that you can go through them one-by-one

# In this case, len() does what it sounds like - finds the length (how many characters) are in a string
if len("Dog") < x:
    print("Question 2 works!") # Output. 3<5
else:
    print("Still missing out")

# 3. GOT QUESTION 3!
x = 2
y = 5
# a**b is python syntax for a-to-the-power-b.
if (x ** 3 >= y) and (y ** 2 < 26):
    print("GOT QUESTION 3!")
else:
    print("Oh good you can count")

# 4. Dan is in group three
name = "Dan"
## This is a LIST - it is pythons version of a VBA array 
## Key difference - python lists can have multiple types
group_one = ["Greg", "Tony", "Susan"]           
group_two = ["Gerald", "Paul", "Ryder"] # TODO: What happens if you add "Dan" here as well?
group_three = ["Carla", "Dan", "Jefferson"]

# <obj> in <list> - very intuitive if the object exists in the list-like object
if name in group_one:
    print(name + " is in the first group")
elif name in group_two:
    print(name + " is in group two")
elif name in group_three:
    print(name + " is in group three")
else:
    print(name + " does not have a group")

# 5. Can ride bumper cars
height = 66
age = 16
adult_permission = True

if (height > 70) and (age >= 18):
    print("Can ride all the roller coasters")
elif (height > 65) and (age >= 18):
    print("Can ride moderate roller coasters")
elif (height > 60) and (age >= 18):
    print("Can ride light roller coasters")
elif ((height > 50) and (age >= 18)) or ((adult_permission) and (height > 50)):
    ## Notice if we have a boolean type we don't have to explicitly say 
    ## if adult_permission == True
    ## This is due to python assuming everything that happens in a condition
    ## is a boolean type (and converts it to such if it isnt)
    print("Can ride bumper cars")
else:
    print("Stick to lazy river")
