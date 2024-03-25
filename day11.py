#index operator - it gives access to a sequence of elements(This can apply for strings, integers or tuples)

name ="samuel Mwaura!"

if (name[0].islower()):
    name = name.capitalize()
first_name = name[:6].upper()
last_name = name[7:].lower()
last_character = name[-1]
print(last_character)

#function- block of code which is executed only when called
def hello(first_name,last_name,age):
    print("Hello "+first_name+" "+last_name)
    print("you are "+str(age)+" years old")
    print("Have a nice day!")

hello("Samuel","Mwaura",20)





    



