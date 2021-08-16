fruits = ['peach', 'kiwi', 'apple', 'blueberry', 'papaya', 'mango', 'pear']

new_order = sorted(fruits, key=lambda name: (-len(name), name))
for i in new_order:
    print(i)
