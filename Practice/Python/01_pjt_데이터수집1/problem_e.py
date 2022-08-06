import json


def dec_movies(movies):

    movie_release_date = []
    for movie in movies:
        _ = open('data/movies/' + str(movie['id']) + '.json', encoding='utf-8')
        movie_detail = json.load(_)
        release_date = movie_detail['release_date'][5:7]
        if release_date == '12':
            movie_release_date.append(movie_detail['title'])

    return movie_release_date

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)
    
    print(dec_movies(movies_list))
