## re模块常用方法

#### 1)re.compile() 生成正则表达式对象

regex=re.compile(pattern,flags=0)

- pattern：正则表达式对象。
- flags：代表功能标志位，扩展正则表达式的匹配。

#### 2)re.findall() 匹配字符串内容

re.findall(patteern,string,flags=0)

- pattern：正则表达式对象。
- string：目标字符串。
- flags：代表功能标志位，扩展正则表达式的匹配。

#### 3)regex.findall() 

regex.findall(string,pos,endpos)

- string 目标字符串。
- pos 截取目标字符串的开始匹配位置。
- endpos 截取目标字符串的结束匹配位置。

#### 4)re.split() 切割目标字符串

re.split(pattern,string,flags=0)

- pattern：正则表达式。
- string：目标字符串。
- flags：功能标志位,扩展正则表达式的匹配。

#### 5)re.sub 替换匹配到的内容

re.sub(pattern,replace,string,max,flags=0)

- pattern：正则表达式。
- replace：替换的字符串。
- string：目标字符串。
- max：最多替换几处，默认替换全部，
- flags：功能标志位,扩展正则表达式的匹配。

#### 6)re.search() 匹配第一个符合的内容

re.search(pattern,string,flags=0)

- pattern：正则表达式
- string：目标字符串



### flag功能标志位

![image-20231122102756247](C:\Users\zjc6\AppData\Roaming\Typora\typora-user-images\image-20231122102756247.png)