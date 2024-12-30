#from src.utils import get_unique
#x=1
#word = 'hello'

#print(get_bellow_avg([1, 2, 3, 4, 5, 1000]))

#print(get_unique(['apple', 'bannana', 'apple']))
#
from src.utils import get_films_by_genre

films = [
        {'title': 'The Shawshank Redemption', 'genre': 'Drama', 'director': 'Frank Darabont'},
        {'title': 'The Godfather', 'genre': 'Crime', 'director': 'Francis Ford Coppola'},
        {'title': 'The Dark Knight', 'genre': 'DRAMA', 'director': 'Christopher Nolan'}
]
genre = 'crime'

print(get_films_by_genre(films, genre))
