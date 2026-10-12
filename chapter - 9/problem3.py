# Write a program to generate a multiplication table fron 2 to 20 and write it to the differents files. place this file in a folder for a 13 year old.

def generateTable(n):
    table =""
    for i in range(1,11):
        table += f"{n}x{i} = {n*i}\n"
        with open(f"tables/table_{n}" , "w") as f :
            f.write(table) 
    
for i in range(2,22):
    generateTable(i)


    # table folder m hai uska output.