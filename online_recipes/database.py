import sqlite3
from models import Recipe, RecipeCreate

class RecipeRepository:
    def __init__(self, db_name="recipe.db"):
        self.db_name = db_name
        self._initialize_table()

    def _get_connection(self):
        conn = sqlite3.connect(self.db_name)
        conn.row_factory = sqlite3.Row
        return conn

    def _initialize_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS recipe (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT NOT NULL,
            ingredients TEXT NOT NULL
        )
        """
        with self._get_connection() as conn:
            conn.execute(query)

    def create(self, recipe: RecipeCreate) -> int:
        query = "INSERT INTO recipe (name, description, ingredients) VALUES (?, ?, ?)"
        with self._get_connection() as conn:
            cursor = conn.execute(query, (recipe.name, recipe.description, recipe.ingredients))
            return cursor.lastrowid

    def get_all(self):
        query = "SELECT * FROM recipe"
        with self._get_connection() as conn:
            rows = conn.execute(query).fetchall()
            return [Recipe(**dict(row)) for row in rows]

    def get_by_id(self, recipe_id: int):
        query = "SELECT * FROM recipe WHERE id = ?"
        with self._get_connection() as conn:
            row = conn.execute(query, (recipe_id,)).fetchone()
            return Recipe(**dict(row)) if row else None

    def update(self, recipe_id: int, recipe: RecipeCreate) -> bool:
        query = "UPDATE recipe SET name = ?, description = ?, ingredients = ? WHERE id = ?"
        with self._get_connection() as conn:
            cursor = conn.execute(query, (recipe.name, recipe.description, recipe.ingredients, recipe_id))
            return cursor.rowcount > 0

    def delete(self, recipe_id: int) -> bool:
        query = "DELETE FROM recipe WHERE id = ?"
        with self._get_connection() as conn:
            cursor = conn.execute(query, (recipe_id,))
            return cursor.rowcount > 0