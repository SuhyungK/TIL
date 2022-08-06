import json
from pprint import pprint


def movie_info(movie, genres):
    m_key = ['id', 'title', 'poster_path', 'vote_average', 'overview']
    m_info = {}

    genre_ids = movie.get('genre_ids')
    genre_names = []
    for genre in genres:
        if genre['id'] in genre_ids:
            genre_names.append(genre.get('name'))

    m_info['genre_names'] = genre_names

    for _ in m_key:
        m_info[_] = movie.get(_)
    
    return m_info
        

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='utf-8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='utf-8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))
