age = int(input("How old are you? "))
bill = 0
if age >=18:
    if age >=18:
        bill = 12
    elif age >=30:
        bill =20
    else:
        bill = 70
    need_luxury = input("Do you need luxury? (Y/N): ")
    if need_luxury == "Y":
        bill += 100
        print(f"Your lux is {bill}")
    if need_luxury == "N":
        bill = bill
        print(f"Your lux is {bill}")
else:
    print("Not enough age")