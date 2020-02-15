class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.cap = k
        self.array = []

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if len(self.array) == self.cap:
            return False
        self.array = [value] + self.array
        return True

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if len(self.array) == self.cap:
            return False
        self.array += [value]
        return True

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if len(self.array) == 0:
            return False
        self.array.pop(0)
        return True

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if len(self.array) == 0:
            return False
        self.array.pop(-1)
        return True

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        if len(self.array) == 0:
            return -1
        return self.array[0]

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        if len(self.array) == 0:
            return -1
        return self.array[-1]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return True if self.array == [] else False

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return True if len(self.array) == self.cap else False