#counti type in numbs and print max
#ver1
while True:
    num = input('please inpuut\n\ta num(q to quit):')
    if num.lower == 'q':
        break
    num = int(num)
    MaxSoFar = num
    print (MaxSoFar)
    num = input('please inpuut\n\ta num(q to quit):')
    if num.lower == 'q':
        break
    num = int(num)
    if MaxSoFar < num:
            MaxSoFar = int(num)
    print (MaxSoFar)
#ver2
temp = input('please inpuut\n\ta num(q to quit):')
a = [int(temp)]
while True:
    temp = input('please inpuut\n\ta num(q to quit):')
    if temp.lower == 'q':
        break
    num = int(temp)
    a = a.append(num)
    Max = a[0]
    for each in a:
        if each > Max:
            Max = each
    print(Max)
#ver3 finish!!yeeeeeese!!!
temp = input('please inpuut\n\ta num(q to quit):')
a = [int(temp)]
while True:
    temp = input('please inpuut\n\ta num(q to quit):')
    if temp.lower == 'q':
        break
    num = int(temp)
    a.append(num)
    Max = max(a)
    print(Max)
