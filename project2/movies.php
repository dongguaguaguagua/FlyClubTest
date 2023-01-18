<?php
header("Content-Type: text/html;charset=utf-8");
$connect_mysql = mysqli_connect('fdb24.awardspace.net','3330419_wpress8d3d497c','ftXqhkvScP5ifksgRVkpilCxbveo600Y'); //创建数据库连接
if(!$connect_mysql){ //如果失败
    die('连接mysql数据库失败'.mysqli_error()); //显示出错误信息
}
mysqli_select_db($connect_mysql,"3330419_wpress8d3d497c");
if($_GET['act'] == 'insert'){

    $sql = "insert into movies (name,movieName,link,extractCode,notes) values ('".$_POST['name']."','".$_POST['movieName']."','".$_POST['link']."','".$_POST['extractCode']."','".$_POST['notes']."')";
    if(mysqli_query($connect_mysql,$sql)){
        echo "插入数据成功";
    }
    else{
        echo "插入数据失败，请联系我";
    }
}
elseif($_GET['act'] == 'delete'){
    $select_deleted_sql = "select * from movies where movieName ='".$_GET['movieName']."' LIMIT 1";
    $deleted_sql = mysqli_query($connect_mysql,$select_deleted_sql);
    $row = mysqli_fetch_array($deleted_sql);
    $insert_deleted_sql = "insert into deleted (name,mediaName,link,extractCode,notes) values ('".$row['name']."','".$row['movieName']."','".$row['link']."','".$row['extractCode']."','".$row['notes']."')";
    $sql = "delete from movies where movieName = '".$_GET['movieName']."' LIMIT 1";
    if(mysqli_query($connect_mysql,$sql)&&mysqli_query($connect_mysql,$insert_deleted_sql)){
        echo "删除数据成功";
    }
    else{
        echo "删除数据失败，请联系我";
    }
}
$select_sql = " select * from movies ";
$result = mysqli_query($connect_mysql,$select_sql);

?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>sufe资源共享站-电影</title>
</head>
<style>

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

</style>
<body>
    <center>
    <h1>欢迎来到SUFE资源共享站</h1>
    <a href="http://sufe.getenjoyment.net">首页</a>
    <a href="http://sufe.getenjoyment.net/movies.php">电影</a>
    <a href="http://sufe.getenjoyment.net/serial.php">电视剧</a>
    <a href="http://sufe.getenjoyment.net/variety_show.php">综艺</a>
    <a href="http://sufe.getenjoyment.net/books.php">书籍</a>
    <form action="movies.php?act=insert" method="post">
        <br>上传者
         <input type="txt" name="name" />
        <br>电影名称
         <input type="txt" name="movieName" required="required"/>
        <br>链接
         <input type="txt" name="link" />
        <br>提取码
         <input type="txt" name="extractCode" />
        <br>备注
         <input type="txt" name="notes" />
         <input type="submit" value="提交" />
     </form>
     <div id="load">数据加载中……请稍等</div>
     <br>
     <div class="wrap">
              <input type='text' value="" id='searchKey' placeholder="搜索……" style="width: 20%"/>
              <input type='button' value="查询" id='searchBtn'/>
              <br>
              <table border=1px id='searchShow'></table>
     </div>
     <br>
     </center>
</body>
<script src="http://apps.bdimg.com/libs/jquery/2.1.1/jquery.min.js"></script>
<script>
let l = [[],[],[],[],[]];
<?php
$i=0;
while($row = mysqli_fetch_array($result)){
    echo "l[0][".$i."]=\"".$row['name']."\";";
    echo "l[1][".$i."]=\"".$row['movieName']."\";";
    echo "l[2][".$i."]=\"".$row['link']."\";";
    echo "l[3][".$i."]=\"".$row['extractCode']."\";";
    echo "l[4][".$i."]=\"".$row['notes']."\";\n";
    $i++;
}
?>
document.getElementById('load').innerHTML="加载成功";
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
            colStr+="<tr><th style=\"width:5.2%\">分享者</th><th style=\"width:30%\">电影名称</th><th style=\"width:30%\">网盘链接</th><th style=\"width:5%\">提取码</th><th style=\"width:26.8%\">备注</th><th style=\"width:3%\">操作</th></tr>";
            for(var i=0,len=list[1].length;i<len;i++){
                 colStr+="<tr><td style=\"width:5.2%\">"+list[0][i]+"</td><td style=\"width:30%\">"+list[1][i]+"</td><td style=\"width:30%\" class=\"link\"><a href=\""+list[2][i]+"\">"+list[2][i]+"</a></td><td style=\"width:5%\">"+list[3][i]+"</td><td style=\"width:26.8%\">"+list[4][i]+"</td><td style=\"width:3%\"><input type=\"button\" value=\"删除\" onclick=\"window.location.href='http://sufe.getenjoyment.net/movies.php?act=delete&movieName="+list[1][i]+"'\"></td></tr>";
            }
            
            this.searchShow.innerHTML = colStr;
      }

}

 new Fuzzysearch(l);
</script>
</html>

