# 第一次遍历记录每个字符最早和最晚出现的位置
# 第二次根据位置对构建分区
class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        appears = {}
        for i, s in enumerate(S):
            if s in appears:
                appears[s] = (appears[s][0], i)
            else:
                appears[s] = (i, i)
    
        ranges = sorted(appears.values())
        ret = []
        if not ranges:
            return ret
        index = 1
        tmp = ranges[0]
        while index < len(ranges):
            if ranges[index][0] > tmp[1]: # 无交集,出现新的分区
                ret.append(tmp[1] - tmp[0] + 1)
                tmp = ranges[index]
            else: # 有交集,扩展分区范围
                tmp = (min(tmp[0], ranges[index][0]), max(tmp[1], ranges[index][1]))
            index += 1
        ret.append(tmp[1] - tmp[0] + 1)
        return ret
        
        
        
        
# leetcode提交之后学到的一个solution
# 先遍历S只记录每个字符最后出现的位置
# 再遍历S,从头开始,开始位置到该字符最后的位置是一个分区,
# 而之间出现的字符又将分区扩展至该字符最后出现的位置

class Solution:
    def partitionLabels(self, S: str) -> List[int]:        
        last = {}
        for idx, char in enumerate(S):
            last[char] = idx
            
        ans = []
        i = 0
        
        while i < len(S):
            start = j = i
            end = last[S[start]]
            while j < end:
                end = max(end, last[S[j]])
                j += 1
            ans.append(S[start:end+1])
            i = end + 1
        
        return [len(a) for a in ans]
