import media
import fresh_tomatoes

#Instances of the Class Movie that is initialized in media.py
beauty_and_the_beast = media.Movie("Beauty and the Beast",
                                   "A young woman whose father has been imprisoned by a terrifying beast offers herself in his place, unaware that her captor is actually a prince, physically altered by a magic spell.",
                                   "https://images-na.ssl-images-amazon.com/images/M/MV5BMzE5MDM1NDktY2I0OC00YWI5LTk2NzUtYjczNDczOWQxYjM0XkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg",
                                   "https://www.youtube.com/watch?v=W5yATM2LkeM",
                                   "G",
                                   "1991")

lion_king = media.Movie("The Lion King",
                        "Lion cub and future king Simba searches for his identity. His eagerness to please others and penchant for testing his boundaries sometimes gets him into trouble.",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BYTYxNGMyZTYtMjE3MS00MzNjLWFjNmYtMDk3N2FmM2JiM2M1XkEyXkFqcGdeQXVyNjY5NDU4NzI@._V1_UX182_CR0,0,182,268_AL_.jpg",
                        "https://www.youtube.com/watch?v=9E5rd4W7IqA",
                        "G",
                        "1994")

frozen = media.Movie("Frozen",
                     "When the newly crowned Queen Elsa accidentally uses her power to turn things into ice to curse her home in infinite winter, her sister, Anna, teams up with a mountain man, his playful reindeer, and a snowman to change the weather condition.",
                     "https://images-na.ssl-images-amazon.com/images/M/MV5BMTQ1MjQwMTE5OF5BMl5BanBnXkFtZTgwNjk3MTcyMDE@._V1_UX182_CR0,0,182,268_AL_.jpg",
                     "https://www.youtube.com/watch?v=TbQm5doF_Uc",
                     "PG",
                     "2013")

harry_potter = media.Movie("Harry Potter and the Deathly Hallows: Pt 2",
                           "Harry, Ron and Hermione search for Voldemort's remaining Horcruxes in their effort to destroy the Dark Lord as the final battle rages on at Hogwarts.",
                           "https://images-na.ssl-images-amazon.com/images/M/MV5BMTY2MTk3MDQ1N15BMl5BanBnXkFtZTcwMzI4NzA2NQ@@._V1_UX182_CR0,0,182,268_AL_.jpg",
                           "https://www.youtube.com/watch?v=mObK5XD8udk",
                           "PG-13",
                           "2011")

hunger_games = media.Movie("The Hunger Games",
                           "Katniss Everdeen voluntarily takes her younger sister's place in the Hunger Games, a televised competition in which two teenagers from each of the twelve Districts of Panem are chosen at random to fight to the death.",
                           "https://images-na.ssl-images-amazon.com/images/M/MV5BMjA4NDg3NzYxMF5BMl5BanBnXkFtZTcwNTgyNzkyNw@@._V1_UX182_CR0,0,182,268_AL_.jpg",
                           "https://www.youtube.com/watch?v=eO0T9A3kdqc",
                           "PG-13",
                           "2012")

forrest_gump = media.Movie("Forrest Gump",
                           "Forrest Gump, while not intelligent, has accidentally been present at many historic moments, but his true love, Jenny Curran, eludes him.",
                           "https://images-na.ssl-images-amazon.com/images/M/MV5BYThjM2MwZGMtMzg3Ny00NGRkLWE4M2EtYTBiNWMzOTY0YTI4XkEyXkFqcGdeQXVyNDYyMDk5MTU@._V1_UY268_CR10,0,182,268_AL_.jpg",
                           "https://www.youtube.com/watch?v=bLvqoHBptjg&t=15s",
                           "PG-13",
                           "1994")

safe_haven = media.Movie("Safe Haven",
                          "A young woman with a mysterious past lands in Southport, North Carolina where her bond with a widower forces her to confront the dark secret that haunts her.",
                          "https://images-na.ssl-images-amazon.com/images/M/MV5BMTg4MzcxODA3OV5BMl5BanBnXkFtZTcwMTYzNDkwOQ@@._V1_UX182_CR0,0,182,268_AL_.jpg",
                          "https://www.youtube.com/watch?v=SCCdqVFA-88",
                          "PG-13",
                          "2013")

shawshank_redemption = media.Movie("The Shawshank Redemption",
                                   "Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.",
                                   "https://images-na.ssl-images-amazon.com/images/M/MV5BODU4MjU4NjIwNl5BMl5BanBnXkFtZTgwMDU2MjEyMDE@._V1_UX182_CR0,0,182,268_AL_.jpg",
                                   "https://www.youtube.com/watch?v=6hB3S9bIaco",
                                   "R",
                                   "1994")

deadpool = media.Movie("Deadpool",
                       "A fast-talking mercenary with a morbid sense of humor is subjected to a rogue experiment that leaves him with accelerated healing powers and a quest for revenge.",
                       "https://images-na.ssl-images-amazon.com/images/M/MV5BMjQyODg5Njc4N15BMl5BanBnXkFtZTgwMzExMjE3NzE@._V1_UY268_CR1,0,182,268_AL_.jpg",
                       "https://www.youtube.com/watch?v=ONHBaC-pfsk",
                       "R",
                       "2016")

movies = [beauty_and_the_beast, lion_king, frozen, harry_potter, hunger_games, forrest_gump, safe_haven, shawshank_redemption, deadpool]

fresh_tomatoes.open_movies_page(movies)
