import os

content = """반갑습니다.
python 개발자 여러분 한살 더 드셨죠!
올 한해는... 행복한 가득한 한해가 되었으면 합니다."""

f = open('t.txt', 'w')
f.write(content)
f.close()
if os.path.exists("t.txt"):
    print("The file removed.")
else:
    print("The file does not exist.")
    os.remove('t.txt')




