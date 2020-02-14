# 第四天作业
    给定两个有序整数数组 nums1 和 nums2，将 nums2 合并到 nums1 中，使得 num1 成为一个有序数组。

说明:

初始化 nums1 和 nums2 的元素数量分别为 m 和 n。
你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。
    
第一次使用双指针解法，思路中规中矩，需要用到额外空间存储列表信息：
![image](https://github.com/jasonlbx13/7days_algorithm/blob/master/homework_0214/pic/1.jpg)
第二次参考题解使用逆序的双指针解法，不太好想，但是空间复杂度降到了常数，速度没有提高：
![image](https://github.com/jasonlbx13/7days_algorithm/blob/master/homework_0214/pic/2.jpg)
第三次使用库函数，合并和直接sort排序，虽然写法简洁但是面试可能会禁止这种做法，慎用！
![image](https://github.com/jasonlbx13/7days_algorithm/blob/master/homework_0214/pic/3.jpg)



