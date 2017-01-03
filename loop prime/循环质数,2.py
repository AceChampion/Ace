#只有1、3、7、9这四个数字组成的1-6位数的组合数，才有可能是循环质数（因为0、2、4、5、6、8排在最末一位，如果不是1位数，就肯定不是质数）
# 所以用这四个数来进行组合，再循环后判断是否全部为质数。
# -*- coding:Utf-8 -*-
import itertools
import time,math
start = time.clock()

def isPrime(n):#质数判断
    if n == 1:
        return False
    elif n < 4:
        return True
    elif n & 1 == 0:      #what is it
        return False
    elif n < 9:
        return True
    elif n %3 == 0:
        return False
    else:
        r = math.floor(math.sqrt(n))       #what is floor
        f = 5
        while f <= r:
            if n % f == 0:
                return False
            if n %(f+2) == 0:
                return False
            f += 6
        return True

def check_nm(j): #是否为循环质数
    list_each=[]
    for each_str in j:
        list_each.append(each_str)
    for i in range(0,len(list_each)):
        s=''
        for each in list_each:
            s+=each
        if isPrime(int(s)):
            list_each.append(list_each[0])
            del list_each[0]
        else:
            return 0
    return 1

list_temp=['2','5']
for i in range(1, 7):
    for eachone in list(itertools.product(['1','3','7','9'],repeat = i)):
        s=''
        for aa in eachone:
            s+=aa
        if check_nm(s):
            list_temp.append(s)

print(len(list_temp))

end = time.clock()
print ("read: %f s" % (end - start))