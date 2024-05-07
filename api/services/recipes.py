import os
import requests

api_url = 'https://api.spoonacular.com/recipes/findByIngredients'

def recipes_by_ingredients(ingredients):
    api_key = "?apiKey=" + os.environ['SPOONACULAR_API_KEY']

    url = api_url + api_key

    num_results = ingredients.num_results
    ignore_pantry = False
    ranking = 1

    params = {"ingredients": ingredients.ingredients,
              "number": num_results,
              "ignorePantry": ignore_pantry,
              "ranking": ranking}

    try:
        response = requests.get(url, params=params).json()
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error: could not find recipe")

    if isinstance(response, list):
        if not len(response):
            raise HTTPException(status_code=404, detail="Error: no results found for search terms")
    return {"message": "Results found", "results":response}