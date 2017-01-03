#hanoi
def hanoi(n, x, y, z):
    if n == 1:
        print(x,' --> ' ,z)
    else:
        hanoi(n-1, x, z, y)
        print(x,' --> ' ,z)
        hanoi(n-1, y, x, z)

n = int(input('how many stage:'))
hanoi(n, 'X', 'Y', 'Z')

how many stage:4
X  -->  Y
X  -->  Z
Y  -->  Z
X  -->  Y
Z  -->  X
Z  -->  Y
X  -->  Y
X  -->  Z
Y  -->  Z
Y  -->  X
Z  -->  X
Y  -->  Z
X  -->  Y
X  -->  Z
Y  -->  Z

how many stage:5
X  -->  Z
X  -->  Y
Z  -->  Y
X  -->  Z
Y  -->  X
Y  -->  Z
X  -->  Z
X  -->  Y
Z  -->  Y
Z  -->  X
Y  -->  X
Z  -->  Y
X  -->  Z
X  -->  Y
Z  -->  Y
X  -->  Z
Y  -->  X
Y  -->  Z
X  -->  Z
Y  -->  X
Z  -->  Y
Z  -->  X
Y  -->  X
Y  -->  Z
X  -->  Z
X  -->  Y
Z  -->  Y
X  -->  Z
Y  -->  X
Y  -->  Z
X  -->  Z
