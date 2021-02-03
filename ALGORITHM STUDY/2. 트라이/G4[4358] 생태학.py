# EOF 처리하다 막힘
# import collections, sys
# input = sys.stdin.readline
#
# class TrieNode:
#     def __init__(self):
#         self.word = False
#         self.children = collections.defaultdict(TrieNode)
#
# class Trie:
#     def __init__(self):
#         self.root = TrieNode()
#
#     def insert(self, word: str ) -> None:
#         node = self.root
#         for char in word:
#             node = node.children[char]
#         node.word = True
#
#     def search(self, word: str) -> bool:
#         node = self.root
#         for char in word:
#             if char not in node.children:
#                 return False
#             node = node.children[char]
#         return node.word
#
#     def startsWith(self, prefix: str) -> bool:
#         node = self.root
#         for char in prefix:
#             if char not in node.children:
#                 return False
#             node = node.children[char]
#         return True
#
# trie = Trie()
# tree_list = []
# sort_tree = []
# cnt = 0
# # trie.insert("abcd")
# # print(trie.search("abcd"))
#
# while True:
#     try:
#         tree = input().rstrip()
#
#         # sort_tree[]
#         if trie.search(tree):
#             for i in range(len(tree_list)):
#                 if tree_list[i][0] == tree:
#                     tree_list[i][1] += 1
#         else:
#             trie.insert(tree)
#             cnt += 1
#             tree_list.append([tree, cnt])
#             cnt = 0
#
#     except EOFError:
#         break
#
# # print(tree_list)


# 새롭게 EOF 처리해보기 (안댐 ;)
# import collections, sys
# input = sys.stdin.readline
#
# class TrieNode:
#     def __init__(self):
#         self.word = False
#         self.children = collections.defaultdict(TrieNode)
#
# class Trie:
#     def __init__(self):
#         self.root = TrieNode()
#
#     def insert(self, word: str ) -> None:
#         node = self.root
#         for char in word:
#             node = node.children[char]
#         node.word = True
#
#     def search(self, word: str) -> bool:
#         node = self.root
#         for char in word:
#             if char not in node.children:
#                 return False
#             node = node.children[char]
#         return node.word
#
#     def startsWith(self, prefix: str) -> bool:
#         node = self.root
#         for char in prefix:
#             if char not in node.children:
#                 return False
#             node = node.children[char]
#         return True
#
# trie = Trie()
# tree_list = []
# sort_tree = []
# cnt = 0
# # trie.insert("abcd")
# # print(trie.search("abcd"))
#
# for word in sys.stdin:
#     if word == '\n':
#         break
#     tree = word.rstrip()
#     print(tree)
#     if trie.search(tree):
#         for i in range(len(tree_list)):
#             if tree_list[i][0] == tree:
#                 tree_list[i][1] += 1
#             else:
#                 trie.insert(tree)
#                 cnt += 1
#                 tree_list.append([tree, cnt])
#                 cnt = 0
#
# print(tree_list)

from collections import defaultdict
import sys

tree_list = defaultdict(int)
tree_num = 0
for word in sys.stdin:
    if word == '\n':
        break
    tree = word.rstrip()
    tree_list[tree] += 1
    tree_num += 1

sorted_tree_list = sorted(list(tree_list.keys()))
for word in sorted_tree_list:
    print("%s %.4f" %(word, tree_list[word]/tree_num*100))

