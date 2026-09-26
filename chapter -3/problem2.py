# Write a program to fill in a letter template given below with name and data.

letter = '''Dear <|Name|>,
            you are selected!
            <|Data|>'''


# answer
print(letter.replace("<|Name|>","Harry").replace("<|Data|", "24 September 2050"))

          

