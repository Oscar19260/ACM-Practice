# https://codeforces.com/contest/158/problem/C
import re
import sys
pattern1="(pwd|cd)( (\/)?(.+))?"
actual_dir=['/']
n=int(input())
for i in range(n):
    line=input()
    split_line=re.search(pattern1,line)
    command=split_line.group(1)
    if split_line.group(2):
        dire=split_line.group(4)
        dirs=dire.split('/')
        if split_line.group(3):
            actual_dir=['/']
        for element in dirs:
            if element=="..":
                actual_dir.pop()
            else:
                actual_dir.append(element+"/")
    else:
        string=''
        print(string.join(actual_dir))
