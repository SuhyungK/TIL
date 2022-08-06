import requests
from pprint import pprint


def recommendation(title):
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

    search_URL = 'https://api.themoviedb.org/3/movie/' + str(movie_id) + '/recommendations'
    search_response = requests.get(search_URL, params=params).json()['results']
    
    titles = []
    for s in search_response:
        titles.append(s['title'])

    return titles

    
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화의 id를 기반으로 추천 영화 목록 구성
    추천 영화가 없을 경우 []를 반환
    영화 id 검색에 실패할 경우 None을 반환
    (주의) 추천 영화의 경우 아래 예시 출력과 차이가 있을 수 있음
    """
    # pprint(recommendation('기생충'))
    # # ['조커', '1917', '조조 래빗', ..생략.., '살인의 추억', '펄프 픽션']
    # pprint(recommendation('그래비티'))
    # # []
    # pprint(recommendation('검색할 수 없는 영화'))
    # # None
