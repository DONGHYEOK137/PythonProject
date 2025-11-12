cities = ['seoul', 'daejeon', 'kimpo', 'suncheon', 'pusan']

# 각 도시 이름 길이 계산
cities_length = [len(city) for city in cities]

longest_length = max(cities_length)
shortest_length = min(cities_length)

# 리스트 초기화
longest_list = []
shortest_list = []

# 가장 긴 도시와 가장 짧은 도시 찾기
for city in cities:
    if len(city) == longest_length:
        longest_list.append(city)
    elif len(city) == shortest_length:
        shortest_list.append(city)

print("가장 긴 길이:", longest_length)
print("가장 긴 도시:", longest_list)
print("가장 짧은 길이:", shortest_length)
print("가장 짧은 도시:", shortest_list)
