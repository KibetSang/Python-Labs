# What's going on?
# This question combines several of the Python List
# I recommend breaking down what’s going on using several print statements using repl.
# print(dirty_dozen)
# Then print out:
#
# print(dirty_dozen[0])
# print(dirty_dozen[1])
# To see what happens at the next stage print out:
#
# print(dirty_dozen[1][2])
# print(dirty_dozen[1][3])
# I hope this helps clarify how nested lists work.


fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
dirty_dozen = [fruits, vegetables]

print(dirty_dozen[1][1])