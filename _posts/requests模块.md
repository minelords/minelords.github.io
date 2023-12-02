## 常用请求方法

![image-20231129201331385](C:\Users\zjc6\AppData\Roaming\Typora\typora-user-images\image-20231129201331385.png)

### 1)requests.get()

res=requests.get(url,headers=headers,params,timeout,verify)

- url：要抓取的 url 地址。
- headers：用于包装请求头信息。
- params：请求时携带的查询字符串参数。
- timeout：超时时间，超过时间会抛出异常。
- verify: 检查 SSL 证书认证,如果设置为 False 则表示不检查 SSL证书。

### 2)requests.post()

res=requests.post(url,data={请求的字典})



HttpResponse响应对象属性

![image-20231128231947303](C:\Users\zjc6\AppData\Roaming\Typora\typora-user-images\image-20231128231947303.png)



## 代理参数

### 1)代理IP池

### 2)proxies参数

```py
proxies = {
      '协议类型(http/https)':'协议类型://IP地址:端口号'
    }
```

## 用户认证-auth参数

auth=('username','password')