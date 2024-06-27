import sqlite3


CREATE_ACTORS_TABLE = """ CREATE TABLE IF NOT EXISTS actors (
                        actor_id INTEGER NOT NULL PRIMARY KEY,
                        actor_name TEXT NOT NULL,
                        date_of_birth DATE NOT NULL,
                        gender TEXT NOT NULL
);"""

CREATE_DIRECTORS_TABLE = """ CREATE TABLE IF NOT EXISTS directors (
                        dir_id INTEGER NOT NULL PRIMARY KEY,
                        dir_name TEXT NOT NULL,
                        dir_date_of_birth DATE NOT NULL,
                        dir_gender TEXT NOT NULL
);"""

CREATE_GENRE_TABLE = """ CREATE TABLE IF NOT EXISTS genres (
                        genre_id INTEGER NOT NULL PRIMARY KEY,
                        genre_name TEXT NOT NULL
);"""

CREATE_MOVIE_TABLE = """ CREATE TABLE IF NOT EXISTS movies (
                        movie_id INTEGER NOT NULL PRIMARY KEY,
                        movie_name TEXT NOT NULL,
                        release_date DATE NOT NULL,
                        duration TIME NOT NULL,
                        dir_id INTEGER NOT NULL,
                        movie_rating TEXT NOT NULL,
                        review_rating INTEGER NOT NULL,
                        gross_income INTEGER NOT NULL,
                        CONSTRAINT FK_movies_directors FOREIGN KEY (dir_id) REFERENCES directors (dir_id)
);"""

CREATE_STUDIO_TABLE = """ CREATE TABLE IF NOT EXISTS studio (
                        studio_id INTEGER NOT NULL PRIMARY KEY,
                        studio_name TEXT NOT NULL
);"""

CREATE_MOVIECAST = """ CREATE TABLE IF NOT EXISTS moviecast (
                        movie_id INTEGER NOT NULL,
                        actor_id INTEGER NOT NULL,
                        actor_role TEXT NOT NULL,
                        CONSTRAINT FK_moviecast_movies FOREIGN KEY (movie_id) REFERENCES movies (movie_id),
	                    CONSTRAINT FK_movies_actors FOREIGN KEY (actor_id) REFERENCES actors (actor_id)
);"""

CREATE_MOVIEGENRE = """ CREATE TABLE IF NOT EXISTS moviegenre (
                        movie_id INTEGER NOT NULL,
                        genre_id INTEGER NOT NULL,
                        CONSTRAINT FK_moviegenre_movies FOREIGN KEY (movie_id) REFERENCES movies (movie_id),
	                    CONSTRAINT FK_movies_genre FOREIGN KEY (genre_id) REFERENCES genres (genre_id)
);"""

CREATE_MOVIESTUDIO = """ CREATE TABLE IF NOT EXISTS moviestudio (
                        movie_id INTEGER NOT NULL,
                        studio_id INTEGER NOT NULL,
                        CONSTRAINT FK_moviestudio_movies FOREIGN KEY (movie_id) REFERENCES movies (movie_id),
                        CONSTRAINT FK_movie_studio FOREIGN KEY (studio_id) REFERENCES studio (studio_id)
);"""

INSERT_ACTOR = "INSERT INTO actors (actor_name, date_of_birth, gender) VALUES (?, ?, ?);"

INSERT_DIRECTOR = "INSERT INTO directors (dir_name, dir_date_of_birth, dir_gender) VALUES (?, ?, ?);"

INSERT_GENRE = "INSERT INTO genres (genre_name) VALUES (?);"

INSERT_MOVIE = "INSERT INTO movies (movie_name, release_date, duration, dir_id, movie_rating, review_rating, gross_income) VALUES (?, ?, ?, ?, ?, ?, ?);"

INSERT_STUDIO = "INSERT INTO studio (studio_name) VALUES (?);"

INSERT_MOVIECAST = "INSERT INTO moviecast (movie_id, actor_id, actor_role) VALUES (?, ?, ?);"

INSERT_MOVIEGENRE = "INSERT INTO moviegenre (movie_id, genre_id) VALUES (?, ?);"

INSERT_MOVIESTUDIO = "INSERT INTO moviestudio (movie_id, studio_id) VALUES (?, ?);"

GET_ALL_MOVIES = "SELECT * FROM movies;"

GET_ALL_ACTORS = "SELECT * FROM actors;"

GET_ALL_DIRECTORS = "SELECT * FROM directors;"

GET_ALL_STUDIOS = "SELECT * FROM studio;"

GET_MOVIES_BY_ACTORNAME = """SELECT actor_name, movie_name, actor_role FROM actors as a
                            JOIN moviecast as mc on mc.actor_id = a.actor_id
                            JOIN movies as m on m.movie_id = mc.movie_id where a.actor_id = ?;"""

GET_MOVIES_BY_DIR_ID = """SELECT dir_name, movie_name FROM directors as d
                            JOIN movies as m on m.dir_id = d.dir_id
                            WHERE d.dir_id = ?;"""

GET_MOVIES_BY_MOVIENAME = """SELECT movie_id, movie_name, release_date, duration, dir_name, movie_rating, review_rating, gross_income FROM movies as m
                            JOIN directors as d on d.dir_id = m.dir_id
                            WHERE m.movie_id = ?;"""

GET_MOVIES_BY_GENRES = """SELECT genre_name, movie_name FROM genres as g
                            JOIN moviegenre as mg on mg.genre_id = g.genre_id
                            JOIN movies as m on m.movie_id = mg.movie_id WHERE g.genre_id = ?;"""

GET_MOVIES_BY_STUDIO = """SELECT studio_name, movie_name FROM studio as s
                            JOIN moviestudio as ms on ms.studio_id = s.studio_id
                            JOIN movies as m on m.movie_id = ms.movie_id WHERE s.studio_id = ?;"""

def connect():
    # connection = sqlite3.connect("moviedb.db")
    # print("Database is connected")
    
    return sqlite3.connect("moviedb.db")

def create_tables(connection):
    with connection:
        connection.execute(CREATE_ACTORS_TABLE)
        connection.execute(CREATE_DIRECTORS_TABLE)
        connection.execute(CREATE_GENRE_TABLE)
        connection.execute(CREATE_MOVIE_TABLE)
        connection.execute(CREATE_STUDIO_TABLE)
        connection.execute(CREATE_MOVIECAST)
        connection.execute(CREATE_MOVIEGENRE)
        connection.execute(CREATE_MOVIESTUDIO)

def add_actor(connection, actor_name, date_of_birth, gender):
    with connection:
        connection.execute(INSERT_ACTOR, (actor_name, date_of_birth, gender))

def add_director(connection, dir_name, dir_date_of_birth, dir_gender):
    with connection:
        connection.execute(INSERT_DIRECTOR, (dir_name, dir_date_of_birth, dir_gender))

def add_genre(connection, genre_name):
    with connection:
        connection.execute(INSERT_GENRE, (genre_name,))

def add_movie(connection, movie_name, release_date, duration, dir_id, movie_rating, review_rating, gross_income):
    with connection:
        connection.execute(INSERT_MOVIE, (movie_name, release_date, duration, dir_id, movie_rating, review_rating, gross_income))

def add_studio(connection, studio_name):
    with connection:
        connection.execute(INSERT_STUDIO, (studio_name,))

def add_moviecast(connection, movie_id, actor_id, actor_role):
    with connection:
        connection.execute(INSERT_MOVIECAST, (movie_id, actor_id, actor_role))

def add_moviegenre(connection, movie_id, genre_id):
    with connection:
        connection.execute(INSERT_MOVIEGENRE, (movie_id, genre_id))

def add_moviestudio(connection, movie_id, studio_id):
    with connection:
        connection.execute(INSERT_MOVIESTUDIO, (movie_id, studio_id))

def get_all_movies(connection):
    with connection:
        return connection.execute(GET_ALL_MOVIES,).fetchall()

def get_all_actors(connection):
    with connection:
        return connection.execute(GET_ALL_ACTORS).fetchall()

def get_all_directors(connection):
    with connection:
        return connection.execute(GET_ALL_DIRECTORS).fetchall()

def get_all_studios(connection):
    with connection:
        return connection.execute(GET_ALL_STUDIOS).fetchall()

def get_movies_by_genres(connection, genre_id):
    with connection:
        return connection.execute(GET_MOVIES_BY_GENRES, (genre_id,)).fetchall()

def get_movies_by_actorname(connection, actor_name):
    with connection:
        return connection.execute(GET_MOVIES_BY_ACTORNAME, (actor_name,)).fetchall()

def get_movies_by_dir_id(connection, dir_id):
    with connection:
        return connection.execute(GET_MOVIES_BY_DIR_ID, (dir_id,)).fetchall()

def get_movie_by_moviename(connection, movie_id):
    with connection:
        return connection.execute(GET_MOVIES_BY_MOVIENAME, (movie_id,)).fetchone()

def get_movies_by_studio(connection, studio_id):
    with connection:
        return connection.execute(GET_MOVIES_BY_STUDIO, (studio_id,)).fetchall()