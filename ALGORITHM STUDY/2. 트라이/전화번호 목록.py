import sys
input = sys.stdin.readline

class Node(object):
    def __init__(self, key, count = 0):
        self.key = key
        self.child = {}

class Trie(object):
    def __init__(self):
        self.head = Node(None)

    def insert(self, word):
        cur = self.head

        for ch in word:
            if ch not in cur.child:
                cur.child[ch] = Node(ch)
            cur = cur.child[ch]
        cur.child['*'] = True


    def search(self,word):
        cur = self.head

        for ch in word:
            if ch not in cur.child:
                return False
            cur = cur.child[ch]
        if '*' in cur.child:
            return True

testcase = int(input())

for i in range(testcase):
    n = int(input())
    for j in range(n):


trie = Trie()
trie.insert('hooong')
print(trie.search('hooong'))