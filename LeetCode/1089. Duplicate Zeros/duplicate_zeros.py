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
            
            
