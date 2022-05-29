def get_number():
    a = input("Enter number ")
    if a.isdecimal():
        return int(a)
    return -1