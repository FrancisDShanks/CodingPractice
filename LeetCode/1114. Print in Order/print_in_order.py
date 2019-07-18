# solution - 1
# using threading.Event to control the flow
from threading import Event
class Foo:
    def __init__(self):
        self.event1 = Event()
        self.event2 = Event()

    def first(self, printFirst):
        printFirst()
        self.event1.set()
        
    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.event1.wait()
        printSecond()
        self.event2.set()

    def third(self, printThird: 'Callable[[], None]') -> None:
        self.event2.wait()
        printThird()
        
        
# solution - 2
# useing threading.Semaphore to act like gates to control the flow
from threading import Semaphore
class Foo:
    def __init__(self):
        # set semaphore to zero, so at beginning everyone is blocked
        self.semaphore = (Semaphore(0), Semaphore(0))

    def first(self, printFirst: 'Callable[[], None]') -> None:
        printFirst()
        self.semaphore[0].release()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        if self.semaphore[0].acquire():
            printSecond()
        self.semaphore[1].release()

    def third(self, printThird: 'Callable[[], None]') -> None:
        if self.semaphore[1].acquire():
            printThird()
        
        
        
# solution - 3
# using Lock
from threading import Lock
class Foo:
    def __init__(self):
        self.locks = [Lock(), Lock()]
        self.locks[0].acquire()
        self.locks[1].acquire()
        
    def first(self, printFirst: 'Callable[[], None]') -> None:
        printFirst()
        self.locks[0].release()

    def second(self, printSecond: 'Callable[[], None]') -> None:    
        if self.locks[0].acquire():
            printSecond()
        self.locks[0].release()
        self.locks[1].release()

    def third(self, printThird: 'Callable[[], None]') -> None:
        if self.locks[1].acquire():
            printThird()
        self.locks[1].release()
        
        
# solution - 4
# using Barrier
from threading import Barrier
class Foo:
    def __init__(self):
        self.barrier = (Barrier(2), Barrier(2))        

    def first(self, printFirst: 'Callable[[], None]') -> None:
        printFirst()
        self.barrier[0].wait()

    def second(self, printSecond: 'Callable[[], None]') -> None:    
        self.barrier[0].wait()
        printSecond()
        self.barrier[1].wait()

    def third(self, printThird: 'Callable[[], None]') -> None:
        self.barrier[1].wait()
        printThird()
        
