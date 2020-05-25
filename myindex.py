import os
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
import csv
import re
#
#
#
# plt.xkcd()
#
#
#
# # f = np.array([2,3,4], dtype=np.int16)
# # print(f)
# #
# # for game in f:
# #     print('Number: ', game)
# #
# #
# # w = np.random.randint(0,10,5)
# # print(w)
# #
# #
# # a = np.array([2,4,5,6,7,9])
# # a= a.reshape(3,2)
# # print(a)
# # print(a.sum(axis=0))
#
# #
# # b = np.array([[1,2,3,4,5,6,7], [8,9,10,11,12,13,14]], dtype=np.int16)
# # print(b[1][6])
# # print(b[0, 1:6:2])
# #
# # b[1,5]= 20
# # print(b)
# # print('\n')
# # b[:,2]= [1,3]
# # print(b)
# #
# #
# #
# #
# # c= np.array([[[1,2], [3,4]], [[5,6], [7,8]]])
# # print(c)
# # print(c[0,1,1])
# #
# # d = np.zeros((2,3))
# # print(d)
# #
# # e= np.ones((3,3), dtype='int32')
# # print(e)
# # print('\n')
# #
# # s = np.full((2,2), 100)
# # s= np.full_like(d, 6)
# # s = np.random.rand(4,2)
# # s = np.random.randint(6,10, size=(3,3))
# # s = np.identity(5)
# #
# # print(s)
# #
# #
# # j = np.array([[2,4,6]])
# # r1= np.repeat(j,4, axis=0)
# # print(r1)
# #
# #
# # output = np.ones((5,5))
# # print(output)
# #
# #
# # a = np.array([1,2,3])
# # a = np.cos(a)
# # print(a)
# #
# # print('\n')
# # a = np.ones((2,3))
# # print(a)
# #
# # b = np.full((3,2), 2)
# # print(b)
# #
# # c =np.identity(4)
# # d= np.linalg.det(c)
# # print(d)
# #
# #
# # before = np.array([[1,2,3,8], [4,5,6,9]])
# # print(before)
# #
# # after = before.reshape((2,2,2))
# # print(after)
# #
# #
# #
# #
# #
# #
# #
# # v1= np.array([1,2,3,4])
# # v2= np.array([5,6,7,8])
# #
# # v3 = np.hstack((v1,v2))
# # print(v3)
# #
# #
# # print('\n')

# # file = open('games.csv')
# # print(file)
# #
# # line = next(file)
# # print(line)
# #
# #
# #
# # for line in file:
# #     pass
# #
# # print(line)
# #
# # file.close()
# #
# #
# # with open('games.csv') as csv_file:
# #     for line in csv_file:
# #         pass
# #     print(line)
# #
# #
# #
# # my_file= open('TSLA.csv')
# #
# # reader = csv.reader(my_file)
# # print(reader)
# #
# # headers = next(reader)
# # print(headers)
# #
# #
# # headers = next(reader)
# # print(headers)
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# # result_list = []
# # for i in range(1,6):
# #     result_list.append(i)
# #
# #
# # print(result_list)
# #
# # a = [i for i in range(1,8)]
# # print(a)
# #
# #
# #
# # print('\n')
# #
# #
# # df = pd.read_csv('TSLA.csv')
# # print(df.iloc[0:2, 0:3])
# # print(df.index)
# # print(df[['Open', 'Close']])
# #
# #
# # print(df.loc[[1200]])
# #
# # print(df.iloc[[0,2]])
# # print(df.loc[0:5, 'Date':'Close'])
# #
# #
# # print(df.info())
# # print(df.select_dtypes(['category']))
# #
# # arr = np.array([[[2,3,4,5.0], [45,5,53,3.0]], [[12,32,12.0,34], [33,23,21.4,67]]])
# #
# # print(arr)
# # print(arr.shape)
# #
# #
# #
# # l = [3,4,5,6,6]
# # b = np.array((l))
# # print(b)

# # print('\n')
# #
# # style = np.ones((3,4))
# # print(style.diagonal())
# #
# #
# # print('\n')
# #
# #
# #
# # emp = np.eye(7)
# # print(emp)
# #
# # ran = np.arange(0, 10, 3)
# # print(ran)
# #
# #
# #
# # space = np.linspace(1, 100, 20)
# # print(space)
# #
# #
# # x = np.ceil(23.533)
# # print(x)
# #
# #
# # print('\n')
# #
# #
# # a = np.arange(10000)
# # print(a)
# #
# # print('\n')
# #
# #
# #
# #
# # print(np.random.rand(1))
# # print('\n')
# # rand = np.random.randn(4,3)
# # print(rand)
# #
# #
# # print('\n')
# #
# #
# # random_int = np.random.randint(1,50, 16)
# # print(random_int)
# #
# #
# #
# #
# # # basic operations in numpy
# #
# # a = np.array([2,3,3,5])
# # b = np.arange(4)
# #
# # print(a)
# # print(b)
# #
# # print('\n')
# # opr = a < 2
# # print(opr)
# #
# #
# #
# # b = np.arange(12).reshape((4,3))
# # print('\n')
# # print(b[...])
# # print(b)
#
#
# ages_x = [25,26,27,28,29,30,31,32,33,34,35]
# dev_y = [38496,42000,46752,49320,53200,56000, 64928,67317,68748,73752,62316]
#
#
# plt.plot(ages_x, dev_y, color= '#444444', linestyle = '--', label = 'All Devs')
#
#
# py_dev_y = [45372,48876,53850,57287,63016,65998,70003,71496,75370,70000,83640]
#
# plt.plot(ages_x, py_dev_y,  label = 'Python')
#
# js_dev_y = [37810, 43515, 46823, 49293, 53437, 56373, 62375, 66674, 68745, 68746,74583]
#
# plt.plot(ages_x, js_dev_y ,label = 'Javascript')
#
#
# plt.xlabel('Ages')
# plt.ylabel('Median salary (USD)')
#
# plt.title('Median salary (USD) by Age')
#
# plt.legend()
# plt.grid(True)
#
# plt.tight_layout()
#
#
# plt.savefig('plot.png')
# # plt.show()
#
# path = 'TSLA.csv'
# lines = [line for line in open(path)]
#
# print(lines[0].strip().split(','))
#
# dataset = [line.strip().split(',') for line in open(path)]
# print(dataset[1])
#
#
# file = open(path, newline='')
#
# reader = csv.reader(file)
# header = next(reader)
# data = [row for row in reader]
# print(header)
# print(data[0])
#

# condition = True
#
# x = 1 if condition else 0
# print(x)
#
#
# num = 1000000000000
# num2 = 10000000
#
# total = num + num2
# print(f'{total:,.2f}')
#
#
# with  open('text', 'r') as f:
#     file_contents = f.read()
#
#
# words = file_contents.split(' ')
# word_count = len(words)
# print(word_count)
#
#
#
#
#
#
# df = pd.read_csv('./CSV/games.csv')
# print(df)
#
# files = [file for file in os.listdir('./CSV/games.csv')]
#


profile = {
    'name': 'Chima Okoro',
    'age': 23,
    'school': 'UNN'

}

print(profile['name'], 'is ', profile['age'], 'and studied in ', profile['school'])

for value in range(1,5):

    for key, value in profile.items():
        print('\nKey:', key)
        print('value: ', value)

favourite_language= {
    'james':['python', 'java', 'ruby'],
    'chima': ['javascript', 'html', 'css'],
    'uche': ['java', 'node'],
    'neme': ['ruby']
}
for name, languages  in favourite_language.items():
    print(name.title(),"'s favourite languages are ", )

    for language in languages:
        print('\t', language.title())

# for language in set(favourite_language.values()):
#     print(language.title())
# for name in sorted(favourite_language.keys()):
#      print(name.title(), 'Thanks for taking the poll!')
#
# friends = ['chima', 'uche']
# for name in favourite_language.keys():
#     print(name)
#
#     if name in friends:
#         print('Hi', name, 'i see your favourite language is', favourite_language[name])
#


print('\n')


# LEARNING SETS
s1 = {1,2,3}
s2 = {2,3,4}
s3 = {3,4,5}


s4 = s1.symmetric_difference(s2)

print(s4)


l1 = [1,2,3,1,2,3]
l2 = list(set(l1))

print(l2)


employees = ['chima', 'uche', 'kammi', 'isioma', 'jane', 'ibe', 'rashford']

gym_members = ['chima', 'kammi', 'jane']

developers = ['chima', 'uche', 'kammi', 'rashford']


results = set(employees).difference(developers, gym_members)
print(list(results))


if 'chima' in employees and developers:
    print('yessseh')


df = pd.read_csv('/Users/HP/PycharmProjects/MYWORK/CSV/20150512_WomensWorldCupPlayers.csv')

# player = df[['Player', 'Search Interest']]
# print(player)


print(df.loc[ :, ['Player', 'Search Interest'] ])




df2 = pd.DataFrame(np.random.rand(8,8), columns=list('ABCDEFGH'))




df3 = pd.concat([df, df2])
print(df3)


my_list= []
new_list = [2,5,7,9,6,4]

for list in new_list:
    my_list.append(list**2)
print(my_list)


name = 'jesus'
print('God is cood all the time he is the father of {}'.format(name.title()))