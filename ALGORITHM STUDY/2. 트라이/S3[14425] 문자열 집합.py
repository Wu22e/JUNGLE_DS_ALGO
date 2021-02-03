import sys
input = sys.stdin.readline

class Node(object):
    def __init__(self, key, count = 0):
        self.key = key  # 해당 문자를 key값으로 가진다.
        self.child = {} # 자식들을 Dict에 저장을 한다.

class Trie(object):
    def __init__(self):
        self.head = Node(None) # 처음 Trie가 만들어지면 빈 Node 하나를 head로 만들어 놓는다.

    def insert(self, word):
        cur = self.head

        for ch in word:             # 문자열의 각 문자들을 반복
            if ch not in cur.child: # 해당 문자가 자식 노드에 존재하지 않을 경우 노드를 추가
                cur.child[ch] = Node(ch)
            cur = cur.child[ch]
        cur.child['*'] = True # 문자열의 마지막에 '*'을 삽입.


    def search(self,word):
        cur = self.head

        for ch in word:
            if ch not in cur.child: # 문자열의 각 문자들을 반복
                return False
            cur = cur.child[ch]
        if '*' in cur.child:
            return True

n, m = map(int,input().split())
trie = Trie()


cnt = 0
for _ in range(n):
    trie.insert(input().rstrip())

for _ in range(m):
    if(trie.search(input().rstrip())):
        cnt += 1
print(cnt)
