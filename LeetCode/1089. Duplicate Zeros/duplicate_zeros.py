class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        index = 0
        l = len(arr)
        while index < l:
            if not arr[index]:
                arr.insert(index, 0)
                index += 1
            index += 1
        while len(arr) > l:
            arr.pop()
            
            
# solution - not using python list.insert()
# much slower, shows that the python list.insert() is well designed
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        i = 0
        l = len(arr)
        while i < l:
            if not arr[i]:
                j = l - 1
                while j > i:
                    arr[j] = arr[j - 1]
                    j -= 1
                i += 1
                    
            i += 1
        while len(arr) > l:
            arr.pop()
