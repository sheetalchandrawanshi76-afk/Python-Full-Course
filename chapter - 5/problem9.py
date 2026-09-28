# Can you change the values inside a list which is contained in set S ?
s = {8 , 7 , 12, "Sheetal", [1,2]}


# Answer 
s = {8 , 7 , 12, "Sheetal", [1,2]} #  TypeError : unhashable type : 'list' .

s [4][0] = 9