url = input("address: ")
print(url)

domain = url.split('/')[2]          # 예: 'www.naver.com'
extension = domain.split('.')[-1]   # 예: 'com'

print("domain:", extension)
