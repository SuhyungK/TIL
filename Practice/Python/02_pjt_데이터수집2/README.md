# Project_02 (22.07.29)

## A. 인기 영화 조회

```python
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

return len(data)
```
- URL 주소는 어떤 걸 써야하고 api키는 어떻게 넣어야 하는지 헤맸는지 한 번 연결하고 나니까 쉬운 문제였다
- 단순히 개수만 반환하면 됐기 때문에 데이터가 담겨 있는 리스트의 길이값을 반환



## B. 특정 조건에 맞는 인기 영화 조회 1

```python
def vote_average_movies():

    URL = 'https://api.themoviedb.org/3/movie/popular'
    params = {
        'api_key' : '26f430349f35e05f01c48db888f30795',
        'language' : 'ko',
        'region' : 'KR'
    }
    response = requests.get(URL, params=params).json()
    data = response['results']
    vote_average_8 = []
    for d in data:
      if d['vote_average'] >= 8.0:
        vote_average_8.append(d)

    return vote_average_8
```

- 평점 8점 이상인 영화들만 추출하는 조건문을 통해 리스트에 값을 추가하는 방식으로 리스트로 정리한 뒤 그대로 반환



## C. 특정 조건에 맞는 인기 영화 조회 2

```python
def ranking():
    URL = 'https://api.themoviedb.org/3/movie/popular'
    params = {
        'api_key' : '26f430349f35e05f01c48db888f30795',
        'language' : 'ko',
        'region' : 'KR'
    }
    response = requests.get(URL, params=params).json()
    datas = response['results']

    return sorted(datas, key= lambda x : x['vote_average'], reverse=True)[:5]
```

- 내장함수 sorted와 람다함수를 통해 리스트에 있는 각각 딕셔너리의 키 값에 따라 정렬했다.
- 상위 5개만 반환하기 위해 `reverse=True` 로 역순 출력, 
- 슬라이싱으로 앞의 5개 값만 반환
- 정렬 후 값을 반환해주는 sorted() 사용
- 이름없는 함수 lambda 사용



## D. 특정 추천 영화 조회

```python
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
```
- 영화를 찾은 뒤 추천 영화를 찾는 방식
- API key값과 같이 query값도 필수(required)로 받음
- 매개변수인 title로 영화의 id 값을 찾아 추천 영화를 받는 url에 추가
- 찾은 영화의 결과값 중 가장 첫번째 영화의 id 값만 추출해야 했는데 이걸 못 찾아서 꼬였다
- 검색한 영화 데이터를 기반으로 추천된 영화 목록의 title만 리스트에 추가시켜 반환
- 검색한 영화의 결과값이 존재하지 않는 경우 response=[]라는 결과가 나오기 때문에 이 상태에서 None으로 반환처리를 했다
- 추천 영화가 없는 경우 자동으로 []값이 반환되었다
  


## E. 출연진, 연출진 데이터 조회

```python
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
```

- D와 같은 방식으로 id를 받아서 크레딧 정보를 받아왔다
- 딕셔너리 키를 통해 casts와 crews 각각의 리스트에 정보를 담은 뒤 조건에 만족하는 값들만 result 딕셔너리에 추가했다. 
- 추가하는 과정은 list comprehension 방식을 사용
- result는 딕셔너리로 각각 cast와 crew 키 값에 리스트 데이터를 추가해줌
 

## 후기

- API를 통해 데이터를 다루는 게 처음이라 어려울 줄 알았는데 처음 연결만 하면 그 뒤는 별로 어렵지 않았다. 오히려 폴더 내에 있는 파일의 데이터를 호출하는 것보다 더 쉽고 재미있었던 것 같다
- 리스트나 딕셔너리 같은 각각 타입의 메서드에 대해서 배우고 난 뒤에 하는 프로젝트라서 더 큰 어려움 없이 할 수 있었다 저번주에는 두 가지를 다루는게 너무 어려웠는데 이번에는 접근하기 쉽게 느껴졌다
- 코드를 짧고 간결하게 짜려고 변수 이름을 무조건 짧게 지었는데 그러다가 더 복잡하게 꼬이는 경우를 경험해서 이번에는 어떤 정보를 담은 변수인지 한 번에 알아볼 수 있게 했다.