from flask import Flask, request, render_template
import requests

app = Flask(__name__)

# Base URL for TheMealDB API
BASE_URL = 'https://www.themealdb.com/api/json/v1/1'
RANDOM_RECIPE_URL = f'{BASE_URL}/random.php'  # Update to the actual endpoint

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query', '')  # Use request.args for GET request
    page = int(request.args.get('page', 1))  # Default to page 1 if not provided
    
    if page < 1:
        page = 1  # Ensure page is at least 1
    
    start = (page - 1) * 10  # Pagination start index
    response = requests.get(f'{BASE_URL}/search.php?s={query}')
    data = response.json()
    
    # Initialize meals to an empty list if 'meals' is None
    meals = data.get('meals', [])
    if meals is None:
        meals = []

    # Handle pagination
    total_meals = len(meals)
    num_pages = (total_meals + 9) // 10  # Number of pages

    # Slice meals for the current page
    meals = meals[start:start + 10]

    return render_template('index.html', meals=meals, query=query, page=page, num_pages=num_pages)

@app.route('/random', methods=['GET'])
def random_recipe():
    try:
        response = requests.get(RANDOM_RECIPE_URL)
        response.raise_for_status()  # Check for HTTP errors
        
        # Print response content for debugging
        print("Response Content:", response.text)
        
        # Attempt to parse JSON
        try:
            data = response.json()
            meal = data.get('meals', [])[0] if data.get('meals') else None
        except requests.exceptions.JSONDecodeError:
            # If JSON parsing fails, handle the error
            print("Error: The response is not valid JSON.")
            meal = None
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        meal = None
    
    return render_template('random.html', meal=meal)

@app.route('/categories')
def categories():
    response = requests.get(f'{BASE_URL}/categories.php')
    data = response.json()
    categories = data.get('categories', [])
    return render_template('categories.html', categories=categories)

@app.route('/search/category/<string:category>', methods=['GET'])
def search_by_category(category):
    print(f"Category requested: {category}")  # Debug print
    response = requests.get(f'{BASE_URL}/filter.php?c={category}')
    data = response.json()
    print(f"API response: {data}")  # Debug print
    meals = data.get('meals', [])
    
    return render_template('category.html', category=category, meals=meals)


@app.route('/meal/<string:meal_id>', methods=['GET'])
def meal_details(meal_id):
    response = requests.get(f'{BASE_URL}/lookup.php?i={meal_id}')
    data = response.json()
    meal = data.get('meals', [])[0] if data.get('meals') else None
    return render_template('meal.html', meal=meal)


if __name__ == '__main__':
    app.run(debug=True)
