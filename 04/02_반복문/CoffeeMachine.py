
num = int(input("돈을 넣어 주세요: "))
print("%d을 넣으셨습니다."%num)
number = int(input("돈을 넣어 주세요: "))
print("%d을 넣으셨습니다."%number)
total = num + number

print("총 금액은 %d"%total)

while 1:
    if total > 300:
        print("거스름돈이 있습니다.")
        break  # 루프 종료
    elif money == 300:
        print("동전이 안 남습니다.")
        break  # 루프 종료
    else:
        print("그냥 커피 드세요.")
        break  # 루프 종료
