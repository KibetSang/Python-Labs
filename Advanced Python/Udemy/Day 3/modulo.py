age = int(input("Enter your age: "))
if age >= 18:
    height = int(input("Enter your height: "))
    if height >= 100:
        print("Pay 200")
    elif height >= 80:
        print("Pay 150")
    elif height >= 60:
        print("Pay 100")
    else:
        print("Pay nothing")
else:
    print(f"Not enough age")
