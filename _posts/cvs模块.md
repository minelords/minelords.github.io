## CVS模块写入

#### 1)cvs.writer() 读写序列化数据

writer(cvsfile,dialect='excel',**fmtparams)

- csvfile：必须是支持迭代(Iterator)的对象，可以是文件(file)对象或者列表(list)对象。
- dialect：编码风格，默认为 excel 的风格，也就是使用逗号`,`分隔。
- fmtparam：格式化参数，用来覆盖之前 dialect 对象指定的编码风格。

```
#delimiter 指定分隔符，默认为逗号，这里指定为空格    
# quotechar 表示引用符    
# writerow 单行写入，列表格式传入数据
# writerows 写入多行数据
```

