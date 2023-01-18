# 川大学子的在线食堂

本网站使用Wordpress搭建了一个去中心化的食物评分系统，网页端主要采用PHP，并使用mysql作为数据库。

参考图片：

![1](https://pic.imgdb.cn/item/63c79cd3be43e0d30e2a71d2.png)
![2](https://pic.imgdb.cn/item/63c79cd3be43e0d30e2a71c6.png)
![3](https://pic.imgdb.cn/item/63c79cd3be43e0d30e2a71bf.png)

部署教程：(需要mysql和PHP)。
1. 在[xampp官网](https://www.apachefriends.org/index.html)下载并安装xampp。
2. 启动XAMPP的所有服务。此处打开localhost:8080将会看到`apache friends`欢迎页。
3. 登入[localhost:8080/phpmyadmin](localhost:8080/phpmyadmin)新建database数据表。
4. 点击`导入`将database.sql文件导入进mysql数据库。
5. 进入[localhost:8080](localhost:8080)即可看到foodrating。

备注：由于川大食物数据来源不可靠，此处默认替换成上海财大的食物数据，具体网站可见[foodrating](http://www.rating.icu)
