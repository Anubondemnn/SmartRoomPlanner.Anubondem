#Smart Room Planner 
furniture_list = []
print("Welcome to the Smart Room Planner")

room_length = float(input("Enter room length(ft): "))
room_width = float(input("Enter room width(ft): "))

room_area = room_length * room_width
used_space = 0

while True:
    name = input("Enter furniture name (or 'done' to finish): ")

    if name.lower() == 'done':
        break

    length = float(input(f"Enter {name} length(ft): "))
    width = float(input(f"Enter {name} width(ft): "))

    area = length * width

    if used_space + area > room_area:
        print("Not enough space for this furniture.")
    else:       
        furniture = {
    "name": name,
    "area": area
}
furniture_list.append(furniture)

used_space += area
print(f"{name} added. Area of the space is {area} sq ft")

remaining_space = room_area - used_space

print("\nFurniture List:")
for item in furniture_list:
    print(f"- {item['name']} ({item['area']} sq ft)")
print("\n===== SUMMARY =====")
print("Room Area:", room_area, "sq ft")
print("Used Space:", used_space, "sq ft")
print("Remaining Space:", remaining_space, "sq ft")

""""
new code """

percent_used = (used_space / room_area) * 100

print(f"Room is {percent_used:.2f}% full")

if percent_used >= 90:
    print("Warning: Room is almost full!")
elif percent_used >= 70:
    print("Room is getting crowded.")
else:
    print("Room has plenty of space.")
print(f"#{item['name']} has {item['area']} sq ft")

#new code
grid_width = int(room_width)
grid_length = int(room_length)

room_grid = []

for i in range(grid_length):
    row = ["[]"]* grid_width
    room_grid.append(row)

area = length * width
x = int(input("Enter X position (number, e.g., 0–10): "))
y = int(input("Enter Y position (number, e.g., 0–10): "))

size_x = int(input("Enter furniture width in grid units (e.g., 2): "))
size_y = int(input("Enter furniture height in grid units (e.g., 2): "))

furniture = {
    "name": name,
    "area": area,
    "x": x,
    "y": y,
    "size_x": size_x,
    "size_y": size_y
}

furniture_list.append(furniture)
can_place = True

for i in range(size_y):
    for j in range(size_x):
        if not (0 <= y+i < grid_length and 0 <= x+j < grid_width):
            can_place = False
        elif room_grid[y+i][x+j] != "[ ]":
            can_place = False

if can_place:
    for i in range(size_y):
        for j in range(size_x):
            room_grid[y+i][x+j] = f"[{name[0].upper()}]"

    furniture_list.append(furniture)
else:
    print("Cannot place furniture here (out of bounds or overlapping).")

# X-axis
print("   ", end="")
for col in range(grid_width):
    print(f"{col:3}", end="")
print()
print("Try a different position inside the grid.")
# Grid with Y-axis
for i, row in enumerate(room_grid):
    print(f"{i:2} ", end="")
    for cell in row:
        print(cell, end="")
print()
