import os
# r = Read
# a = Append
# w = Write
# x = Create

# Read - error if it doesn't exist

f = open("names.txt")
# print(f.read())
# print(f.read(4))

# print (f.readline())
# print (f.readline())

for line in f:
    print(line)
    
f.close()

try:
    f = open("names.txt")
    print(f.read())
except:
    print("The file you want does not exist")
finally:
    f.close()
    
# Append - creates the file if it doesnt exist
f = open("names.txt", "a")
f.write("Neil\n")
f.close()

f = open("names.txt")
print(f.read())
f.close()

# Write (overwrite)
f = open("context.txt", "w")
f.write("I deleted all of the context")
f.close()

f = open("context.txt")
print(f.read())
f.close()

# Two ways to create a new file

# Opens a file for writing, creates the file if it doesn't exist
f = open("name_list.txt", "w")
f.close()

# Create the specified file, but returns an error if the file exists
if not os.path.exists("dave.txt"):
    f = open("dave.txt", "x")
    f.close()

# Delete a file

# avoid an error if it doesnt exist
if os.path.exists("dave.txt"):
    os.remove("dave.txt")
else:
    print("The file you wish to delete does not exist")
    
if os.path.exists("name_list.txt"):
    os.remove("name_list.txt")
else:
    print("The file you wish to delete does not exist")
    
with open("more_names.txt") as f:
    content = f.read()
    
    with open("names.txt", "w") as f:
        f.write(content)