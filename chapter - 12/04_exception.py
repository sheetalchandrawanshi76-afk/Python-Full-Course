try:
    a = int(input("Enteer a number:"))
    print(a)

except ValueError as v:
    print("Heyy")
    print(v)
except Exception as e:
 print(e)
print("Thank You")