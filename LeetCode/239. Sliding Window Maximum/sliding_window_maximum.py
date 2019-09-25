# O(n)解,用双向队列
# 我们用双向队列，在遇到新的数的时候，将新的数和双向队列的末尾进行比较，如果末尾的数比新数小，则把末尾的数扔掉，直到该队列的末尾数比新数大或者队列为空的时候才停止。
# 这样，我们可以保证队列里的元素是重头到位的降序。由于队列中只有窗口里的数，就是窗口里的第一大数，第二大数，第三数...。

# 如何保持队列呢。每当滑动窗口的k已满，想要新进来一个数，就需要把滑动窗口最左边的数移出队列，添加新的数。

# 我们在添加新的数的时候，就已经移出了一些数，这样队列头部的数不一定是窗口最左边的数。
# 技巧：我们队列中只存储那个数在原数组的下标。这样可以判断该数是否为最滑动窗口的最左边的数。

class Solution:
    def renew(self, nums, deq, i):
        while deq:
            if nums[deq[-1]] >= nums[i]:
                deq.append(i)
                return
            deq.pop()
        deq.append(i)
        return
            
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        from collections import deque
        deq = deque()
        for i in range(k):
            self.renew(nums, deq, i)
            
        ret = [nums[deq[0]]]
        
        for i in range(k, len(nums)):
            self.renew(nums, deq, i)
            if deq[0] == i - k:
                deq.popleft()
            ret.append(nums[deq[0]])
        return ret
        
            
        


# 最开始的提交
# 最好情况是O(n),最坏情况是O(nk)?
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        
        cur = nums[0:k]
        m = max(cur)
        ret = [m]
        for i in range(1, len(nums) - k + 1):
            if nums[i-1] == m:
                m = max(nums[i:i+k])
            else:
                if nums[i+k-1] > m:
                    m = nums[i+k-1]
            ret.append(m)
        return ret
