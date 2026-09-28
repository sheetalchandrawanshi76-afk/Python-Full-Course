#Item Method
marks = {
    "sheetal": 97,
    "shipra":95,
    "shivani":99,
}
print(marks.items()) # naam ke sath no. bhi print hote hai.


# Keys Method
marks = {
    "sheetal": 97,
    "shipra":95,
    "shivani":99,
}
print(marks.keys()) # sirf naam show honge ess method se. 


# Values Method
marks = {
    "sheetal": 97,
    "shipra":95,
    "shivani":99,
}
print(marks.values()) # sirf value show hongi. 


# Update Method 
marks = {
    "sheetal": 97,
    "shipra":95,
    "shivani":99,
}
marks.update({"sheetal": 99}) # update ho jynge no. ye method lagne se. 
print(marks)


# Get Method 
marks = {
    "sheetal": 97,
    "shipra":95,
    "shivani":99,
}
print(marks.get("sheetal")) # agar list ke ander ka he naam dnge toh jo no. hai vohi btyega. 
print(marks.get("tamanna")) # toh ye none dena agar list main vo naam phle se nhi hai toh.