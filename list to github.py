lis = [1,'hhaha',['werew',2333]]

#add new character
lis.append('x')

#add new characterS, need extend
lis.extend(['hssss',666])

#insert 'dsada' at the fifth space
lis.insert(4,'dsada')

#have a look the fourth charactar
lis[3]

#list can be operated
lis *= 3

# index from 3 to 7 and print exactlly where is it
lis.index('hhaha', 3, 7)

# reverse the list
lis.reverse

# put name in it directly can't remove 2333 cuz it's in a list
lis.remove(4)
#and remove(name) can only remove the first 'name' in list,try it!

# auto print and delete last one in list
lis.pop()
# print and del the 3rd charactar
lis.pop(2)
# list slice begin at 3 to last
lis[3:]
#better creat a new list like lis2 = lis[3:]

#samely,begin at 0 to 3
lis[:3]

#u can also use this way to copy list
lis3 = lis[:]

# a BIF del can del everything
del lis[2]
del lis

lis2 = [3, 9, 6, 4, 5, 7]
# sort list
lis2.sort()

#join,make list muti and spill the joined list
jointhing = 'Ace'
lisj = jongthing.join('12345')
#and lisj = '1Ace2Ace3Ace4Ace5'
