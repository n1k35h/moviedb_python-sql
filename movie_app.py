from sqlite3 import Date
import movie_system

MENU_PROMPT = """\n --- Movie Database App ---

Please choose one of the following options:

1) Add an Actor
2) Add a Director
3) Add a Genre
4) Add a Movie
5) Add a Studio
6) Add an Actor Role for the Movie
7) Add a Genre to a Movie
8) Add a Studio to a Movie
9) See all Actors
10) See all Directors
11) See all Movies
12) See all Studio
13) Search by Genre
14) Search by Actor
15) Search by Director
16) Search by Movie
17) Search by Studio
18) Exit

Your selection: """

def menu():
    connection = movie_system.connect()
    movie_system.create_tables(connection)
 
    # begin of the while loop
    while (user_input := input(MENU_PROMPT)) != "18": # this loop continues until the user enter 18, which will exit the loop
        if user_input == "1":
            actor_name = input("Enter the Actor's Name: ")
            date_of_birth = input("Enter the Actor's Date of Birth: ")
            gender = input("Enter the Actor's Gender (m/f): ")
            if gender.lower() not in ["m", "f"]:
                print('Invalid Input! Choose either m for Male or f for Female')
                continue
            else:
                print("\n")
                print(actor_name, "added to the Actor table")

            movie_system.add_actor(connection, actor_name, date_of_birth, gender)

        elif user_input == "2":
            dir_name = input("Enter the Director's Name: ")
            dir_date_of_birth = input("Enter the Director's Date of Birth: ")
            dir_gender = input("Enter the Director's Gender (m/f): ")
            if dir_gender.lower() not in ["m", "f"]:
                print('Invalid Input! Choose either m for Male or f for Female')
                continue
            else:
                print("\n")
                print(dir_name, "added to the Director table")

            movie_system.add_director(connection, dir_name, dir_date_of_birth, dir_gender)

        elif user_input == "3":
            genre_name = input("Enter a Genre Name: ")

            print("\n")
            print(genre_name, "added to the Genre table")

            movie_system.add_genre(connection, genre_name)

        elif user_input == "4":
            movie_name = input("Enter a New Movie: ")
            release_date = input("Enter the Release Date of this Movie: ")
            duration = int(input("Enter the Duration of this Movie (in mins): "))
            dir_id = int(input("Enter the ID of the Director: "))
            movie_rating = input("Enter the Movie Rating of the Movie: ")
            review_rating = float(input("Enter the Review Rating of the Movie: "))
            gross_income = int(input("Enter the Gross Income that this Movie Earned: "))

            print("\n")
            print(movie_name, "added to the Movie table\n")
            # cur.execute('SELECT count(movie_name) from movies')
            # count the number of movies 

            movie_system.add_movie(connection, movie_name, release_date, duration, dir_id, movie_rating, review_rating, gross_income)

        elif user_input == "5":
            studio_name = input("Enter a Studio Name: ")

            print("\n")
            print(studio_name, "added to the Studio table")

            movie_system.add_studio(connection, studio_name)

        elif user_input == "6":
            movie_id = int(input("Enter a Movie ID: "))
            actor_id = int(input("Enter a Actor ID: "))
            actor_role = input("Enter the Actor's role for this Movie: ")

            print("\n")
            print(actor_role, "added to the Movie Cast table")

            movie_system.add_moviecast(connection, movie_id, actor_id, actor_role)

        elif user_input == "7":
            movie_id = int(input("Enter a Movie ID: "))
            genre_id = int(input("Enter a Genre ID: "))

            print("\n")
            print("Genre added to the Movie Genre table")

            movie_system.add_moviegenre(connection, movie_id, genre_id)

        elif user_input == "8":
            movie_id = int(input("Enter a Movie ID: "))
            studio_id = int(input("Enter a Studio ID: "))

            print("\n")
            print("Studio added to the Movie Studio table")

            movie_system.add_moviestudio(connection, movie_id, studio_id)
    
        elif user_input == "9":
            actors = movie_system.get_all_actors(connection)
            #need to count the number of movies made by each actors

            for actor in actors:
                print(actor)

        elif user_input == "10":
            directors = movie_system.get_all_directors(connection)
            # need to count the number of movies made by each Directors

            for director in directors:
                print(director)
                
        elif user_input == "11":
            
            movies = movie_system.get_all_movies(connection)

            for movie in movies:
                print(movie)

        elif user_input == "12":

            studios = movie_system.get_all_studios(connection)

            for studio in studios:
                print(studio)

        elif user_input == "13":
            genre_id = int(input("Please enter the Genre's ID: "))
            movies = movie_system.get_movies_by_genres(connection, genre_id)

            for movie in movies:
                print(movie)


        elif user_input == "14":
            actor_id = int(input("Please enter the Actor's ID: "))
            actors = movie_system.get_movies_by_actorname(connection, actor_id)

            for actor in actors:
                print(actor)

        elif user_input == "15":
            dir_id = int(input("Please enter the Director's ID: "))
            directors = movie_system.get_movies_by_dir_id(connection, dir_id)

            for director in directors:
                print(director)

        elif user_input == "16":
            movie_id = int(input("Please enter the Movie's ID to find: "))
            movies = movie_system.get_movie_by_moviename(connection, movie_id)

            print("\nMovie ID: ", movies[0])
            print("Movie Name: ", movies[1])
            print("Released Dated: ", movies[2])
            print("Duration: ", movies[3],"mins")
            print("Director Name: ", movies[4])
            print("Movie Rating: ", movies[5])
            print("Review Rating: ", movies[6])
            print("Grossed Earned: ", f"${movies[7]}")

        elif user_input == "17":
            studio_id = int(input("Please enter the Studio's ID: "))
            movies = movie_system.get_movies_by_studio(connection, studio_id)

            for movie in movies:
                print(movie)          
        else:
            print("\nInvalid input, please try again!\n")

menu()