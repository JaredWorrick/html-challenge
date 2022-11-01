
# name is a string so pretty standard input statement
name = input("What is your name? ")


## Try to put in a non integer value for the input here when you run it. What error do you get? 
age = int(input("How old are you? "))

# Note that non-zero,non-empty objects are truth-y.
trueOrFalse = bool(input("Is the input truthy? "))

## Sidebar: 
print("\n"*8 + "Sidebar------------------") 
## The note (non-zero, non-empty objects are truthy) is super important in python. 
## Play around with the following inputs and 'bool' conversions. Are there any that surprise you?
b1 = ""
b2 = "False"
b3 = "0"
b4 = 0
b5 = 1
b6 = "Hello, my name is Raghu"

print('When I convert b1 to boolean I get {}'.format(bool(b1)))
print('When I convert b2 to boolean I get {}'.format(bool(b2)))
print('When I convert b3 to boolean I get {}'.format(bool(b3)))
print('When I convert b4 to boolean I get {}'.format(bool(b4)))
print('When I convert b5 to boolean I get {}'.format(bool(b5)))
print('When I convert b6 to boolean I get {}'.format(bool(b6)))
print('----------------- End Sidebar')
print('Returning to the exercise')

# Creates three print statements that to respond with the output.
print("My name is {}".format(name))
print("I will be {} next year.".format(age+1))
print("The input was converted to {}".format(trueOrFalse))
