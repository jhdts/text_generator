# # a = [int(n) for n in input().split(" ")]
# # for i in range(len(a) - 1):
# #     for j in range(len(a) - i - 1):
# #         if a[j] > a[j + 1]:
# #             a[j], a[j + 1] = a[j + 1], a[j]
# # print(a)
# import numpy as np
#
# text = open('che.txt').read()
# # text = open('example.txt').read()
# words = text.split()
#
# # print('words:')
# # print(words)
#
# def pairs_gen(words):
#     for i in range(len(words) - 1):
#         yield words[i], words[i + 1]
#
# pairs = pairs_gen(words)
#
# # print('pairs =', pairs)
#
# dictionary = {}
# rome = ["XI"]
# # почитать про регулярные выражения OR regular expressions OR regexp
# for w1, w2 in pairs:
#     if w1.isdigit() or w2.isdigit():
#         continue
#     if w1.find('"') != -1 or w2.find('"') != -1:
#         continue
#     if w1 in dictionary.keys():
#         dictionary[w1].append(w2)
#     else:
#         dictionary[w1] = [w2]
#
# # print('dictionary:', dictionary)
#
# first_word = np.random.choice(words)
# while first_word.islower():
#     first_word = np.random.choice(words)
# new_text = [first_word]
#
# i = 0
# while i < 150 or i > 149 and new_text[-1][-1] != ".":
#     if new_text[-1] in dictionary.keys():
#         new_text.append(np.random.choice(dictionary[new_text[-1]]))
#     else:
#         break
#     i += 1
#
#
# print(' '.join(new_text))
import markovify

text = open('che.txt').read()
new_text = markovify
