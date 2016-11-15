# -*- coding: utf-8 -*-
import random

data1 = []
pesel = []
scale = [1,3,7,9,1,3,7,9,1,3]
odd_plec = [0,2,4,6,8]
last2 = 0
d = 0

print 'Podaj datę urodzenia (DD-MM-RRRR): '
data = raw_input()
data1.append(data.split('-'))
day1 = data1[0][0]
mounth1 = data1[0][1]
year1 = data1[0][2]

if 1800 <= int(year1)<= 1899:
    d = 8
elif 1900 <= int(year1) <= 1999:
    d = 0
elif 2000 <= int(year1) <= 2099:
    d = 2
elif 2100 <= int(year1) <= 2199:
    d=4
elif 2200<=int(year1)<=2299:
    d = 6
else:
    print 'Rok spoza dopuszczonego zakresu'

pesel.extend([int(year1[2:3]),int(year1[3:]),int(mounth1[:1])+d,int(mounth1[1:]),int(day1[:1]),int(day1[1:])])

for i in range(1,5):
    number = random.randint(0, 9)
    pesel.append(number)
    i = i + 1
for a in range (0,10):
    last1 = (pesel[a] * scale[a])
    last2 = last2 + last1
    last = (last2 % 10)
if last == 0:
    pesel.append(0)
else:
    pesel.append(10 - last)
if pesel[9]in odd_plec:
    print 'Jesteś kobietą'
else:
    print 'Jesteś mężczyzną'
print ''.join(str(i) for i in pesel)

