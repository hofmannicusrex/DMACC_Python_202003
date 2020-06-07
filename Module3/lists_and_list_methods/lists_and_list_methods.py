"""
Program: lists_and_list_methods.py
Author: Nick Hofmann | nickhofmann1989@hotmail.com | nohofmann@dmacc.edu
Last Modified: 6/6/2020

Program specifications: The program will demonstrate different Python list methods.
"""

listOne = ['Tucker', 'Noel', 'DragonBallZ']

# append
print('---append---')
list.append(listOne, 'Diablo')
print('listOne:', listOne)

# clear
print('\n---clear---')
list.clear(listOne)
print('listOne:', listOne)

# copy (hint: you need two string variables)
listOne = ['Tucker', 'Noel', 'DragonBallZ']
print('\n---copy---')
listOneCopy = list.copy(listOne)
print('listOneCopy:', listOneCopy)

# count
print('\n---count---')
print('Occurrences of the string \'Noel\' in listOne:', listOne.count('Noel'))

# extend
print('\n---extend---')
listOne.extend(['Diablo', 'Heroes of the Storm'])
print('Extended listOne:', listOne)

# index (use twice, once for an item in the list, once for an item not in the list)
listOne = ['Tucker', 'Noel', 'DragonBallZ']
print('\n---index---')
print(listOne.index('Diablo'))
print('Index of string \'Tucker\' in listOne:', listOne.index('Tucker'))

# insert
print('\n---insert---')
listOne.insert(2, 'Diablo')
print('Updated listOne:', listOne)

# remove
listOne = ['Tucker', 'Noel', 'DragonBallZ']
print('\n---remove---')
listOne.remove('DragonBallZ')
print('\'Removed\' listOne:', listOne)

# reverse
print('\n---reverse---')
listOne.reverse()
print('listOne reversed:', listOne)

# sort
listOne = ['Tucker', 'Noel', 'DragonBallZ']
print('\n---sort---')
listOne.sort()
print('Sorted listOne:', listOne)
