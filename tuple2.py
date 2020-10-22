comedians = [('Eddie', 'Murphy'), ('Richard', 'Pryor'), ('Red', 'Fox')]
for first_name, last_name in comedians:
    print("first name:", first_name, "last name:", last_name)


fruits = ['apple', 'pear', 'apricot', 'cherry', 'peach']
for n in range(len(fruits)):
    print(n, fruits[n])

# now we are going to use enumerate function
# apparently this is more 'pythonic'
fruits = ['apple', 'pear', 'apricot', 'cherry', 'peach']
for item in enumerate(fruits):
    print(item[0], item[1])

# However, to do this the pythonic way is to put a tuple of variable names in
# the for loop as below:
fruits = ['apple', 'pear', 'apricot', 'cherry', 'peach']
for idx, fruit in enumerate(fruits):
    print(idx, fruit)

def add(x, y):
    return x + y

print(add(3, 4))
z = (5, 4)
print(add(*z)) # this line will cause the values to be unpacked
