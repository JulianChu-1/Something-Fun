# WangYiyun-Music-Comment-Spider
## 使用说明
本次爬取网易云音乐评论的方法主要是使用python+js进行爬取   
所使用的python库主要为seleinum模拟人进行操作
需要修改的地方主要是浏览器driver的配置，CSDN中有具体方法
## 具体思路
具体思路主要为使用python进行模拟点击操作    
利用pyton库中所带的execute_script方法执行js代码爬取相应的数据并以json格式传出
最后使用pandas等进行数据简单的处理
