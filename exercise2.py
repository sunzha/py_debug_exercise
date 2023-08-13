from typing import Generic
import unittest
from data_structures.referential_array import ArrayR, T
from data_structures.queue_adt import CircularQueue

class DynCircularQueue(CircularQueue, Generic[T]):
    """ Circular queue which dynamically expands when full
    """
    DEFAULT_MAX_CAPACITY = 20

    def __init__(self, max_capacity: int = DEFAULT_MAX_CAPACITY) -> None:
        super().__init__(max_capacity)

    def append(self, item: T) -> None:
        """ Adds an element to the rear of the queue, if the queue is full, 
        it expands the length of the storage array by two. 
        
        :Input:
            item (T): The item to append
        
        :Complexity: O(1) if the self is not full 
                else O(N) where N is the number of elements in the queue
        """
        if self.is_full():
            self.expand()
        super().append(item)

    def expand(self) -> None:
        """ Expands the available size of the queue by a factor of 2
        
        
        :Complexity: O(N) where N is the number of elements in the queue
        """
        new_arr = ArrayR(len(self.array)*2)
        for i in range(len(self.array)):
            new_arr[i] = self.serve()
        
        self.array = new_arr
        self.front = 0
        self.rear = len(self)
