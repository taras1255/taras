#! /usr/bin/env python  
# -*- coding: utf-8 -*-
print('Калькулятор')
num1= float(input('ведыть перше число:   '))
num2= float(input('ведыть друге число:   '))
print()
print("операцыи")
print()
print("1 - додавання")
print("2 - выднымання")
print("3 - множення")
print("4 - дылення")
vibir =float(input(' зробыть вибыр      '))

if vibir == 1:
   rezult = num1 + num2
   print("сума двох  " + str(rezult))
elif vibir == 2:
    rezult= num1 - num2
    print("рызниця двох  " + str(rezult))
elif vibir == 3:
    rezult = num1 * num2 
    print("добуток двох  " + str(rezult))
elif vibir == 4:
    rezult = num1 / num2
    print("Частка двох  " + str(rezult))
else:
 print('Eror')