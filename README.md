# 来源
https://github.com/Skyorca/NogizakaCrawer
在这个老哥写的爬虫的基础上改动的

# 如何启动
因为是多线程爬虫，通过bash multi_thread.sh启动start.py文件

然后需要在start.py修改line 28里面的idol_url来爬取对应小偶像的博客

在crawer.py最下面的setDir函数里面设置小偶像第一条博客的发布年月

start.py调用crawer.py和translator.py。注意翻译接口有点问题，正在调试，即不能一次性完成写入日文，写入图片，翻译并写入中文三种操作，只能完成前两者。

test.py就是测试函数的集合，主要是看内容格式怎么提取。其他随用随加。

![正在爬取...](https://github.com/Skyorca/NogizakaCrawer/blob/master/crawing.png)

总的来说还有很多bug
有空继续改
