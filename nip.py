# -*- coding: utf-8 -*-
#generator nip

import random

scale = [6,5,7,2,3,4,5,6,7]

while True:
    nip=[]
    i=0
    last1=0
    for i in range(0,9):
        if i == 0 or i == 2:
            number = random.randint(1, 9)
        else:
            number = random.randint(0, 9)

        nip.append(number)
        last1 = last1 + (nip[i] * scale[i])
        i = len(nip)

    last = last1 % 11
    print last

    if last == 10:
        continue
    else:
        nip.append(last)
        print ''.join(str(i) for i in nip)

    print 'Wygenerować kolejny nip (t/n)?'
    answer = raw_input()
    if answer == 'tak' or answer == 't':
        continue
    else:
        break