path = "/etc/passwd"
a = path.split('/')  # '\' 기준으로 나눔
b = a[-1]             # 마지막 요소 가져오기

print(path)
print(b)
