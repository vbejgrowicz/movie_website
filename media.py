class Movie():
    """This class provides a way to store movie related information including tite, storyline, image, trailer, rating, cast members, and year released"""

    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube, movie_rating, year_released):
        # This constructor initializes the instance variables
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.movie_rating = movie_rating
        self.year_released = year_released
