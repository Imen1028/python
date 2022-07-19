def get_number():
    try:
        n = int(input("Size: "))
        return n
    except ValueError:
        print("Please Enter an integer")
        get_number()

n = get_number()

for i in range(n):
    for j in range(n):
        print('#', end='')
    print()