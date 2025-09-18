global_scoped = 23

def add_two_numbers(a):
    global_scoped = 23
    return global_scoped
add_two_numbers(10)


print(global_scoped)