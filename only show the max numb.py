#counti type in numbs and print max
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
