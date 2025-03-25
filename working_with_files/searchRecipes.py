food = input('What recipe would you like to find?\n')

found = False

file = open('recipes.txt', 'r')
result = file.readlines()

for line in result:
    if food in line:
        print(line)
        found = True
        file.close()
if not found:
    print('We dont have that recipe')
    addRecipe = input('Would you like to add a new one? (y/n)\n')
    if addRecipe.lower() == 'y':
        with open('recipes.txt', 'a') as file:
            name = input('What is the item called?:\n')
            recipe = input('What is the recipe?\n')
            file.write('\n' + name + '-' + recipe)
    elif addRecipe.lower() == 'n':
        print('Have a nice day!')