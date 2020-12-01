#!/usr/bin/env python3

def findEntries(entries):
   for x in entries:
      for y in reversed(entries):
         if x + y == 2020:
            return x * y

         if x + y < 2020:
            break

def findThreeEntries(entries):
   for index, x in enumerate(entries):
      for y in entries[index + 1:]:
         for z in reversed(entries):
            if x + y + z == 2020:
               return x * y * z

            if x + y + z < 2020:
               break

with open('input/advent1.txt') as f:
   entries = f.readlines()

entries = sorted([int(x) for x in entries])

print('A: {0}'.format(findEntries(entries)))

print('B: {0}'.format(findThreeEntries(entries)))