import json

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

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)
    
    print(max_revenue(movies_list))
