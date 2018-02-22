# Hello World program in Python

# repeat_lyrics()

# def repeat_lyrics():
#     print_lyrics()
#     print_lyrics()
    
# def print_lyrics():
#     print("I'm a lumberjack, and I'm okay.")
#     print("I sleep all night and I work all day.")

# repeat_lyrics()

# def style_1():
#     print( ('+ ' + '- ' * 4) * 2 + '+')
    
# def style_2():
#     print( ('| ' + ' ' * 8) * 2 + '|')

# def draw():
#     for i in range(1, 12):
#         if i == 1 or i == 6 or i == 11:
#             style_1()
#         else: style_2()

# draw()

# if 1 > 0 and 0 < 1:
# 	print("hello")
# 	print("hien")

# def recuse():
# 	recuse()
# recuse()

# name = input('name: ?\n')
# print(name)

# import time
# print(time.time())

# def check_fermat(a, b, c, n):
# 	if a ** n + b ** n == c ** n:
# 		print('Holy smokes, Fermat was wrong!')
# 	else:
# 		print("No, that doesn't work", "Hi")

# a = input('a = ')
# b = input('b = ')
# c = input('c = ')
# n = input('n = ')
# a = int(a)
# b = int(b)
# c = int(c)
# n = int(n)
# check_fermat(a, b, c, n)

# str = 'HienPham'
# print(str.lower())
# print(ord('c') - ord('a'))
# print(ord('c'))

# fin = open('words.txt')
# for line in fin:
# 	word = line.strip()
# 	print(word)

#chapter10
# t = ['d', 'd', 'e', 'b', 'a']
# t.remove('d')
# print(t)
# 
# def is_anagram(l1, l2):
# 	# khac len -> False
# 	if len(l1) != len(l2):
# 		return False
# 	# duyet va xoa cac phan tu l1 trong l2
# 	for e in l1:
# 		if e in l2:
# 			l2.remove(e)
# 		else:
# 			return False
# 	# neu l2 khac [] -> False
# 	if len(l2) != 0:
# 		return False
# 	# True
# 	return True
	
# str1 = input('str1 = ')
# str2 = input('str2 = ')
# list1 = list(str1)
# list2 = list(str2)
# print(list1, list2)
# if is_anagram(list1, list2) == True:
# 	print('Two strings are anagrams!')
# else:
# 	print('Not anagrams!')

#chapter11: dictionaries
# dic = dict({'key': 'value'})
# print(dic)
# dic['key1'] = 'value1'
# print(dic)
# for key, value in dic.items():
# 	print(key, value)

# test = False
# def change():
# 	# global test
# 	test = True
# 	print(test)

# change()
# print(test)

#Chapter12: Tuples

# t = ('a',)
# print(type(t))
# a, b = 1, 2
# a, b = b, a
# print(a, b)

# Here is an example of a function that returns a tuple:
# def min_max(t):
# 	return min(t), max(t)

# def sum_all(*args):
# 	sum = 0
# 	for e in args:
# 		sum += e
# 	return sum

# print(sum_all(1, 2, 3, 5))

# l1 = ('a', 1, 'c')
# l2 = [1, 2, 3]
# print(zip(l1, l2))
# for pair in zip(l1, l2):
# 	print(pair)

# d = {1: 'a', 2: 'b', 3: 'c'}
# print(d.items())

# d = dict(zip('abc', (1, 2, 3)))
# print(d)

# import random	
# l = [1, 2, 4]
# for i in range(10):
# 	x = random.choice(l)
# 	print(x)

# str = ' pham duc   hien '
# print(str.split())

# import os
# cmd = 'ls -l'
# fp = os.popen(cmd)
# res = fp.read()
# fp.close()
# print(res)

#Chapter15: Classes and Objects

# class Time:
	
# 	def __init__(self):
# 		self.hour = 0
# 		self.minute = 0
# 		self.second = 0
	
# time1 = Time()
# time1.hour = 10
# time1.minute = 11
# time1.second = 12

# def print_time(time):
# 	print('{:02d}: {:02d}: {:02d}\n'.format(
# 		time.hour, time.minute, time.second)
# 	)

# print_time(time1)

# class Parent:        # define parent class
#    parentAttr = 100
#    def __init__(self):
#       print ("Calling parent constructor")

#    def parentMethod(self):
#       print ('Calling parent method')

#    def setAttr(self, attr):
#       Parent.parentAttr = attr

#    def getAttr(self):
#       print ("Parent attribute :", Parent.parentAttr)

# class Child(Parent): # define child class
#    def __init__(self):
#       print ("Calling child constructor")

#    def childMethod(self):
#       print ('Calling child method')

# c = Child()          # instance of child
# c.childMethod()      # child calls its method
# c.parentMethod()     # calls parent's method
# c.setAttr(200)       # again call parent's method
# c.getAttr()          # again call parent's method

class Time:
	__hour = 'Hien'

	def __init__(self, hour):
		self.__hour = hour

time = Time(10)
print(Time._Time__hour)