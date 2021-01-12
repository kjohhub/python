# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 16:41:05 2021

@author: 경진
"""

### write
f = open("live.txt", "wt")
f.write("""삶이 그대를 속일지라도
슬퍼하거나 노여워하지 말라!
우울한 날들을 견디면
믿으라, 기쁨의 날이 오리니""")
f.close()


### read
try:
    f = open("live.txt", "rt")
    text = f.read()
    print(text)
except FileNotFoundError:
    print("파일이 없습니다.")
finally:
    f.close()
print()
    
    
### readline
f = open("live.txt", "rt")
text = ""
line = 1
while True:
    row = f.readline()
    if not row:
        break
    text += str(line) + " : " + row
    line += 1
f.close()
    
print(text)
print()


### readlines
f = open("live.txt", "rt")
rows = f.readlines()
for row in rows:
    print(row, end = '')
f.close()
print()
print()


### readfile
f = open("live.txt", "rt")
for line in f:
    print(line, end = '')
f.close()
print()
print()


### seek
f = open("live.txt", "rt")
f.seek(12, 0)
text = f.read()
f.close()
print(text)
print()


### append
f = open("live.txt", "at")
f.write("\n\n푸쉬킨 형님의 말씀이었습니다")
f.close()


## with open
with open("live.txt") as f:
    text = f.read()
print(text)
        