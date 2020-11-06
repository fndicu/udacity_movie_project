import media 
import fresh_tomatoes

# list of Francis' favorite movies
rtt = media.Movie('Remember the Titans', "https://upload.wikimedia.org/wikipedia/en/thumb/d/d1/Remember_the_titansposter.jpg/220px-Remember_the_titansposter.jpg", "youtube.com/watch?v=nPhu9XsRl4M")
tp = media.Movie('Treasure Planet', "https://upload.wikimedia.org/wikipedia/en/thumb/7/7e/Treasure_Planet_poster.jpg/220px-Treasure_Planet_poster.jpg","https://www.youtube.com/watch?v=DJNT7C61NrE")
kt = media.Movie("A Knight's Tale", "https://upload.wikimedia.org/wikipedia/en/thumb/a/a6/AKnightsTale.jpg/220px-AKnightsTale.jpg", "https://youtu.be/_KzsTKqTq1M")
im = media.Movie("Iron Man", "https://upload.wikimedia.org/wikipedia/en/0/00/Iron_Man_poster.jpg", "https://youtu.be/8ugaeA-nMTc")

# Grouping movies together in an array to be fed into fresh tomatoes
movies = [rtt, tp, kt, im]
# calling open movies page method in fresh_tomatoes
fresh_tomatoes.open_movies_page(movies)