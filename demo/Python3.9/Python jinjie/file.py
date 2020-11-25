from io import StringIO
import os
f = open('D:/Users/season/Desktop/python.txt', 'r', encoding="utf-8")
print(f.read())
f.close()
with open('D:/Users/season/Desktop/python.txt', 'r', encoding="utf-8", errors='ignore') as f:
    # print(f.read())
    for line in f.readlines():
        print(line.strip())
with open('D:/Users/season/Desktop/favicon.ico', 'rb') as f:
    print(f.read())
filename = 'D:/Users/season/Desktop/pyfile.txt'
# with open(filename, 'w', encoding='utf-8') as f:
with open(filename, 'a', encoding='utf-8') as f:
    f.write("first : this is second changshi")
    f.close()

