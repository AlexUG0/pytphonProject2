def get_bellow_avg(my_list):
    avg = sum(my_list) / len(my_list)
    return [i for i in my_list if i < avg]


def get_unique(my_list):
    return list(set(my_list))

def get_films_by_genre(films_list, genre):
    new_film_list = []
    for film in films_list:
        if film['genre'].lower() == genre.lower():
            new_film_list.append(film['title'])

    return  new_film_list