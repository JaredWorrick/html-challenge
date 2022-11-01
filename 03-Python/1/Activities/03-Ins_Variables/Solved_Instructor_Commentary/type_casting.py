
title = "Frankfurter"
years = 80
expert_status = True


## Python is a dynamically typed language , variables will often appear with no type declaration. 
## As such to find the type of something while debugging we can often use the type() function

print("The type of {} is {}".format("title",type(title)))
print("The type of {} is {}".format("years",type(years)))
print("The type of {} is {}".format("expert_status",type(expert_status)))


## Typing can cause errors, and being able to interpret them is essential to debugging
## Uncomment this next line of code - you should get an error, what does the error message tell you? 

## x = "3" + True

