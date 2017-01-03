def whil():
    num = input('input a number:')
    for each in range(int(num)):
        for i in range(1,int(num)-1):
            if each % i != 0:
                if each < 10:
                    print(each)
                else:                       
                    numlize = ''
                    temp = each
                    lis = list(str(temp))
                    firs = lis[0]
                    lis.pop(0)
                    lis.append(firs)
                    for each in lis:
                        numlize += each
                    numlize = int(numlize)
                    if numlize % 2 != 0:
                        if numlize % 3 != 0:
                            if numlize % 5 != 0:
                                print(numlize)
                        
                        
whil()
