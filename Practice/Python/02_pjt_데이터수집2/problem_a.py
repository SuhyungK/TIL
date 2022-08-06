import requests


def popular_count():

    URL = 'https://api.themoviedb.org/3/movie/popular'
    params = {
        'api_key' : '26f430349f35e05f01c48db888f30795',
        'language' : 'ko',
        'region' : 'KR'
    }
    response = requests.get(URL, params=params).json()
    data = response['results']
    
    return len(data)
    
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20