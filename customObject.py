class Recipe():
    def __init__(self, dish, items, time) -> None: # Constructor method for the class Recipe 
    # The constructor method is called when an object is created from the class Recipe 
    # The constructor method is used to initialize the attributes of the class Recipe which means to assign values to the attributes of the class Recipe
    # In the the values are assigned to the attributes of the class Recipe like name, ingredients, and instructions 

        self.dish= dish
        self.items= items
        self.time= time
    
    def getRecipe(self):
        # print(f"Recipe for {self.dish} is {self.items} and takes {self.time} minutes to cook")
        print("The " + self.dish + " recipe is " + str(self.items) + " and takes " + str(self.time) + " minutes to cook")

pizza= Recipe("Pizza", ["cheese", "tomato", "onion", "pepper"], 30)
maggie= Recipe("Maggie", ["water", "maggie", "salt", "pepper"], 5)
sandwich= Recipe("Sandwich", ["bread", "cheese", "tomato", "onion", "pepper"], 10)

pizza.getRecipe() # Calling the method getRecipe() on the object pizza
maggie.getRecipe()
sandwich.getRecipe()

    








