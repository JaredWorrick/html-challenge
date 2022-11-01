## A dangerous, but common (and somewhat accepted) practice in python that you will see are "lazy" conditionals
## Aka conditionals that use/abuse pythons default boolean conversion for conditionals 

integer_object = 123

if integer_object: 
    # TODO: What am I really trying to say here? What is the actual condition?
    # TODO: Look back to Activity 05's Commentary, in particular the sidebar
    print('Integer condition met')

string_object = 'Hello'

if string_object:
    # TODO: What am I really trying to do here
    print('String condition met')

list_object = []

if list_object:
    # TODO: What am I really trying to do here
    print('List condition met')


## This auto-bool conversion is lazy, and can be dangerous when you are not sure what type
## your output will be (note the 0 vs '0' distinction from Activity 05)