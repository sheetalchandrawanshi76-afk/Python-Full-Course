f = open("file.txt")
print(f.read())
f.close()
# The same can be written using with statement like this:
with open("file.txt") as f:
    print(f.read())

# you dont have to explicity[automatically] close the file.


# eski file [file.txt hai hai]