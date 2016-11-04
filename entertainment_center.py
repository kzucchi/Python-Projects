import media

toy_story = media.Movie ("Toy Story","A story of a boy and his toys that come to life", "http://bit.ly/2fjKVGL", "http://bit.ly/VZggnq")
                        
print (toy_story.storyline)

avatar = media.Movie ("Avatar", "A marine lost on a island with aliens", "https://en.wikipedia.org/wiki/File:Avatar-Teaser-Poster.jpg", "http://bit.ly/2fk1rsF")

print (avatar.storyline)

avatar.show_trailer()
