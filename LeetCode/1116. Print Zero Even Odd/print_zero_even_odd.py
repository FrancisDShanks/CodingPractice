# this is my original solution
# I tested many many times in my PC, it works perfect, no error
# but when I submit it to oj, it always raise error and the error test case always change
# everytime I test the test case with error in my PC I got correct result
from threading import Semaphore
class ZeroEvenOdd(object):
    def __init__(self, n):
        self.n = n
        self.semaphore = [Semaphore(0), Semaphore(0), Semaphore(0)]
        self.semaphore[0].release()  # print zero first
        self.cnt = 0
        
	# printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        while self.cnt < self.n:
            if self.semaphore[0].acquire() and self.cnt <= self.n:
                printNumber(0)
                self.cnt += 1
                self.semaphore[1].release()
                self.semaphore[2].release()
        
        
        
    def even(self, printNumber: 'Callable[[int], None]') -> None:
        while self.cnt < self.n:
            if self.semaphore[1].acquire():
                if self.cnt % 2 == 0:
                    printNumber(self.cnt)
                    self.semaphore[0].release()
                
        
        
    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        while self.cnt < self.n:
            if self.semaphore[2].acquire():
                if self.cnt % 2 == 1:
                    printNumber(self.cnt)
                    self.semaphore[0].release()
     
     
     
     
                    
# this solution is what I used to pass the oj
# I modified my original based on post from Internet
from threading import Semaphore
class ZeroEvenOdd(object):
    def __init__(self, n):
        self.n = n
        self.semaphore = [Semaphore(0), Semaphore(0), Semaphore(0)]
        self.semaphore[0].release()  # print zero first
        self.cnt = 0
        
	# printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        for _ in range(self.n):
            self.semaphore[0].acquire()
            printNumber(0)
            self.cnt += 1
            if self.cnt % 2 == 0:
                self.semaphore[1].release()
            else:
                self.semaphore[2].release()
       
        
    def even(self, printNumber: 'Callable[[int], None]') -> None:
        for _ in range(self.n//2):
            self.semaphore[1].acquire()
            printNumber(self.cnt)
            self.semaphore[0].release()       
        
    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        for _ in range((self.n+1)//2):
            self.semaphore[2].acquire()
            printNumber(self.cnt)
            self.semaphore[0].release()
# the core idea is the same with my original solution
