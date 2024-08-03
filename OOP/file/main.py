# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)

# add text without deleting the contents
# a = append
# r = read
# w = write

# with open("my_file.txt", mode="a") as file:
#     file.write("\nNew text.")

# create new file
with open("new_file.txt", mode="w") as file:
    file.write("New text.")
