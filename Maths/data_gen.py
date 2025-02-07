import random
import os

# Generate random data with no duplicated lines
data = set()
num_points = 100
while len(data) < num_points:
    x = random.randint(1, 15)
    y = random.randint(1, 15)
    data.add((x, y))

data = list(data)

# Generate a unique file name
base_filename = "data"
filename = base_filename
file_count = 1
while os.path.exists(filename + ".txt"):
    filename = base_filename + str(file_count)
    file_count += 1

# Write data to the file
with open(filename + ".txt", "w") as file:
    file.write(str(num_points) + "\n")
    for point in data:
        file.write(" ".join(str(coord) for coord in point) + "\n")

print("File '{}' generated.".format(filename + ".txt"))
