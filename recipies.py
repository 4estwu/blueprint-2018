import unirest

class recipies(object):
    '''
    takes ingredients and returns dishes
    '''
    def __init__(self, names, num):
        '''
        takes names (strings in list), and number of recipies to be returned
        '''
        "%2C".join(names)
        self.response = unirest.get("https://spoonacular-recipe-food-nutrition-v1.p.mashape.com/recipes/findByIngredients?fillIngredients=false&ingredients="+str(names)+"&limitLicense=false&number="+str(num)+"&ranking=1",
  headers={
    "X-Mashape-Key": "ASamou9Upcmshsg1bRJ1F0UnseK0p1ietqvjsnhjUe3llq5r2s",
    "Accept": "application/json"
  }
)
