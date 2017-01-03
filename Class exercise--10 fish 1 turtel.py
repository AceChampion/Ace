'''we got 10 fish and a turtel in a pool now.
and the turtel can eat a fish to got 3 energy
if turtel remian 0 energy and the fish remain 0
then the game end'''
class TT:
    energy = int(input('set the ennergy:'))
    def life():
        TT.energy -= 1
    def eat():
        TT.energy += 3
class Fish:
    numb = 10
    def be_eated():
        Fish.numb -= 1
t = TT
f = Fish
while f.numb != 0:
    if t.energy > 0:
        print('now i have '+ str(t.energy) + ' energy')
        t.life()
        print('i lose an energy')
        print(str(t.energy) + ' energy now')
    else:
        t.eat()
        print('eat a fish')
        f.be_eated()
        print('now i have '+ str(t.energy) + ' energy')
        print('remian '+ str(f.numb) + ' fish now')
    continue
print('end')
