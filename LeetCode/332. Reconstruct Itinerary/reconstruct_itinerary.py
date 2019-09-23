# 通过题目，应该要反应出来解法应该是DFS的回溯问题
# 把同一个from的所有to排序来达到取字典序最小的结果。这样DFS的时候遇到的第一个解就是字典序最小的解

# 这是修修改改得出的第一个通过的解
class Solution(object):
    def __init__(self):
        self.result = []
        
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        from collections import defaultdict
        d = defaultdict(list)
        if not tickets:
            return []
        for f, t in tickets:
            d[f].append(t)
        
        for v in d.values():
            v.sort()
        
        
        def visit(it, start):
            if self.result:
                return
            if not d:
                self.result = it
                return 
            if start in d:
                for i, end in enumerate(d[start]):
                
                    if len(d[start])>1:
                        d[start] = d[start][0:i] + d[start][i+1:]
                    else:
                        del(d[start])

                    visit(it + [end], end)
                    d[start] = d[start][0:i]+[end]+d[start][i:]
            return
        
        visit(['JFK'], 'JFK')

        return self.result

# 另一个点是欧拉通路的解法
'''
欧拉通路：遍历所有的边的一条路径
存在的充要条件：
   2个点一个点出度大于入度（起始点），一个点入度大于出度（终止点）
   或 所有点出度=入度（欧拉回路）
欧拉回路：遍历所有的边并回到初始点的一条回路
存在的充要条件：
  所有点出度=入度（欧拉回路）

此题即遍历所有的边的一条路径，并不一定要回到JFC，所以是求欧拉通路问题，用dfs其实就是套圈法：
1、用dfs一延边找点，由于题目说要字典序，就按字典序来找，若找到不能继续往下找的点，记为p，此即为终止点
2、回溯到其上层节点，走别的路，由于p是唯一的终止点，所以再找一定最后可以回来（除p和JFC外其他都出度=入度）
3、不断重复1、2，直到所有边全部遍历
可以模拟一下[["JFK","ATL"],["ATL","SFO"],["SFO","JFK"],["JFK","LAS"],["LAS","ATL"],["ATL","ABC"]]，可以看到这个方法非常巧妙
'''
def findItinerary(self, tickets):
    targets = collections.defaultdict(list)
    for a, b in sorted(tickets)[::-1]:
        targets[a] += b,
    route = []
    def visit(airport):
        while targets[airport]:
            visit(targets[airport].pop())
        route.append(airport)
    visit('JFK')
    return route[::-1]

            
