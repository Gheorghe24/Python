"""
	Bonus task: load all the available coffee recipes from the folder 'recipes/'
	File format:
		first line: coffee name
		next lines: resource=percentage

	info and examples for handling files:
		http://cs.curs.pub.ro/wiki/asc/asc:lab1:index#operatii_cu_fisiere
		https://docs.python.org/3/library/io.html
		https://docs.python.org/3/library/os.path.html
"""
import os
RECIPES_FOLDER = "SC/lab1/recipes"

def load_recipe(filename):
    
    resources = {}
    with open(filename) as recipe_file:
        coffee_type = recipe_file.readline().strip()
        for line in recipe_file.readlines():
            line_parts = line.split("=")
            if len(line_parts) != 2:
                print("Incorrect file format, resources should be listed as: resource=percent")
            resources[line_parts[0]] = int(line_parts[1])
    return coffee_type, resources

def load_all_recipes():
	
	if not os.path.exists(RECIPES_FOLDER) or not os.path.isdir(RECIPES_FOLDER):
		print("No recipes folder")
		return None

	recipes = {}
	for recipe_file in os.listdir(RECIPES_FOLDER):
		(recipe_name, resources) = load_recipe(os.path.join(RECIPES_FOLDER, recipe_file))
		recipes[recipe_name] = resources
	
	return recipes

# print(type(load_all_recipes()))