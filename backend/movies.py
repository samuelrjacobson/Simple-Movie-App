# Class contains a list variable of dictionaries
class Movies:
    def __init__(self, movies_file):
        self._movies = []

        # Read movie info from file, create list
        with open(movies_file, encoding="utf-8") as file:
            row_idx = 0
            for line in file:
                if row_idx%3 == 0:
                    movie_name = line.rstrip()
                if row_idx%3 == 1:
                    movie_cast = line.rstrip().split(',')
                if row_idx%3 == 2:
                    self._movies.append(
                        {
                            'name': movie_name,
                            'cast': movie_cast,
                            'movie_id': (len(self._movies)),
                        }
                    )
                row_idx += 1

    # Get entire movie listing, the one with specified id
    def get_movie_by_id(self, movie_id):
        return self._movies[movie_id]
        
    # Replace entire movie listing with altered listing
    def edit_movie(self, movie_id, newMovieInfo):
        self._movies[movie_id] = newMovieInfo
        return
    
    # Replace entire movie listing with nothing
    def delete_movie(self, movie_id):
        self._movies[movie_id] = None
        return
    
    # Add entered movie listing to end of list
    #def add_movie(self, newMovieInfo):
    #    Assign it an id (numerical, the next unused)
    #    id = len(self._movies)
    #    newMovieInfo['movie_id'] = id
    #    self._movies.append(newMovieInfo)
    #   return id
        
if __name__ == "__main__":
    movies = Movies('./movies.txt')