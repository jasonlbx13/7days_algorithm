# 第六天作业
    给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
第一次使用双指针法，分别从两端向中间最高柱遍历，若遍历节点下一个小于遍历过程中遇到过的最高节点，则计算高度差并累加：
![image](https://github.com/jasonlbx13/7days_algorithm/blob/master/homework_0216/pic/1.jpg)
第二次参考题解使用动态规划方法，分别向左和向右扫描，用数组记录下扫描的数据，进行遍历并取最小值相加即为结果（如图所示）：
![image](https://github.com/jasonlbx13/7days_algorithm/blob/master/homework_0216/pic/2.jpg)
![image](https://github.com/jasonlbx13/7days_algorithm/blob/master/homework_0216/pic/3.jpg)



