<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>scu资源共享站-电影</title>
    <link rel="stylesheet" href="https://cdn.staticfile.org/font-awesome/4.7.0/css/font-awesome.css">
    <style>
        /* unnecessary code */
        table#searchShow{
            width : 1424px;
            /* 只有定义了表格的布局算法为fixed，下面td的定义才能起作用。 */
            table-layout : fixed;
        }
        /*溢出部分样式*/
        td.link{
            width:100px;
            word-break:keep-all;
            white-space:nowrap;
            overflow:hidden;
            text-overflow:ellipsis;
        }
        /* unnecessary code end */
        body{
            margin: 0;
        }
        .head{
            background-color: white;
            height: ;
        }
        .head .container{
            width: 70%;
            margin-left: auto;
            margin-right: auto;
            /*border: 1px solid red;*/
        }
        .head .container .logo{
            float: left;
            display: inline-block;
            padding-top: 40px;
        }
        .head .container .logo1{
            padding: 10px;
            padding-top: 12px;
            display: inline-block;
            text-align: center;
            color: white;
            background: #7a56ae;
            border-radius: 10px;
            border: 2px solid #7a56ae;
            font-size: 25px;
            -webkit-transition-duration: 0.5s;
            transition-duration: 0.5s;
        }
        .head .container .logo1:hover{
            background-color: white;
            color: #7a56ae;
            cursor: pointer;
        }
        .head .container .logo2{
            display: inline-block;
            color: black;
            font-size: 25px;
            font-weight: bold;
            font-family: cursive;
        }
        .head .container .menu{
            float: right;
            display: inline-block;
            width: 70px;
            height: 120px;
            text-align: center;
            line-height: 120px;
            font-size: small;
            -webkit-transition-duration: 0.5s;
            transition-duration: 0.5s;
            font-family: sans-serif;
        }
        .head .container .menu:hover{
            background-color: #e6e6e6;
            color: #7a56ae;
            cursor: pointer;
        }
        .body .container{
            position: relative;
            width: 100%;
            height: 100%;
        }
        .body .container .mask{
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-color: rgba(121, 87, 174, 0.9);
            /*color: #7a56ae;*/
        }
        .body .form{
            margin-top: 20px;
        }
        .body .form .label{
            margin-left: 20px;
            color: white;
            font-size: 30px;
            font-family: sans-serif;
        }
        .body .form .input{
            float: right;
            padding-left: 10px;
            padding-top: 8px;
            margin-left: 10px;
            border-width: 2px;
            border-style: solid;
            border-color: #f2ac61;
            height: 30px;
            width: 400px;
            border-radius: 10px;
            outline-style: none;
            font-family: monospace;
            -webkit-transition-duration: 0.5s;
            transition-duration: 0.5s;
        }
        .body .form .input:focus{
            border-color: lightgreen;
            box-shadow: lightgreen 5px 5px 30px 5px;
        }
        .body .submitButton{
            margin-top: 20px;
            background-color: white;
            color: #f2ac61;
            width: 80px;
            height: 40px;
            font-weight: bold;
            border-radius: 25px;
            border: 2px solid #f2ac61;
            -webkit-transition-duration: 0.5s;
            transition-duration: 0.5s;
        }
        .body .submitButton:hover{
            background-color: #f2ac61;
            color: white;
        }
    </style>
</head>
<body>
    <div class="head">
        <div class="container">
            <div class="logo">
                <div class="logo1" onclick="window.open('https://www.scu.edu.cn/')">scu</div>
                <div class="logo2">资源共享站(电影)</div>
            </div>
            <div class="menu" onclick="window.open('http://scu.getenjoyment.net/movies.php')">
                <i class="fa fa-film fa-lg"></i>
                电影
            </div>
            <div class="menu" onclick="window.open('http://scu.getenjoyment.net/serial.php')">
                <i class="fa fa-video-camera fa-lg"></i>
                电视剧
            </div>
            <div class="menu" onclick="window.open('http://scu.getenjoyment.net/variety_show.php')">
                <i class="fa fa-hand-peace-o fa-lg"></i>
                综艺
            </div>
            <div class="menu" onclick="window.open('http://scu.getenjoyment.net/books.php')">
                <i class="fa fa-book fa-lg"></i>
                书籍
            </div>
            <!--
            <div class="menu" onclick="window.open('http://scu.getenjoyment.net/about.php')">
                <i class="fa fa-info-circle fa-lg"></i>
                关于
            </div> -->
            <div style="clear: both;"></div>
        </div>
    </div>
    <div class="body">
        <div class="container">
            <img src="https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fp2.itc.cn%2Fq_70%2Fimages03%2F20201018%2F8f9322ec8402451aa80a3880ae2a9a72.jpeg&refer=http%3A%2F%2Fp2.itc.cn&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=auto?sec=1668062892&t=59611fee402937e846dda7f670ca3a09" style="width: 100%;">
            <div class="mask"></div>
            <div style="position: absolute;top: 20%;left: 30%;">
                <form action="movies.php?act=insert" method="post">
                    <div class="form">
                        <i style="color: #f2ac61;" class="fa fa-user-circle fa-2x"></i>
                        <span class="label">上传者:</span>
                        <input class="input" type="txt" placeholder="[选填]无需实名" name="name" id="uploaderInput"/>
                    </div>
                    <div class="form">
                        <i style="color: #f2ac61;" class="fa fa-film fa-2x"></i>
                        <span class="label">电影名称:</span>
                        <input class="input" type="txt" name="movieName" placeholder="[必填]请填写影片名" required="required" id="filmNameInput"/>
                    </div>
                    <div class="form">
                        <i style="color: #f2ac61;" class="fa fa-link fa-2x"></i>
                        <span class="label">链接:</span>
                        <input class="input" type="txt" name="link" placeholder="[必填]请填写电影链接" required="required" id="linkInput"/>
                    </div>
                    <div class="form">
                        <i style="color: #f2ac61;" class="fa fa-code fa-2x"></i>
                        <span class="label">提取码:</span>
                        <input class="input" type="txt" placeholder="[选填]链接提取码" name="extractCode" id="extractCodeInput" />
                    </div>
                    <div class="form">
                        <i style="color: #f2ac61;" class="fa fa-file-text-o fa-2x"></i>
                        <span class="label">备注:</span>
                        <input class="input" type="txt" placeholder="[选填]你对影片的评价/你的联系方式" name="notes" id="notesInput"/>
                    </div>
                    <input class="submitButton"type="submit" value="提交" />
                    <!-- <span>网站资源仅供学习，请于24小时内删除</span> -->
                    <div style="clear: both;"></div>
                </form>
            </div>
        </div>
    </div>
    <br>
    <center>
    <div id="load">数据加载中……请稍等</div>
    <div class="wrap">
             <input type='text' value="" id='searchKey' placeholder="搜索……" style="width: 20%"/>
             <input type='button' value="查询" id='searchBtn' />
             <table border=1px id='searchShow'></table>
    </div>
    </center>
    <script src="http://apps.bdimg.com/libs/jquery/2.1.1/jquery.min.js"></script>
    <script>
        linkInput.onkeyup = function autoLoadFilmNameAndExtractCode(){
            var m = document.getElementById("linkInput").value;
            var linkBegin = m.search("http");
            if (linkBegin != -1) {
                var linkEnd = linkBegin;
                while (33 <= m.charCodeAt(linkEnd) && m.charCodeAt(linkEnd) <= 126)
                {
                    linkEnd++;
                }
                document.getElementById("linkInput").value = m.substring(linkBegin,linkEnd);
            }
            var codeBegin = m.search("码");
            if (codeBegin != -1) {
                codeBegin += 2;
                var codeEnd = codeBegin;
                while (33 <= m.charCodeAt(codeEnd) && m.charCodeAt(codeEnd) <= 126)
                {
                    codeEnd++;
                }
                document.getElementById("extractCodeInput").value = m.substring(codeBegin,codeEnd);
            }
        }
        extractCodeInput.onkeyup = function autoLoadFilmNameAndExtractCode2(){
            var m = document.getElementById("extractCodeInput").value;
            var linkBegin = m.search("http");
            if (linkBegin != -1) {
                var linkEnd = linkBegin;
                while (33 <= m.charCodeAt(linkEnd) && m.charCodeAt(linkEnd) <= 126)
                {
                    linkEnd++;
                }
                document.getElementById("linkInput").value = m.substring(linkBegin,linkEnd);
            }
            var codeBegin = m.search("码");
            if (codeBegin != -1) {
                codeBegin += 2;
                var codeEnd = codeBegin;
                while (33 <= m.charCodeAt(codeEnd) && m.charCodeAt(codeEnd) <= 126)
                {
                    codeEnd++;
                }
                document.getElementById("extractCodeInput").value = m.substring(codeBegin,codeEnd);
            }
        }
    </script>
    <?php
    header("Content-Type: text/html;charset=utf-8");
    $connect_mysql = mysqli_connect('fdb24.awardspace.net','3330419_wpress8d3d497c','ftXqhkvScP5ifksgRVkpilCxbveo600Y'); //创建数据库连接
    if(!$connect_mysql){ //如果失败
        die('连接mysql数据库失败'.mysqli_error()); //显示出错误信息
    }
    mysqli_select_db($connect_mysql,"3330419_wpress8d3d497c");
    if($_GET['act'] == 'insert'){
        $sql = "insert into books (name,bookName,link,extractCode,notes) values ('".$_POST['name']."','".$_POST['bookName']."','".$_POST['link']."','".$_POST['extractCode']."','".$_POST['notes']."')";
        if(mysqli_query($connect_mysql,$sql)){
            echo "<script language='javascript'>alert('插入数据成功')</script>";
        }
        else{
            echo "<script language='javascript'>alert('插入数据失败，请联系我')</script>";
        }
    }
    elseif($_GET['act'] == 'delete'){
        $select_deleted_sql = "select * from books where bookName ='".$_GET['bookName']."' LIMIT 1";
        $deleted_sql = mysqli_query($connect_mysql,$select_deleted_sql);
        $row = mysqli_fetch_array($deleted_sql);
        $insert_deleted_sql = "insert into deleted (name,mediaName,link,extractCode,notes) values ('".$row['name']."','".$row['bookName']."','".$row['link']."','".$row['extractCode']."','".$row['notes']."')";
        $sql = "delete from books where bookName = '".$_GET['bookName']."' LIMIT 1";
        if(mysqli_query($connect_mysql,$sql)&&mysqli_query($connect_mysql,$insert_deleted_sql)){
            echo "<script language='javascript'>alert('删除数据成功')</script>";
        }
        else{
            echo "<script language='javascript'>alert('删除数据失败，请联系我')</script>";
        }
    }
    $select_sql = " select * from books ";
    $result = mysqli_query($connect_mysql,$select_sql);
    ?>
    <script>
    let l = [[],[],[],[],[]];

    <?php
    $i=0;
    while($row = mysqli_fetch_array($result)){
        echo "l[0][".$i."]=\"".$row['name']."\";";
        echo "l[1][".$i."]=\"".$row['bookName']."\";";
        echo "l[2][".$i."]=\"".$row['link']."\";";
        echo "l[3][".$i."]=\"".$row['extractCode']."\";";
        echo "l[4][".$i."]=\"".$row['notes']."\";\n";
        $i++;
    }
    ?>
    document.getElementById('load').innerHTML="<p>加载成功</p>";

    function Fuzzysearch(l){

      this.l = l,//请求得到的数据
      this.searchKey = document.getElementById('searchKey'),//查询关键字
      this.searchBtn = document.getElementById('searchBtn'),//查询按钮
      this.searchShow = document.getElementById('searchShow')//显示查询结果的表格

      this.renderTab(this.l);
      this.init();
    }

    Fuzzysearch.prototype={
          init :function(){
            let _this = this;
            //键入触发事件
            _this.searchKey.onkeyup=function(e){
                var e = e || event;
                if(e.keyCode == 13) {
                  let searchResult = _this.searchFn();
                  _this.renderTab(searchResult);
                }
            };
            //点击查询按钮触发事件
            _this.searchBtn.onclick=function(){
                let searchResult = _this.searchFn();
                _this.renderTab(searchResult);
            };


          },
          searchFn:function(){
            var keyWord = this.searchKey.value;
            var len = this.l[1].length;
            var arr = [[],[],[],[],[]];
            var reg = new RegExp(keyWord);
            for(var i=0;i<len;i++){
                //如果字符串中不包含目标字符会返回-1
                if(this.l[1][i].match(reg)){
                    arr[0].push(l[0][i]);
                    arr[1].push(l[1][i]);
                    arr[2].push(l[2][i]);
                    arr[3].push(l[3][i]);
                    arr[4].push(l[4][i]);
                }
            }
            return arr;
          }
          ,renderTab:function(list){
                let colStr = '';

                if(list[1].length==0){
                  this.searchShow.innerHTML='未查询到关键字相关结果';
                  return;
                }
                colStr+="<tr><th style=\"width:5.2%\">分享者</th><th style=\"width:30%\">书籍名称</th><th style=\"width:30%\">网盘链接</th><th style=\"width:5%\">提取码</th><th style=\"width:26.8%\">备注</th><th style=\"width:3%\">操作</th></tr>";
                for(var i=list[1].length-1; i>=0; i--){
                     colStr+="<tr><td style=\"width:5.2%\">"+list[0][i]+"</td><td style=\"width:30%\">"+list[1][i]+"</td><td style=\"width:30%\" class=\"link\"><a href=\""+list[2][i]+"\">"+list[2][i]+"</a></td><td style=\"width:5%\">"+list[3][i]+"</td><td style=\"width:26.8%\">"+list[4][i]+"</td><td style=\"width:3%\"><input type=\"button\" value=\"删除\" onclick=\"window.location.href='http://scu.getenjoyment.net/books.php?act=delete&bookName="+list[1][i]+"'\"></td></tr>";
                }
                this.searchShow.innerHTML = colStr;
          }
    }

    new Fuzzysearch(l);
    </script>
</body>
</html>

