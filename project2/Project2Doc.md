# 项目二

## 版1 川大资源共享站

**符合要求：自己设计的前端项目、增删操作、界面美观**

## 开源说明

[川大资源共享站](http://scu.getenjoyment.net) <- 这是部署在服务器上的资源共享站

`flyClubTest/project2`中存放的是它的源码，但是mysql数据库仍然在云端，所以**本地不可见电影资源数据**。

[川大资源共享站](http://scu.getenjoyment.net)旨在让大家互利共赢，分享自己收藏的影视产品，让找电影、找电视剧变得更加轻松。每一位访问网站的人都可以在上面**添加/删除**链接。（非常符合互联网精神不是吗）

### 技术原理

1. 采用PHP后端，因此部署需要PHP环境。
2. 所有数据都缓存在二维数组l中，便于搜索。
3. 使用的是mysql数据库管理，并且电影、电视剧、综艺和书籍用的是不同的表。
4. 修改每一条数据后都会更新数据库。
5. 搜索部分是逐字搜索的，由于数据量较大，因此不会实时更新结果，需要点击搜索按钮。
6. 我在PHP代码中链接了云端的数据库，可以将所有资源加载出来。

### 页面截图

![添加电影](https://github.com/dongguaguaguagua/FlyClubTest/blob/main/project2/images/page1.png)

![资源页面](https://github.com/dongguaguaguagua/FlyClubTest/blob/main/project2/images/page2.png)

![查找电影](https://github.com/dongguaguaguagua/FlyClubTest/blob/main/project2/images/page3.png)

（友情链接：[上海财经大学资源共享站](http://sufe.getenjoyment.net/serial.php)）

## 版2 Unicode工具

**符合要求：自己设计的前端小项目、界面美观**

由于源代码我已经开源到了 [GitHub](https://github.com/dongguaguaguagua/unicode)，在这里就不放源码了。

### 技术原理

1. 主要使用JavaScript实现Unicode码的相互转换逻辑，HTML+CSS实现界面
2. 界面的动画是纯CSS实现，包括按钮的涟漪效果
3. 本项目的Feature在于，通过巧妙使用零宽字符
    - 生成加密文本
    - 生成暗语（文字水印）
    - 绕过regex屏蔽
4. `clipboard.min.js`不是我写的，使用开源js完成复制任务。
5. 绕过regex屏蔽主要依靠字符之间夹杂不可见的零宽字符。

### 页面截图

![unicode和字符串相互转换、反屏蔽文本](https://github.com/dongguaguaguagua/FlyClubTest/blob/main/project2/images/unicodePage1.png)

![加密解密文本](https://github.com/dongguaguaguagua/FlyClubTest/blob/main/project2/images/unicodePage2.png)

这里提供加密解密函数。可知，使用5进制和5个零宽字符来实现隐藏一段文本。

```javascript
function encode(){
    const str = "\u200e\u200f\u200c\u200d\ufeff";
    var vis = document.getElementById("visibleInput").value;
    var hid = document.getElementById("hidenInput").value;
    var result = ""
    for (var i = 0; i < hid.length; i++) {
        var tmp = hid.charCodeAt(i);
        var oneLetter = "";
        while (tmp > 0){
            oneLetter = str[tmp % 5] + oneLetter;
            tmp = (tmp - tmp % 5) / 5;
        }
        result = result + oneLetter;
        if (i != hid.length - 1){
            result += "\u200b";
        }
    }
    document.getElementById("encodedText").innerHTML = vis[0] + result + vis.slice(1);
}
function decode(){
    var str = document.getElementById("encodedInput").value;
    var hid = "";
    var vis = "";
    for (var i = 0; i < str.length; i++) {
        if (str[i] == '\u200b' || str[i] == '\u200c' || str[i] == '\u200d' || str[i] == '\u200e' || str[i] == '\u200f' || str[i] == '\ufeff'){
            hid = hid + str[i];
        }else{
            vis = vis + str[i];
        }
    }
    var letters = hid.split('\u200b');
    // console.log(letters);
    for (var i = 0; i < letters.length; i++) {
        var charCode = 0;
        for (var j = 0; j < letters[i].length; j++) {
            if (letters[i][j] == '\u200e'){
                charCode = charCode * 5 + 0;
            }
            if (letters[i][j] == '\u200f'){
                charCode = charCode * 5 + 1;
            }
            if (letters[i][j] == '\u200c'){
                charCode = charCode * 5 + 2;
            }
            if (letters[i][j] == '\u200d'){
                charCode = charCode * 5 + 3;
            }
            if (letters[i][j] == '\ufeff'){
                charCode = charCode * 5 + 4;
            }
        }
        hid = hid + String.fromCharCode(charCode);
    }
    document.getElementById("visibleText").innerHTML = vis;
    document.getElementById("hidenText").innerHTML = hid;
}
```
