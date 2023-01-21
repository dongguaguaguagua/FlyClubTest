# 川大学子的在线食堂

**符合要求：是一个产品管理网站、注册登录操作、界面美观**

本网站使用Wordpress搭建了一个去中心化的食物评分系统，网页端主要采用PHP，并使用mysql作为数据库。

## 参考图片：

![主页](https://github.com/dongguaguaguagua/FlyClubTest/blob/main/project1/images/1.png)

支持查找、查看菜肴等。

![产品页面](https://github.com/dongguaguaguagua/FlyClubTest/blob/main/project1/images/2.png)

产品可评论、可评分、可上传图片等等。

![评论页面](https://github.com/dongguaguaguagua/FlyClubTest/blob/main/project1/images/3.png)

## 部署教程：(需要mysql和PHP)。

1. 在[xampp官网](https://www.apachefriends.org/index.html)下载并安装xampp。
2. 启动XAMPP的所有服务。此处打开localhost:8080将会看到`apache friends`欢迎页。
3. 登入[localhost:8080/phpmyadmin](localhost:8080/phpmyadmin)新建database数据表。
4. 点击`导入`将database.sql文件导入进mysql数据库。
5. 进入[localhost:8080](localhost:8080)即可看到foodrating。

备注：由于川大食物数据来源不可靠，此处默认替换成[上海财大的食物数据](http://www.rating.icu)。
