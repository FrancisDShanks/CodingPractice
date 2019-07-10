class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace('.','[.]')
        
class Solution:
    def defangIPaddr(self, address: str) -> str:
        return '[.]'.join(address.split('.'))
        
class Solution:
    def defangIPaddr(self, address: str) -> str:
        import re
        return re.sub('\.', '[.]', address)
