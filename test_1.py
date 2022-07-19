def pp():
    try:
        size = int(input("Size: "))

    except ValueError:
        print("Please Enter An integer!")        
        pp()

    print(f"Your pp size is {size}cm, Your pp small and stinks!")
    exit(0)

size = 0

try:
    size = int(input("Size: "))

except ValueError:
    print("Please Enter An integer!")        
    pp()

print(f"Your pp size is {size}cm, Your pp small and stinks!")
exit(0)