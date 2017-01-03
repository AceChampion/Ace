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
