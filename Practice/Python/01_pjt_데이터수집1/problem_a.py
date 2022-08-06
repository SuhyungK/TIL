import json
from pprint import pprint


def movie_info(movie):
    m_key = ['id', 'title', 'poster_path', 'vote_average', 'overview', 'genre_ids']
    m_info = {}

    for _ in m_key:
        m_info[_] = movie.get(_)

    return m_info

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='utf-8')
    movie_dict = json.load(movie_json)
    
    pprint(movie_info(movie_dict))
