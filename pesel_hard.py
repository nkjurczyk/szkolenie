# -*- coding: utf-8 -*-

#path=r'C:\python dla testerow\pesel.txt'
#path2=r'C:\python dla testerow\pesel2.txt'
pesel=[]
day=[]
d=0
year=[]
scale = [1,3,7,9,1,3,7,9,1,3]
check=[]
correct=[]
incorrect=[]

def data(d):
    if month in range (0,13):
        d=0
        year.append(19)
    elif month in range (20,33):
        d=20
        year.append(20)
    elif month in range (40,53):
        d=40
        year.append(21)
    elif month in range (60,73):
        d=60
        year.append(22)
    elif month in range (80,93):
        d=80
        year.append(18)
    else:
        print 'Niepoprawny rok'
    return d


def month_name():
    a=int(line[2]+line[3])-data(d)
    if a ==1:
        month='stycznia'
    elif a==2:
        month='lutego'
    elif a==3:
        month='marca'
    elif a==4:
        month='kwietnia'
    elif a==5:
        month='maja'
    elif a==6:
        month='czerwca'
    elif a==7:
        month='lipca'
    elif a==8:
        month='sierpnia'
    elif a ==9:
        month='wrzesnia'
    elif a==10:
        month='pazdziernika'
    elif a==11:
        month='listopada'
    else:
        month = 'grudnia'
    return month


def birth_date():
    if len(line)==12:
        check_pesel()
        if int(line[10])==int(check[0]):
            month_name()
            correct.append(pesel[0][:11])
            day.extend([(line[4] + line[5]), month_name(), str(year[0]) + line[0] + line[1]])
            write()
        else:
            incorrect.append(pesel[0][:len(line)-1])
    else:
        incorrect.append(pesel[0][:len(line)-1])
    del day[:]
    del pesel[:]

def check_pesel(control_sum=0):
    for a in range(0, 10):
        control_sum = control_sum + (int(line[a]) * scale[a])
    last_number = (control_sum % 10)
    if last_number == 0:
        check.append(0)
    else:
        check.append(10 - last_number)

def write():
    append_file = open('zapisane_numery_pesel.txt', 'a')
    append_file.write (pesel[0][:11])
    append_file.write (" : ")
    append_file.write(' '.join(str(i) for i in day))
    append_file.write('\n')
    append_file.close()

#------------------------------------------------------------

file=open('lista_pesel.txt')

for line in file:
    pesel.append(line)
    del year[:]
    del check[:]
    month = int(line[2] + line[3])
    birth_date()

print 'poprawne',len(correct), ' :\n', ('\n'.join(str(i) for i in correct))
print 'niepoprawne', len(incorrect), ' :\n', ('\n'.join(str(i) for i in incorrect))
file.close()