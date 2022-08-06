# Project_01 (22.07.22)

## A. 제공되는 영화 데이터의 주요내용 수집
- 내용 : json을 통한 데이터 추출 & 딕셔너리를 통한 값 반환
  ```python
  def movie_info(movie):
    m_key = ['id', 'title', 'poster_path', 'vote_average', 'overview', 'genre_ids']
    m_info = {}

    for _ in m_key:
        m_info[_] = movie.get(_)

    return m_info
  ```
  - 딕셔너리를 다루는게 익숙하지 않아서 리스트랑 비슷한 방식으로 접근하다보니까 에러가 났다
  - 하나씩 값을 넣었더니 코드가 복잡해졌었는데 키 값으로 접근하니까 빠르고 간단해졌다
  - 딕셔너리는 키 값으로 접근하는게 가장 빠른 것 같다
  - movie.get()을 통해 value 값을 가져오고 그 값을 dict[key] = value() 하는 방식으로 해결했다


## B. 제공되는 영화 데이터의 주요내용 수집
- 내용 : 리스트를 이용한 딕셔너리 값 추출
  ```python
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
  ```
  - id값을 리스트로 가져오는 것까지는 쉬웠는데 그걸 통해 딕셔너리의 값에 접근하는 게 어려웠다. genres 딕셔너리의 값이 id를 담은 리스트에 있는지 찾는 과정을 반복문을 통해 돌려 찾는 줄 알았는데 간단하게 in을 써도 된다는 것을 알게되었다. 파이썬은 정말 너무 쉬운 거 같다...
  - 리스트 추가 기능(append)을 이용해서 따로 genre_names 리스트를 만들고 이걸 새로 딕셔너리에 추가해주는 방식으로 문제를 해결했다


## C. 다중 데이터 분석 및 수정
- 내용 : A,B 에서 데이터를 다룬 방식을 다중 데이터에 적용하기
  ```python
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
  ```
  - B에서와 비슷한 방식으로 코드를 짠 대신에 이번에는 다중 데이터이기 때문에 반복문을 이용했다
  - movies리스트에 담긴 movie 데이터(dictionary 형태)를 하나씩 추출해 B와 같은 방식으로 적용
  - 다중 데이터를 한 번에 반환하기 위해서 새로운 영화 리스트 m_info를 생성하고 append를 통해 값을 추가한 뒤 반환
  
## D. 알고리즘을 사용한 데이터 출력
- json을 통해 다른 폴더에 있는 파일 가져온 후 원하는 데이터 반환
```python
def max_revenue(movies):

    movie_revenue = []
    max_movie_revenue = 0
    for movie in movies:
        _ = open('data/movies/' + str(movie['id']) + '.json', encoding='utf-8')
        movie_detail = json.load(_)
        movie_revenue.append(movie_detail['revenue'])

        if movie_detail['revenue'] == max(movie_revenue):
            max_movie_revenue = movie_detail['title']
    return max_movie_revenue
```
  - json 다루는데 익숙하지 않아서 거의 몇 번 에러를 냈는데 파일명이 movie의 id값과 일치한다는 점을 이용해서 데이터를 불러올 수 있었다. 
  - 처음에는 movie['id']를 이용했는데 int 값 에러가 나 str로 자료형 변환을 통해 해결했다
  - 수익값을 전부 리스트에 넣고 최대값을 구해서 제목만 추출하는 방식으로 문제를 풀었다
  - json 사용빼고는 별로 어렵지 않았다



## E. 알고리즘을 사용한 데이터 출력
- 내용 : 특정 조건에 충족하는 데이터만 반환
```python
def dec_movies(movies):

    movie_release_date = []
    for movie in movies:
        _ = open('data/movies/' + str(movie['id']) + '.json', encoding='utf-8')
        movie_detail = json.load(_)
        release_date = movie_detail['release_date'][5:7]
        if release_date == '12':
            movie_release_date.append(movie_detail['title'])

    return movie_release_date
```
  - D와 비슷하게 작성해서 별로 어렵지 않았다
  - 12월을 가져오는 건 슬라이싱을 통해서 해결했다




# 후기
- json 파일 가져오는 예시가 있는지 모르고 찾아보는게 힘들어서 포기할 뻔 했다
- 혼자 프로젝트 해보는 게 재미있었다 팀원들과 더 복잡하고 큰 프로젝트를 해보는 것도 재미있을 것 같다 아직 실력은 모자라지만...
- 박제되고싶지않다..
- 코드를 짜는 거 자체는 어렵지 않은데 너무 복잡하게 짜는 것 같다 
- 더 간단하거나 쉬운 방식으로 짠 코드를 보면 너무 부럽다...
- 그냥 연습만 하다가 어떤 결과물이 나오는 프로젝트를 하니까 동기부여가 되는 것 같다
- 아직 파이썬의 기본 문법을 잘 모르는 거 같다 리스트나 딕셔너리를 통해 데이터값을 주고 받는 게 어려웠는데 어떤 데이터가 리스트고 딕셔너리인지를 구분하는 과정을 몇 번 해보니까 좀 알 수 있을 것 같다