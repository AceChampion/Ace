import os
os.chdir('/Users/Ace/Documents/YURI/')
lis = []
count = []
for each in os.listdir('/Users/Ace/Documents/YURI/'):
    temp = each.split('.')[-1]
    lis.append(str(temp))
for each in lis:
    temp = lis.count(each)
    count.append(temp)
