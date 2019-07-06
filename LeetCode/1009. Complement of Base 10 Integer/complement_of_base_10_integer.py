# one line solution
class Solution:
    def bitwiseComplement(self, N: int) -> int:
        return int('0b'+''.join(list(map(lambda x:'0' if x=='1' else '1',bin(N)[2:]))),2)
        

# readable solution
class Solution:
    def bitwiseComplement(self, N: int) -> int:
        binary_str = bin(N).replace('0b','')
        switch = lambda x:'0' if x=='1' else '1'
        new_binary = '0b'+''.join(list(map(switch, binary_str)))
        return int(new_binary, 2)
