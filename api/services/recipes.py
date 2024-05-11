import os
import requests

from fastapi import Request, HTTPException

api_url = 'https://api.spoonacular.com/recipes/'

def recipes_by_ingredients(ingredients):
    api_key = "?apiKey=" + os.environ['SPOONACULAR_API_KEY']

    url = api_url + "findByIngredients" + api_key

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

def get_recipe_details(request):
    recipe_id = request.get('recipe_id')

    api_key = "?apiKey=" + os.environ['SPOONACULAR_API_KEY']

    url = api_url + str(recipe_id) + "/analyzedInstructions" + api_key 

    step_breakdown = True

    params = {"stepBreakdown": step_breakdown}

    try:
        response = requests.get(url, params=params).json()
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error: could not get recipe information at this time.")

    if isinstance(response, list):
        if not len(response):
            raise HTTPException(status_code=404, detail="Error: details not found for recipe.")

    return {"message": "Recipe details successfully retrieved", "results":response}