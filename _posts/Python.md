# 语法

## 字符串

### 字符串拼接

![35e1d7ceb2774c34a2353a89f23bd45d.png](./img/bb0ab53ab5356c1979f1518858000092.png)

### 字符串格式化



### 字符串打印

print(x,end='')  `end=''`不换行

#### 1.占位符

![截图](./img/8d4823404e0c418fcbd1db205cc743aa.png)

![40013b5f107d4b3995faed98c3aa1073.png](./img/168c2065e1d8d8ecf45d073e6f4a3836.png)

#### 2.精度

> %5.2f：表示将宽度控制为5，将小数点精度设置为2 。

#### 3.快速格式化

![b30efaada225428ea7fdc429acd3d71b.png](./img/4e6cba97102a7793c0e0786aba870a40.png)

<br/>

## range语句

![截图](./img/bc3fa57ed023c5fbd170788289763460.png)

***

# 数据容器

## 列表list

![截图](./img/408f7a407751df5b84164b7199962472.png)

<br/>

## 元组tuple

![截图](./img/ee88e2c73a5fc34c05f6bdac155dcc9a.png)

> 元组不可修改，但是元组里的列表可以修改

<br/>

## 字符串

![截图](./img/e3e7f0a48fc945bcf9b5b86dd29f6837.png)

> 字符串只可以存储字符串，不可以修改字符串。

<br/>

## 序列的切片

序列[起始下标:结束下标:步长]

步长为1表示一个一个取，步长为负表示反向取

<br/>

## 集合

不允许重复元素存在，无序存储

用set()定义空集合

![截图](./img/cf14624744627c16ccabf232e3076bb1.png)

<br/>

## 字典

内容可以修改和添加

> 储存键值对    {key : value}

![截图](./img/62f4d34081a5a911f893151046f6f729.png)

<br/>

## 数据容器总结

![截图](./img/4ebea7fe10af56f903066b63b6730392.png)

<br/>

## 数据容器操作

![截图](./img/97f042fce460b4a5ee5ed4af079c39a5.png)

> 字典除了转换成本身和字符串value不会丢失，其他情况都会

### 排序

sorted(容器,[reverse=True])  //reverse:倒序

***

# 函数

## 函数的多种参数形式

### 1.位置参数

根据位置传参

### 2.关键字参数

根据`键=值`形式传参，顺序不限

### 3.缺省参数

使用默认的参数必须定义在最后

### 4.不定长参数

1.位置不定长以`*`号标记，以元组的形式接收参数

2.关键字不定长以`**`号标记，以字典的形式接收参数

## 函数作为参数传递

## lambda匿名函数

格式：`lambda 传入参数 :  函数体`

> 只能一行

```python
def func(computer){
  result=computer(1,2)
  print(result)
}
func(lambda x,y: x+y)  #lambda匿名函数的形式传入
```

***

# 文件操作

![截图](./img/e878d235520df1a34f9a8d55d793481b.png)

## 1.文件读取

### open()打开文件

`f=open('1.txt','r',encoding="UTF-8")`

### read()方法

`f.read(10)`：读取字符

`f.readlines()`：读取行，封装到列表里

`f.readline()`：一次读取一行

### for line in f  循环读取

### close()关闭文件

`f.close()`

### with open()避免忘记close

`with open('1.txt','r',encoding="UTF-8") as f：`

<br/>

## 2.文件写入

`open('1.txt','r',encoding="UTF-8")`

`f.write("hello world")`

`f.flush()`：内容刷新

`close()`带有``flush()`的功能

<br/>

`with open('eggs.txt', 'w', newline='') as f:`

> newline参数：逐行写入，否则会出现空行现象



## 3.文件追加

`open('1.txt','a',encoding="UTF-8")`



# 模块和包

```python
from 模块名 import 功能名 as 别名
```

## 1.自定义模块

```python
if __name__ == "__main__"  #表示当直接执行时才会成立，而被导入的则不行
```

![image-20230920234738667](C:\Users\zjc6\AppData\Roaming\Typora\typora-user-images\image-20230920234738667.png)

## 2.包的自定义

> 包由模块和`__init__.py`

```python
from xxx import xxx  #有多种写法
```

