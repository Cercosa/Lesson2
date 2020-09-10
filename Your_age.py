your_age = input("How old are you?:"  )

 
def your_occupation(your_age):
    if 0 < your_age <= 5:
        return "go to kindergarten"
    elif 17 >= your_age > 5:
        return "go to school"
    elif 23 >= your_age > 17:
        return "go to university"
    elif 100 >= your_age > 23:
        return "go to work"
    else:
        return "this data is not correct, try again"  

if type(your_age) is int:
    result = your_occupation(your_age)
    print(result)
elif type(your_age) is not int: 
    print("this data is not correct, try again")   