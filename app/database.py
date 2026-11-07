import sqlite3
from models.category import  CategoryBase
from routers.recipes import RecipeBase
from typing import Any



def create_connection()-> Any:
    '''
    Create the connection between the server and the database
    :return: Connection varialble

    '''
    conn=sqlite3.connect('db_app.db')
    conn.row_factory=sqlite3.Row
    return conn


def create_table():
    connection=create_connection()
    cursor=connection.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS (
            Id integer PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL      
        );
    ''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS recipes(
            Id integer PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT,
            ingredients TEXT NOT NULL,
            instructions TEXT NOT NULL,
            cuisine TEXT NOT NULL,
            difficulty TEXT NOT NULL,
            category_id INTEGER,
            FOREIGN KEY (category_id) REFERENCES categories (Id)
        );
    ''')
    connection.commit()
    connection.close()

def create_category(category:CategoryBase):
    """
    Store a new category in the database
    :param category: A pydentic model of conntaining the name of the category to be created
    :return: int: The ID of the created category stored in the database
    """
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO categories (name) VALUES (?)",
                   (category.name,))
    connection.commit()
    category_id=cursor.lastrowid
    connection.close()
    return category_id
def get_categories():
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute(
        "SELECT * FROM categories")

    categories = [dict(row) for row in cursor.fetchall()]
    connection.close()
    return categories

def get_category(category_id: int):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute(
        "SELECT * FROM categories WHERE Id=?", (category_id,))
    category = cursor.fetchone()
    connection.close()

    return (dict(category) if category else None)

def update_category(category_id: int, category: CategoryBase):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute(
        "UPDATE categories SET name=? WHERE Id=?", (category.name, category_id))
    connection.commit()
    connection.close()

    return update()

def delete_category(category_id: int):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute(
        "DELETE FROM categories WHERE Id=?", (category_id,))
    connection.commit()
    connection.close()

    return delete()

def create_recipe(recipe: RecipeBase):
    """
    Store a new recipe in the database
    :param recipe: A pydentic model of conntaining the name, description, ingredients, instructions, cuisine, difficulty and category_id of the recipe to be created
    :return: int: The ID of the created recipe stored in the database
    """
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO recipes (name, description, ingredients, instructions, cuisine, difficulty, category_id) VALUES (?,?,?,?,?,?,?)",
                   (recipe.name, recipe.description, recipe.ingredients, recipe.instructions, recipe.cuisine, recipe.difficulty, recipe.category_id))
    connection.commit()
    recipe_id=cursor.lastrowid
    connection.close()
    return recipe_id

def get_recipes():
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute(
        "SELECT * FROM recipes")
    recipes = [dict(row) for row in cursor.fetchall()]
    connection.close()
    return recipes

def get_recipe(recipe_id: int):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute(
        "SELECT * FROM recipes WHERE Id=?", (recipe_id,))
    recipe = cursor.fetchone()
    connection.close()

    return (dict(recipe) if recipe else None)

def update_recipe(recipe_id: int, recipe: RecipeBase):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute(
        "UPDATE recipes SET name=?, description=?, ingredients=?, instructions=?, cuisine=?, difficulty=?, category_id=? WHERE Id=?",
        (recipe.name, recipe.description, recipe.ingredients, recipe.instructions, recipe.cuisine, recipe.difficulty, recipe.category_id, recipe_id))
    connection.commit()
    connection.close()

    return update()

def delete_recipe(recipe_id: int):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute(
        "DELETE FROM recipes WHERE Id=?", (recipe_id,))
    connection.commit()
    connection.close()

    return delete()