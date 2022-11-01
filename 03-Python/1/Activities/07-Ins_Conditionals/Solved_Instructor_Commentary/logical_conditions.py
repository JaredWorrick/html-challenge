
x = 1
y = 2
z = 3 
a = "Hello"

## Since or statements are true if ANY of the statements are true, Python stops reading as soon as it sees a true statment in an 'or' chain

if x == 1 or int(a) == 2:
    # Even though the second conditional SHOULD trigger an error (a cannot be converted to an integer)
    # It never does, because the first is true and due to the properties of OR, the entire condition MUST be true. 
    print('Condition 1 triggered')
else:
    print('Condition 1 not triggered')

## Since AND statements are true if ANY of the statements are false, Python stops reading as soon as it sees a false statment in an 'AND' chain

if x == 2 and int(a) == 2:
    # Even though the second conditional SHOULD trigger an error (a cannot be converted to an integer)
    # It never does, because the first is FALSE and due to the properties of AND, the entire condition MUST be false. 
    print('Condition 2 triggered')
else:
    print('Condition 2 not triggered')

if x == 2 or int(a) == 2:
    # Since the first condition is now FALSE, the second condition is actually checked, finally triggering the error. 
    print('Condition 3 triggered')