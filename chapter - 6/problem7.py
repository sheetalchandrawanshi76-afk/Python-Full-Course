# Write a program to find out whether a given post is talking about "sheetal" or not.

post = input("Enter the post:")

if("Sheetal.lower() in post.lower()"):
    print("This post is talking about sheetal")
  
else:
    print("This post is not talking about sheetal")