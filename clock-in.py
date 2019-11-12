'''
@Author: Yao Lu
@Date: 2019-11-12 20:01:43
@Description: Clock in github.
'''
import os
import time

git_pull = 'git pull'
git_add = 'git add .'
git_commit = 'git commit -m '
git_push = 'git push -u origin master'
os.system(git_pull)
clock_in_file = './clock-in.txt'
with open(clock_in_file, 'a') as f:
    timeStamp = time.time()
    localTime = time.localtime(timeStamp)
    strTime = time.strftime("%Y-%m-%d %H:%M:%S", localTime)
    clock_in_content = strTime + " I have clocked in."
    f.write(clock_in_content)

os.system(git_add)
os.system(git_commit + '\'' + strTime + '\'')
os.system(git_push)