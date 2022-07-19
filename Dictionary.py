import sys

people = {
    "Imen": "0923852968",
    "Levi": "0942352525"
}

name = str(input("Name: "))

if name in people:
    print(f"number: {people[name]}")
else:
    print("pp")