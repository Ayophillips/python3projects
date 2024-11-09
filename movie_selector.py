import random
import json

# Function to read movies from the file
def read_movies_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            movies = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        movies = []
    return movies

# Function to write movies to the file
def write_movies_to_file(file_path, movies):
    with open(file_path, 'w') as file:
        json.dump(movies, file)

# Function to get movie input from the user
def get_movie_input(file_path):
    movies = read_movies_from_file(file_path)
    done = False
    
    while not done:
        title = input("Enter a movie title (or type 'done' to finish): ")
        if title.lower() == 'done':
            done = True
        else:
            category = input("Enter the category (Movie, TV Show, Animation): ").strip().lower()
            while category not in ['movie', 'tv show', 'animation']:
                print("Invalid category. Please enter 'Movie', 'TV Show', or 'Animation'.")
                category = input("Enter the category (Movie, TV Show, Animation): ").strip().lower()
            
            movies.append({"title": title, "category": category})
    
    write_movies_to_file(file_path, movies)

# Function to select a random movie
def select_random_movie(movies):
    if not movies:
        print("No movies available to select.")
        return None
    
    random_movie = random.choice(movies)
    return random_movie

# Main function
def main():
    file_path = 'movies.json'
    print("Welcome to the Movie Selector!")

    def ask_for_random_movie():
        choice = input("Do you want to select a random movie to watch? (yes/no): ").strip().lower()
        
        if choice == 'yes':
            movies = read_movies_from_file(file_path)
            selected_movie = select_random_movie(movies)
            if selected_movie:
                print(f"How about watching '{selected_movie['title']}' from the '{selected_movie['category'].capitalize()}' category?")
            ask_for_random_movie()
        elif choice == 'no':
            print("Okay, maybe next time!")
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
            ask_for_random_movie()
    
    choice = input("Do you want to update the movie list? (yes/no): ").strip().lower()
    if choice == 'yes':
        get_movie_input(file_path)
    
    ask_for_random_movie()

if __name__ == "__main__":
    main()
