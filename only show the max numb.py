#counti type in numbs and print max
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
