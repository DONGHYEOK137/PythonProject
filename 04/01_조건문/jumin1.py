# j = input("주민등록번호: ")
j = "821010-1635210"
# print(j)
# print(j[7], j[8:10])

gender = int(j[7])
locale = int(j[8:10])

# 성별 판별
if gender == 1 or gender == 3:
    print("[ 성별 ] 남자")
elif gender == 2 or gender == 4:
    print("[ 성별 ] 여자")
else:
    print("[ INFO ] 알 수 없음")