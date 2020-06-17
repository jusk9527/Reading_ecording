### 导读

由于django、flask 都使用了wsgi，我们看下wsgi标准是如何实现的



### 实验环境

> python 3.6+windows7

#### socket测试


```
python sock.py
```


![](https://raw.githubusercontent.com/jusk9527/images/master/data/20191225164528.png)

![](https://raw.githubusercontent.com/jusk9527/images/master/data/20191225164456.png)



#### 使用官方库测试

```
python wsgi01.py
```

![](https://raw.githubusercontent.com/jusk9527/images/master/data/20191225164811.png)


![](https://raw.githubusercontent.com/jusk9527/images/master/data/20191225164742.png)


#### 自己动手实现一个wsgi服务器


```
python server.py
```


![](https://raw.githubusercontent.com/jusk9527/images/master/data/20191225161901.png)


![](https://raw.githubusercontent.com/jusk9527/images/master/data/20191225164124.png)



#### 总结
本质：其实一个 wsgi server 的重要之处就在于用environ去跑 web app 得到返回结果这一步，

参考资料：

https://cizixs.com/2014/11/08/understand-wsgi/

https://juejin.im/entry/5754ece97db2a20069902655

