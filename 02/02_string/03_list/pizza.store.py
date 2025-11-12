movies = {'파묘': [23.6, 5.5, 11914798],
          '범죄도시4': [20.6, 8.8, 11502779],
          '인사이드 아웃2': [15.6, 8.8, 7525302],
          '베테랑2': [10.8, 5.3, 5000000]}

# 특정 영화 관객수 출력
print(movies["파묘"][2])

# 평점이 8.8인 영화 제목 출력 (방법1)
for i in movies:
    if movies[i][1] == 8.8:
        print(i)

# 평점이 8.8인 영화 제목 출력 (방법2, items 사용)
for title, info in movies.items():
    if info[1] == 8.8:
        print(title)

print('*'*50)

# 관객수가 100만 이상인 영화 출력
for i in movies:
    if movies[i][2] > 1000000:
        print(i)
