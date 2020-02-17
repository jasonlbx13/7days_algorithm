# 第七天作业
    给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。

最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。

你可以假设除了整数 0 之外，这个整数不会以零开头。
第一次反向遍历数组，加一并判断进位，思路简单但速度有点慢：
![image](https://github.com/jasonlbx13/7days_algorithm/blob/master/homework_0217/pic/1.jpg)
第二次考虑到python长整型不会溢出，直接转换成字符串再转整形加一后转回整形数组：
![image](https://github.com/jasonlbx13/7days_algorithm/blob/master/homework_0217/pic/2.jpg)




