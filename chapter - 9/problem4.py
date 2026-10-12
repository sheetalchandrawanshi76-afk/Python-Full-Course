# A file contains a word "Donkey" multiple times. You need to write a program which replace this word with #### by updating the same file. 

word = "Donkey"

with open("file.txt4", "r") as f:
    content = f.read()

contentNew = content.replace(word , "######")

with open("file.txt4" ,"w") as f:
        f.write(contentNew)