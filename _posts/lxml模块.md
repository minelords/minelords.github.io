## 了解Xpath

### XPath（全称：XML Path Language）即 XML 路径语言



### 1）基本语法

![image-20231130094625142](C:\Users\zjc6\AppData\Roaming\Typora\typora-user-images\image-20231130094625142.png)



例如：

```xml
<ul class="BookList">
  <li class="book1" id="book_01" href="http://www.biancheng.net/">
        <p class="name">c语言小白变怪兽</p>
        <p class="model">纸质书</p>
        <p class="price">80元</p>
        <p class="color">红蓝色封装</p>
    </li>
  
    <li class="book2" id="book_02" href="http://www.biancheng.net/">
        <p class="name">Python入门到精通</p>
        <p class="model">电子书</p>
        <p class="price">45元</p>
        <p class="color">蓝绿色封装</p>
    </li>
</ul>
```

当需要查找某个特定的节点或者选取节点中包含的指定值时需要使用`[]`方括号

![image-20231130095116716](C:\Users\zjc6\AppData\Roaming\Typora\typora-user-images\image-20231130095116716.png)

### 2）xpath通配符

![image-20231130095224295](C:\Users\zjc6\AppData\Roaming\Typora\typora-user-images\image-20231130095224295.png)



3）多路径匹配

```
xpath表达式1 | xpath表达式2 | xpath表达式3
```



### 3）Xpath内建函数

![image-20231130095430307](C:\Users\zjc6\AppData\Roaming\Typora\typora-user-images\image-20231130095430307.png)



### 4）Xpath helper使用ctrl+shift+x





## lxml第三方库

### 1)导入模块

from lxml import etree

### 2)创建解析对象

parse_html=etree.HTML(html)

### 3)调用xpath表达式

r_list=parse_html.xpath('xpath表达式')

### 4)将元素装换为字符串输出

etree.tostring(html)

```py
html = etree.HTML(html_str)
xpath='//a/text()'
r_list=html.xpath(xpath)
print(r_list)
```