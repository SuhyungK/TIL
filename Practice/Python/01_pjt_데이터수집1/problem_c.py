import json
from pprint import pprint


def movie_info(movies, genres):
    m_info = []
    m_key = ['id', 'title', 'poster_path', 'vote_average', 'overview']

    for movie in movies:
        genre_ids = movie.get('genre_ids')
        genre_names = []
        for genre in genres:
            if genre['id'] in genre_ids:
                genre_names.append(genre.get('name'))

        m_info.append({'genre_names':genre_names})
        
        m_info_dict = {}
        for key in m_key:
            m_info_dict[key] = movie[key]

        m_info.append(m_info_dict)

    return m_info

        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='utf-8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))