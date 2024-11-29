## HTML(Hyper Text Markup Language)
用特殊的标记把需要展示的东西标记出来

超文本：文本，图片，音乐

语法规则：
1. <标记> 需要标记的内容 </标记>
2. <标记/>
3. h系列标签:号越大字越小
4. 在html中想要换行：两个方案
   - 选择自己独占一行的标签
   - 加入 "《br/》"标签
   - 段落标签 "《p》" 有外边距
5. 列表：ol(ordered list)，ul(unordered list),
dl()
- 正常情况下，ol和ul里边放的是li，列表里的东西 
- dl里边放的是dt和dd

6. 超文本标记 
- 超链接
- target:链接展示的方式
  -  _blank:在新窗口展示
  - _self:在当前窗口展示
- href: 超链接的跳转url，有可能是绝对地址或者相对地址

- 图片
 - src:图片地址
 - width/height：宽和高

7. table 

        <table border="10">
            <!-- table row 行-->
            <tr>
                <!-- table data 单元格1-->
                <td>葫芦爷爷</td>
                <td>张无忌</td>
            </tr>
            <tr>
                <!-- table data 单元格2-->
                <td>葫芦爷爷2</td>
                <td>张无忌2</td>
            </tr>
        </table>
在浏览器中的元素中，渲染过程中会加入<tbody>,爬虫爬到的是页面的源代码，而不是浏览器渲染的代码elements。

以前的完整代码：

      <table border="10">
            <!-- table head 表头-->
            <thead>
                <tr>
                    <th>1</th>
                    <th>2</th>
                    <th>3</th>
                </tr>
            </thead>
            <!-- table body -->
            <tbody>
                <!-- table row 行-->
                <tr>
                    <!-- table data 单元格1-->
                    <td>葫芦爷爷</td>
                    <td>张无忌</td>
                    <td>333</td>
                </tr>
                <tr>
                    <!-- table data 单元格2-->
                    <td>葫芦爷爷2</td>
                    <td>张无忌2</td>
                    <td>3eee</td>
                </tr>
            </tbody>
        </table>

8. 表单
默认情况下采用get提交，get提交的特点是在url可以看到所有参数。如果不希望看到内容
可以改成post提交。
   
         <form action = "http://www.baidu.com" method = "post/get">
            用户名：<input type="text" name="username"/><br/>
            密码 :  <input type="password" name="pwd"/><br/>
            性别 :
            男 <input type ="radio" name = "gender"/>
            女 <input type ="radio" name = "gender"/><br/>
            爱好：
            <input type = "checkbox" name = "hobby"/> 篮球
            <input type = "checkbox" name = "hobby"/> 足球
            <input type = "checkbox" name = "hobby"/> 橄榄球
            <input type = "checkbox" name = "hobby"/> 网球  <br/>
                家庭地址：
                  <select name="address">
                      <option>北京</option>
                      <option>上海</option>
                      <option>西安</option>
                  </select> <br/>
                  个人说明：
                  <textarea rows="10" cols ="10"></textarea>
                  <input type = "submit" value = "注册">
         </form>

9. div标签和span标签

   两个素标签，没有功能，可塑性很强

   div：块级元素，独占一行
   span：行级元素，默认不独占一行
   
   div和span必须搭配css来使用

## CSS(层叠样式表)
使用css的三种方式
 css样式本身的语法规则
   属性：值;
   属性：值1 值2 值3;

1. 直接在标签上使用style，在style中给出样式的内容

2. 在html中添加style，然后在style中选择div


     <style>
            /标签选择器/
            div{
                background:pink;
                width:100px;
                height:100px;
            }
            /*类选择器/
            .dd{
                background:red;
                width:100px;
            }
            /* id选择器 /
            #德云社2{
                background:green;
            }
        </style>


      <style>
            /* 空格表示section里边的所有span /
             section span{
               color:red;
             }
            /* 只需要一层的span/
            section > span {
               color:green;
            }
      </style>

3. 属性选择器

         <head>
           <style>
             /* 属性选择器 /
             div[qiguai = "sss"]{
               color:red;
             }
      
           </style>
         </head>
         <body>
           <div qiguai = "sss">11111</div>
           <div >12</div>
           <div >11122211</div>
         </body>



##  