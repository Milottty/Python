import sqlite3
from models import Movie, MovieBase
from  typing import Any

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




def main():
    movie1=MovieBase(title='Odyssey', director='Uvejsi', genre='Fantasy', year_of_release=2026)
    print(create_movie(movie1))


if __name__=="__main__":
    main()
