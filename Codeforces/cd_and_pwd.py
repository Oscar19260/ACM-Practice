# https://codeforces.com/contest/158/problem/C
# no jala con el test 7
# Israel
import re
import sys

pattern1="(pwd|cd)( (\/)?(.+))?"
pattern2="[^\/]+"
actual_dir=['/']
n=int(input())
for i in range(n):
    line=input()
    split_line=re.search(pattern1,line)
    command=split_line.group(1)
    if split_line.group(2):
        dire=split_line.group(4)
        dirs=dire.split('/')
        for element in dirs:
            if element=="..":
                actual_dir.pop()
            else:
                actual_dir.append(element+"/")
    else:
        string=''
        print(string.join(actual_dir))
