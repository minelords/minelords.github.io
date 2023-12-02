## Beautiful Soup 是 python 的一个库，最主要的功能是从网页抓取数据。

无论哪种解析器都需要导入BeautifulSoup，即: `from bs4 import BeautifulSoup`

```
from bs4 import BeautifulSoup
soup = BeautifulSoup(markup, "lxml") # 参数位置的markup表示从网络获取的网页页面
soup = BeautifulSoup(markup, "html.parser")  # Python标准库
soup = BeautifulSoup(markup, "html5lib")  # html5lib库
推荐使用lxml作为解析器，因为效率更高。
```

节点对象可以归纳为4种：Tag ，NavigableString ，BeautifulSoup ， Comment

### 1.tag

tag有两个重要的属性name和attrs

```python
soup.a.name # 标签名
soup.a.attr # 标签属性
```

### 2.NavigableString

字符串常被包含在tag内. Beautiful Soup用 NavigableString 类来包装tag中的字符串。

```python
from bs4 import BeautifulSoup
xml_soup = BeautifulSoup('<p class="body strikeout">我是一个段落</p>', 'lxml')
tag = xml_soup.p
print(tag['class']) # 获取class属性值
print(tag.string) # 获取tag中的文本内容
```

### 文档树

![9ebc375f221647464ed7ecf1688525fa](C:\Users\zjc6\Desktop\笔记\Python基础\img\9ebc375f221647464ed7ecf1688525fa.jpg)

### 搜索文档树

1.find_all( name , attrs , recursive , text , **kwargs )：find_all () 方法搜索当前 tag 的所有 tag 子节点，并判断是否符合过滤器的条件

### find()和find_all()的区别

```python
find 返回的是匹配的第一个结果，find_all 返回匹配的所有结果
find 直接将结果返回，find_all 将结果作为一个列表返回
```

### select()

我们在写 CSS 时，标签名不加任何修饰，类名前加点，id 名前加 #，在这里我们也可以利用类似的方法来筛选元素，用到的方法是 soup.select()，返回类型是 list

```
print(soup.select('div'))  # 通过标签选择器查找
print(soup.select('#div1')) # 查找id选择器是div1的标签
print(soup.select('.c1')) # 查找class类选择器是c1的标签
也可以通过组合查找即和写 class 文件时，标签名与类名、id 名进行的组合原理是一样的，例如查找 p 标签中，id 等于 link1 的内容，二者需要用空格分开
print(soup.select('p em'))  # 查找p中em标签
在选择器中查找时还可以加入属性元素，属性需要用中括号括起来，注意属性和标签属于同一节点，所以中间不能加空格，否则会无法匹配到。
print(soup.select("div[data-foo]"))  # 查找有data-foo属性的div标签
select的使用与 find_all 方法有异曲同工之妙的查找方法，是不是感觉很方便？
```

### 一个简单的例子：

```python
import requests
from bs4 import BeautifulSoup
import time
url="http://node5.anna.nssctf.cn:28720"
s = requests.Session()
for i in range(0,20):
    res1 = s.get(url=url)
    soup = BeautifulSoup(res1.text,'html.parser') #HTMLParser是Python内置的专门用来解析HTML的模块
    tags = soup.find_all('div')
    cal = ''
    for tag in tags:
        cal += tag.text
    cal = cal[:-1]
    num = eval(cal)

    data={
        'ans':num
    }
    time.sleep(1)
    res2 = s.post(url=url,data=data)
    print(res2.text)
```
