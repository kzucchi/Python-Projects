import fresh_tomatoes
import media

toy_story = media.Movie ("Toy Story","A story of a boy and his toys that come to life", "http://bit.ly/2fjKVGL", "http://bit.ly/VZggnq")
                        
#print (toy_story.storyline)

avatar = media.Movie ("Avatar", "A marine lost on a island with aliens", "https://en.wikipedia.org/wiki/File:Avatar-Teaser-Poster.jpg", "http://bit.ly/2fk1rsF")

#print (avatar.storyline)

#avatar.show_trailer()

pursuit_of_happyness = media.Movie ("Pursuit of Happyness", "A single father who pursues a career as a stockbroker", "http://bit.ly/2fodFy5", "http://bit.ly/1s2tMjQ")

#pursuit_of_happyness.show_trailer()

#movies is an array

movies = [toy_story, avatar, pursuit_of_happyness]

#fresh_tomates.open_movies_page(movies)

#print(media.Movie.VALID_RATINGS)

print(media.Movie.__doc__)


print(media.Movie.__name__)

print(media.Movie.__module__)
