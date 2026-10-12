
# Vacuum Cleaning Problem in AI

rooms = {
    'A': 'Dirty',
    'B': 'Dirty'
}

location = 'A'

while True:
    print("\nCurrent Location:", location)
    print("Room Status:", rooms)

    if rooms[location] == 'Dirty':
        print("Room", location, "is dirty. Cleaning...")
        rooms[location] = 'Clean'
    else:
        print("Room", location, "is already clean.")

    if location == 'A':
        location = 'B'
    elif location == 'B':
        print("\nAll rooms cleaned!")
        break
