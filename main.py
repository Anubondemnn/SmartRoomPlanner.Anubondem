#Smart Room Planner 

print("Welcome to the Smart Room Planner")

room_length = float(input("Enter room length(ft): "))
room_width = float(input("Enter room width(ft): "))

room_area = room_length * room_width
used_space = 0 

while True:
    name = input("\nEnter furniture name (or 'done' to finish): ")

    if name.lower() == 'done':
        break

    length = float(input(f"Enter {name} length(ft): "))
    width = float(input(f"Enter {name} width(ft): "))

    area = length * width

    if used_space + area > room_area:
        print("Not enough space for this furniture.")
    else:       
        used_space += area
        print(f"{name} added. Area of the space is{area} sq ft")

remaining_space = room_area - used_space

print("\n===== SUMMARY =====")
print("Room Area:", room_area, "sq ft")
print("Used Space:", used_space, "sq ft")
print("Remaining Space:", remaining_space, "sq ft")