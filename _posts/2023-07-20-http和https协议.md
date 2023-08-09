---

catalog: true
tags:
    web
    http
---
# HTTP/HTTPS协议

## URI和URL
>URI（Uniform Resource Identifier），翻译为统一资源标识符，是一个用于标识某一互联网资源名称的字符串
>URL（Uniform Resource Location），翻译为统一资源定位符，它描述一台特定服务器上某特定资源的特定位置。

## 响应头
### 常见的
>GET  
>POST  
>HEAD：只请求头部  
>PUT：向指定资源位置上传其最新内容。  
>DELETE：请求服务器删除指定的页面。  
>OPTIONS：返回服务器针对特定资源所支持的 HTTP 请求方法。  
>TRACE：回显服务器收到的请求，主要用于测试或诊断。  
-----------------------
### 少见的
>PATCH：实体中包含一个表，表中说明与该URI所表示的原内容的区别。  
>MOVE：请求服务器将指定的页面移至另一个网络地址。  
>COPY：请求服务器将指定的页面拷贝至另一个网络地址。  
>LINK：请求服务器建立链接关系。  
>UNLINK：断开链接关系。  
>WRAPPED：允许客户端发送经过封装的请求。  

## 状态码 

|200|	ok	|请求成功其后是对GET和POST请求的应答文档|
|:-----|:----------------------:|:---------|
|301|    Moved Permanently|	请求的永久页面跳转|
|403|	Forbidden|	禁止访问该页面|
|404|	Not Found|	服务器无法找到被请求的页面|
|500|	Internal Server Error|	内部服务器错误|
|502|	Bad Gateway|	无效网关|
|503|	Service Unavailable|	当前服务不可用|
|504|	Gateway Timeout|	网关请求超时|

# 客户端发起请求 #
![图片.png](/img/https.png)

## Content-Type:
## Referer：
## User-Agent：
## X-Forwarded-For：
## Cookie和session
>储存用户信息

## Apache Tomcat漏洞 ##
`CVE-2017-12615（远程代码执行漏洞）`





