# blueprint-2018


# Genome Link API
Client ID: p0LRC0Mi57EUEGfc2NZvKAeXBVeanFniIyxNYRFC
Client Secret: VtLr55D1aU2Z5JLUMePKvIKJnv2LeWfytTakDvrvc7V7lweVABesM4hEjBqdnrQHwHuzby00LgcnCEHDeayOPqNc8mvJ2AHRBmvrgtPQu7YRcHBt5n8DOqH7tDXF0Cap
Redirect uris (could be wrong): http://127.0.0.1:5000/callback


# API for Pulling Recipes Based on Ingredient List

### https://market.mashape.com/spoonacular/recipe-food-nutrition#classify-cuisine


# API for Genetic Info:

### https://genomelink.io/developers/?_ga=2.149081462.116353461.1518959527-31592564.1516897393

###  Guy’s genome for testing:
### https://github.com/lecoq/genome
### GPL-2 license so it’s fine to use



# Functionality:

### Format of Key
## Name of Trait
Name to Pull from API
List of Presence in Ingredients
Ingredient 1
Ingredient 2
Ingredient 3
Ingredient 4
Ingredient 5


Alpha-linolenic acid
Alpha-linolenic-acid


## Calcium
###
Milk
Kale
Sardines
Yogurt
Broccoli
Cheese
Carbohydrate intake
Iron
Iron
Bean and lentils
Tofu
Baked potatoes
Cashews
Spinach
Nuts
Turkey
###


## Phosphorus
###
Phosphorus
Tuna
Brown rice
Turkey
Beef
Potatoes
Broccoli
Egg



## Vitamin D
###
Vitamin-d
Salmon
Tuna
Eggs
Mushrooms
Cheese
Cod liver oil
Vitamin E
Vitamin-e
Almonds
Spinach
Avocado
Trout
Sweet potato

## What To Do After Pulling Genetic Information from the given traits
If they have low serum levels (0 or 1), then suggest that food type
If they have intermediate serum level (2), then ignore
If they have higher serum level (3 or 4), then bring up recipes that don’t have that food


## Functionality Goals
### Be able to search in the Ingredient List via Genetic Info
### Pull all this information back and show the suggested 5 recipes based on this
### Create a web platform where users can input their information





