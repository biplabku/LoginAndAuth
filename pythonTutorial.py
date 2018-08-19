## Python tutorials

name = "am learning"
print(name.title())

# Calling python method title on the variable to make it title
# how to remove extra space from the variable

favorite_language = ' python '
print(favorite_language)
favorite_language = favorite_language.rstrip();
print(favorite_language)
print "favorite_language"


age = 27
print ("my age is " + str(age) + ".")

## List learning tutorials

names = ['Biplab', 'Binita', "hello"]
print(names)

biplab = []
biplab = names

print(biplab)

## tutorial for 
### Tuple

# its just like a list but instead of using square brackets we will use paranthesis
dimensions  = (100,20)
print(dimensions)
print(dimensions[0])

# tuple values cant be changed by assinging
# python tells use we cant assign  a new value to an item in a tuple

# overriding a tuple is allowed

# example dictionary 
alien = {'color':'green', 'points':5}
print(alien['points'])

# how to loop over the dicitionary
for key, value in alien.items():
	print(key)
	#print(value)



def describe_pet(pet_name, type_an='dog'):
	print("\nI have a " + type_an + ".")
	print("My " + type_an + "'s name is " + pet_name.title() + ".")

describe_pet(pet_name='willie')