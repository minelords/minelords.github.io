```py
创建目录
dict = 'C:/Users/zjc6/Desktop/image/{}/'.format(word)
if not os.path.exists(dict):
    os.makedirs(dict)
```