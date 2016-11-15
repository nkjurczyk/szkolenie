# -*- coding: utf-8 -*-
#generator nip

import random
nip = []
scale = [6,5,7,2,3,4,5,6,7]
i = 1
last2 = 0
getData = True
while getData:
    for i in range(1,10):
        if i == 1 or i == 3:
            number = random.randint(1, 9)
        else:
            number = random.randint(0, 9)

        nip.append(number)
        i = len(nip)
        #print 'i',i
        last1 = (nip[i-1] * scale[i-1])
        last2 = last2 + last1

    last = last2 % 11
#    print 'last',last
    if last == 10:
        i = 1 #powinien wrócić do generowania
    else:
        nip.append(last)
        print ''.join(str(i) for i in nip)

    print 'Wygenerować kolejny nip (t/n)?'
    answer = raw_input()
    if answer == 'tak' or answer == 't':
        continue
    else:
        break