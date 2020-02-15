class ListNode:

    def __init__(self, x=0):
        """
        Initializa your ListNode and data
        """
        self.prev = None
        self.next = None
        self.val = x


class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.max_cap = k
        self.cap = k
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if self.cap == 0:
            return False
        node = ListNode(value)
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
        self.cap -= 1
        return True

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if self.cap == 0:
            return False
        node = ListNode(value)
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node
        self.cap -= 1
        return True

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """

        if self.cap == self.max_cap:
            return False
        self.head.next = self.head.next.next
        self.head.next.prev = self.head
        self.cap += 1
        return True

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if self.cap == self.max_cap:
            return False
        self.tail.prev = self.tail.prev.prev
        self.tail.prev.next = self.tail
        self.cap += 1
        return True

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        if self.cap == self.max_cap:
            return -1
        return self.head.next.val

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        if self.cap == self.max_cap:
            return -1
        return self.tail.prev.val

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return True if self.cap == self.max_cap else False

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return True if self.cap == 0 else False