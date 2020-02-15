# 第五天作业
    设计实现双端队列。
你的实现需要支持以下操作：
	

MyCircularDeque(k)：构造函数,双端队列的大小为k。

	insertFront()：将一个元素添加到双端队列头部。 如果操作成功返回 true。

	insertLast()：将一个元素添加到双端队列尾部。如果操作成功返回 true。
deleteFront()：从双端队列头部删除一个元素。 如果操作成功返回 true。
	
deleteLast()：从双端队列尾部删除一个元素。如果操作成功返回 true。
	
getFront()：从双端队列头部获得一个元素。如果双端队列为空，返回 -1。
	
getRear()：获得双端队列的最后一个元素。 如果双端队列为空，返回 -1。
	
isEmpty()：检查双端队列是否为空。
isFull()：检查双端队列是否满了。



第一次看到需要频繁操作查询头尾节点，自然而然想到了双向链表，写起来有点麻烦但是思路比较清晰：
![image](https://github.com/jasonlbx13/7days_algorithm/blob/master/homework_0215/pic/1.jpg)
第二次利用python的列表结构，简单明了，其中为了在插入节点时避免所有元素后移使时间复杂度到O(n)，使用了空间换时间的小trick：
![image](https://github.com/jasonlbx13/7days_algorithm/blob/master/homework_0215/pic/2.jpg)




