Recipe Finder is a Flask-based web application that allows users to search for recipes based on various criteria. 
The application interacts with TheMealDB API to fetch recipe data and provides features like:

Searching for recipes by name.
Viewing random recipes.
Browsing recipes by categories.
Detailed view of individual recipes.


Features
Search Recipes: Find recipes by entering keywords.
Random Recipe: Get a randomly selected recipe.
Recipe Categories: Browse recipes by category.
Recipe Details: View ingredients, instructions, and source of each recipe.


Technologies Used
Backend: Python, Flask
Frontend: HTML, CSS
API: TheMealDB


Getting Started
Prerequisites
Python 3.6 or higher
Flask


Requests library
Installation

Clone the Repository:


git clone https://github.com/SuhailAwez/recipe-finder.git
cd recipe-finder
Create a Virtual Environment (optional but recommended):


python -m venv venv
Activate the Virtual Environment:

On Windows:


venv\Scripts\activate
On macOS/Linux:


source venv/bin/activate
Install Dependencies:


pip install -r requirements.txt
Running the Application
Set Environment Variables (if needed):


export FLASK_APP=app.py
export FLASK_ENV=development


Run the Flask Application:
flask run


The application will be available at http://127.0.0.1:5000.

Usage
Home Page: Visit the home page to access the search, random recipe, and categories features.
Search Recipes: Enter keywords in the search bar and click "Search" to find recipes.
Random Recipe: Click "Random Recipe" to view a randomly selected recipe.
Categories: Browse recipes by selecting a category.


API Endpoints
GET /search: Search for recipes by name.
GET /random: Get a random recipe.
GET /categories: View all recipe categories.
GET /search/category/<category>: View recipes by category.
