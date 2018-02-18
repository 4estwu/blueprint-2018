

condition_to_number = {
"Lower serum level" : 0 ,
"Slightly serum level" : 1 ,
"Intermediate" : 2 ,
"Slightly higher serum level" : 3 ,
"Higher serum level" : 4 ,
}

calcium_level = condition_to_number{input}
iron_level = condition_to_number{input}
phosphorus_level = condition_to_number{input}


ingredient_search = []

if calcium_level < 2 :
    ingredient_search += ["milk", "kale", "yogurt", "sardines", "broccoli", "cheese"]
else:
    ingredient_search -= ["milk", "kale", "yogurt", "sardines", "broccoli", "cheese"]

if iron_level < 2 :
    ingredient_search += ["beans", "tofu", "potato"]
else:
    ingredient_search -= ["beans", "tofu", "potato"]

if phosphorus_level < 2 :
    ingredient_search += ["tuna", "brown rice", "turkey"]
else:
    ingredient_search -= ["tuna", "brown rice", "turkey"]

if 
print(ingredient_search)



