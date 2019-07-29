# solution - 1, implement trie tree with defaultdict
from collections import defaultdict
Trie = lambda: defaultdict(Trie)

class StreamChecker:

    def __init__(self, words: List[str]):
        self.Trie = Trie()
        for word in words:
            cur = self.Trie
            for c in word:
                cur = cur[c]
            cur['end'] = True
        self.trie_nodes = [self.Trie] # 维护已经有匹配的前缀结点
        

    def query(self, letter: str) -> bool:
        tmp = self.trie_nodes
        self.trie_nodes = [self.Trie] # 保持Trie跟在里面(代表从头匹配)
        flag = False
        for node in tmp:
            if letter not in node: 
                continue
            self.trie_nodes.append(node[letter])
            if 'end' in node[letter]:
                flag = True # 标记flag而不是马上返回,要过完所有tmp
        return flag
                
        


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)


# solution - 2
# a concise and fast solution learned from leetcode discussion
# trie is too heavy in this problem - 杀鸡用牛刀了
class StreamChecker:

    def __init__(self, words: List[str]):
        self.s = ''
        self.dic = collections.defaultdict(set)
        for w in words:
            self.dic[w[-1]].add(w)
                

    def query(self, letter: str) -> bool:
        self.s += letter
        return any(self.s.endswith(w) for w in self.dic[letter])
