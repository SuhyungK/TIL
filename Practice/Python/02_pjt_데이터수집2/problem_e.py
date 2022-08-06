import requests
from pprint import pprint


def credits(title):
    URL = 'https://api.themoviedb.org/3/search/movie'
    params = {
        'api_key' : '26f430349f35e05f01c48db888f30795',
        'language' : 'ko',
        'region' : 'KR',
        'query' : title
    }
    response = requests.get(URL, params=params).json()['results']
    if response == []:
        return None
    
    movie_id = response[0]['id']

    credits_URL = 'https://api.themoviedb.org/3/movie/' + str(movie_id) + '/credits'
    credits_response = requests.get(credits_URL, params=params).json()
    casts = credits_response['cast']
    crews = credits_response['crew']

    result = {}
    cast = result.update(cast=[c['name'] for c in casts if c['cast_id'] < 10])
    crew = result.update(crew=[c['name'] for c in crews if c['department'] == 'Directing'])

    return result


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화 id를 통해 영화 상세정보를 검색하여 주연배우 목록(cast)과 스태프(crew) 중 연출진 목록을 반환
    영화 id 검색에 실패할 경우 None을 반환
    """
    pprint(credits('기생충'))
    # {'cast': ['Song Kang-ho', 'Lee Sun-kyun', ..., 'Jang Hye-jin'], 'crew': ['Bong Joon-ho', 'Park Hyun-cheol', ..., 'Yoon Young-woo']}
    pprint(credits('검색할 수 없는 영화'))
    # None
