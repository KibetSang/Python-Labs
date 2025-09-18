print("Welcome")
# Set the starting point for the bill
bill = 0
# Take input from the user
size= input("Size of piza e.g. S, M, L")
pepperoni = input("Do you need Pepperoni Y/N ?")
extra_cheese = input("Do you need extra cheese Y/N ?")
# Check the size of pizaa using if
if size == "S":
    bill = 15
elif size == "M":
    bill = 20
else:
       bill = 25
# Check user selection on the pepperoni and  use nested if to check size
if pepperoni == "Y":
    if size == "S":
        bill +=2
    else:
        bill +=3
if extra_cheese == "Y":
        bill+= 1
        # Print results using the f string
print(f"Your bill is {bill}")