# Write a program to mine a log file a find out whether it contains 'python'.

with open("log.txt") as f:
    content = f.read()

if("python" in content):
    print("yes python is present")

else:
    print("No python is not present")
