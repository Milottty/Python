from fastapi import FastAPI
import sqlite3
from models import Movie, MovieBase
from  typing import Any,List

from sdisdi.app import response

app=FastAPI()

def create_connection()-> Any:
    '''
    Create the connection between the server and the database
    :return: Connection varialble
    '''
    conn=sqlite3.connect('pyadvanced24.db')
    conn.row_factory=sqlite3.Row
    return conn


def create_table():
    connection=create_connection()
    cursor=connection.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS movies(
        ID integer PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        director TEXT NOT NULL,
        genre TEXT NOT NULL,
        year_of_release INTEGER NOT NULL          
        );
    ''')
    connection.commit()
    connection.close()

@app.post(path="/movies", response_model=Movie)
def create_movie(movie:MovieBase):
    """
    Store a new movie in the database
    :param movie: A pydentic model of conntaining the tittle, director, genre and year of release of the movie to be created
    :return: int: The ID of the created movie stored in the database
    """
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO movies (title, director, genre, year_of_release) VALUES (?,?,?,? )",
                   (movie.title, movie.director, movie.genre, movie.year_of_release))
    connection.commit()
    movie_id=cursor.lastrowid
    connection.close()
    return movie_id



@app.get(path="/movies/",response_model=List[Movie])
def read_movies() ->    list[Movie]:
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM movies")
    rows=cursor.fetchall()
    connection.close()
    movies=[Movie(id=row[0], title=row[1], director=row[2], genre=row[3], year_of_release=row[4]) for row in rows]
    return movies



@app.get(path="/movie/{movie_id}",response_model=Movie)
def read_movie(movie_id:int)-> Any:
    """
    Retrieves a single movie from the database based in its ID.
    :param movie_id: The ID of the movie that want to retrieve.
    :return: A Movie Model representing the retrieved movie. Returns None, if no movies correspond to the ID.
    """
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM movies WHERE ID=?", (movie_id,))
    row=cursor.fetchone()
    connection.close()
    if row is None:
        return None
    else:
         return Movie(id=row['ID'], title=row['title'],
                     director=row['director'], genre=row['genre'],
                     year_of_release=row['year_of_release'])



@app.put(path='/movies/{movie_id}' ,response_model=Movie)
def update_movie(movie_id:int, movie:Movie)-> str:
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("UPDATE movies set title=?, director=?, genre=?, year_of_release=? WHERE ID=?",
                   (movie.title, movie.director, movie.genre, movie.year_of_release, movie_id))
    connection.commit()
    updated=cursor.rowcount
    connection.close()
    if updated==1:
        return f'One record updated with ID {movie_id}'
    return 'No record affected.'

@app.delete('/movies/{movie_id}', response_model=str)
def delete_movie(movie_id:int):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM movies WHERE ID=?", (movie_id,))
    connection.commit()
    deleted=cursor.rowcount
    connection.close()
    if deleted==1:
        return f'One record deleted with ID {movie_id}'
    return 'No record affected.'


def main():
    # movie1=MovieBase(title='test1', director='xzv', genre='Fantasy', year_of_release=2022)
    movies=read_movies()
    for movie in movies:
        print(f" {movie.id}.{movie.title} - {movie.year_of_release} directed by {movie.director} in the genre of {movie.genre}")
    print(read_movie(movie_id=3))


if __name__=="__main__":
    main()
