#!/usr/bin/env python3

def checkPassword(entry):
   policy, password = entry.split(': ')
   letter = policy[-1]
   letterRange = policy[:-2]
   letterMin, letterMax = (int(x) for x in letterRange.split('-'))

   count = password.count(letter)



   return count >= letterMin and count <= letterMax, (password[letterMin - 1] == letter) != (password[letterMax - 1] == letter)





with open('input/advent2.txt') as f:
   entries = f.readlines()

count1 = 0
count2 = 0
for entry in entries:
   check1, check2 = checkPassword(entry)
   if check1:
      count1 += 1
   if check2:
      count2 += 1


print('A: {0}'.format(count1))
print('B: {0}'.format(count2))
