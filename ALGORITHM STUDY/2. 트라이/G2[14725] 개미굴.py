# 블로그보고 성공한 풀이
# import sys
# input = sys.stdin.readline
# 
# class Node(object):
#     def __init__(self, key, count = 0):
#         self.key = key
#         self.child = {}
# 
# class Trie(object):
#     def __init__(self):
#         self.head = Node(None)
# 
#     def insert(self, word):
#         cur = self.head
# 
#         for ch in word:
#             if ch not in cur.child:
#                 cur.child[ch] = Node(ch)
#             cur = cur.child[ch]
#         cur.child['*'] = True
# 
# 
#     def search(self,word):
#         cur = self.head
# 
#         for ch in word:
#             if ch not in cur.child:
#                 return False
#             cur = cur.child[ch]
#         if '*' in cur.child:
#             return True
# 
# n = int(input())
# trie = Trie()
# 
# for i in range(1, n+1):
#     feedInfo = input().split()
#     feedInfo.pop(0)
#     trie.insert(feedInfo)
# 
# def print_ant_cave(len, cur):
#     if '*' in cur.child:
#         return
#     sort_child = sorted(cur.child)
#     for char in sort_child:
#         print('--' * len + char)
#         print_ant_cave(len+1, cur.child[char])
# 
# cur = trie.head
# print_ant_cave(0, cur)
#
# 알고리즘 인터뷰 책보고 구현한 방법

import collections, sys
input = sys.stdin.readline

#트라이의 노드
class TrieNode:
    def __init__(self):
        self.word = False
        self.children = collections.defaultdict(TrieNode)

class Trie:
    def __init__(self):
        self.root = TrieNode()

    # 단어 삽입
    def insert(self, word: str ) -> None:
        node = self.root
        for char in word:
            node = node.children[char]
        node.word = True

    # 단어 존재 여부 판별
    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]

        return node.word

    # 문자열로 시작 단어 존재 여부 판별
    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]

        return True

n = int(input())
trie = Trie()

for i in range(1, n+1):
    feedInfo = input().split()
    feedInfo.pop(0)
    trie.insert(feedInfo)

def print_ant_cave(len, cur):
    if cur.word == True:
        return
    sort_children = sorted(cur.children)
    for char in sort_children:
        print('--' * len + char)
        print_ant_cave(len+1, cur.children[char])

cur = trie.root
print_ant_cave(0, cur)