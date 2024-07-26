### 1 解释性语言和编译型语言的区别
解释性语言：把源程序翻译一句，执行一句，直到结束。 例如python

编译型语言：把源程序全部编译为二进制的可运行程序，然后直接运行。如C，cpp

### 2. python中的数据结构
1. 字符串：引号包含的任意文本
2. 列表：有序集合，可以添加和删除元素
3. 元组：有序集合，元组中的数字无法修改，即不可变
4. 字典：无序集合，由键值对组成。
5. 集合：是一组key的集合，每个元素都唯一

### 3.上述类型的常用方法：
1. 字符串：
   1. 切片
   2. join：可以用来连接字符串 ，将字符串，元组，列表中的元素以指定的字符连接
   3. replace(old,new,count):将字符串old换成new
   4. split():默认以空格进行分割

2. 列表：
   1. 切片，同字符串
   2. append：直接添加，哪怕是列表也会加入进入。
      extend：在当前列表的前提下，扩展列表的元素
   3. 删除：del:根据下标
            pop：删除最后一个
            remove：根据值删除
   4. sort排序：默认由小到大，参数reverse改为True可改为由大到小
   5. reverse：列表倒置

3. 字典：
   1. 清空：clear
   2. pop('key):清除一个key
   3. 遍历：【key for key in dict2],
            [value for value in dict2.values()],
            [(k,v)) for k,v in dict2.items()]
   4. fromkeys 用于创建一个新的字典，以序列中元素作为字典的建，value为字典中建对应的初始值

### 4.python中的字符串编码
Unicode编码把所有的语言都编码到一套编码系统中，在python中可以用encode()的方法
进行编码，也可以用decode()来吧bytes编码成字符串。

    bytes = '您好'.encode('utf-8')
    str = bytes.decode('utf-8')

### 5.一行实现数值交换

    a，b = 1,2
    b,a = a,b

### 6.is和== 的区别：
== 是比较操作符，比较对象的值是否一致，is是判断对象之间的身份(内存地址)是否相同，可以用
id()的方法查看内存地址。

    a = [1,2]
    pring(id(a))

### 7.python函数中的参数类型
位置参数，默认参数，可变参数，关键字参数
        
    def example_function(positional, default="default value", *args, **kwargs):
        print("Positional argument:", positional)
        print("Default argument:", default)
        print("Variable length positional arguments (args):", args)
        print("Keyword arguments (kwargs):", kwargs)
    
    # 调用示例
    example_function("positional value")
    example_function("positional value", "non-default value")
    example_function("positional value", "non-default value", 1, 2, 3)
    example_function("positional value", "non-default value", 1, 2, 3, key1="value1", key2="value2")
    
### 8.*arg 和 ** kwarg

    def ekke(*args, **kwargs):
    if args:
        print("args:",args)
    if kwargs:
        print("kwargs:",kwargs)
    ekke(1,2,3,key = '222')

    args: (1, 2, 3)
    kwargs: {'key': '222'}

*arg 会把位置参数转变为tuple，*kwarg会把关键字参数转为dict

### 9.获取当前时间

    import time
    import datetime
    
    print(datetime.datetime.now())
    print(time.strftime("%Y-%m-%d"))


### 10.PEP8规范
1. 尽量避免使用小写字母l，大写字母O，以及大写字母I等容易混淆的字母
2. 函数命名使用全部小写的方式
3. 变量命名使用全部大写的方式
4. 使用has 或者 is 命名布尔元素
5. 不要使用反斜杠连接行
6. 方法定义之间空一行，顶级定义之间空两行
7. 如果一个类不能继承其他类，就从object中继承。
8. 内部使用的类，方法，变量前加前缀_ 表明

### 11.python的深浅拷贝
1. 浅拷贝:只成功拷贝了列表的外城，列表内层的列表还是共享的
    
        import copy
        list1 = [1,2,3,[1,2,'a']]
        
        list2 = copy.copy(list1)
        list2.append('a')
        list2[3].append('a')
        print(list1)
        print(list2)

2. 深拷贝:两个列表完全独立开来，一个列表的操作不会影响另外一个

        import copy
        list1 = [1,2,3,[1,2,'a']]
        list2 = copy.deepcopy(list1)
        list2.append('a')
        list2[3].append('a')
        print(list1)
        print(list2)

### 12.【lambda x:i*x for i in rnage(4)]
由于闭包的特性，闭包会延迟对外部函数变量的求值，直到内部函数被调用。这也是为什么在循环中创建闭包时，所有闭包引用的都是循环变量的最终值。
这4个lambda函数都会引用 i 的最终值。由于 range(4) 的最后一个值是3，所以每个lambda函数的 i 都是3,
结果为【3，3，3，3】

问题解决：

      def num():
          return [lambda x,i=i: i*x for i in range(4)]
      a = [m(1) for m in num()]
      print(a)

### 13 九九乘法表：print函数会默认换行
      for i in range(10):
          for j in range(1,i+1):
              print(f"{i}*{j} = {i*j}",end= ' ')
          print()

### 14.filter,map,reduce的作用：
1. filter函数用于过滤序列，它接收一个函数和一个序列，把函数作用在序列上，根据返回值的True，False来判断是否保留元素。


      list1 = [i for i in range(10)]
      list2 = list(filter(lambda x:x%2 == 1,list1))
      print(list2)
2. map函数传入一个函数和一个序列，把函数作用到序列上的每一个元素，并且返回一个可迭代的对象。
   

      list1 = [i for i in range(10)]
      list2 = list(map(lambda x:x%2,list1))
      print(list2)
3. reduce用于递归计算，同样传入一个函数和一个序列，并把函数与序列的计算结果与下一个元素计算。
   

      from functools import reduce
      a = reduce(lambda x,y:x+y,range(101))
      print(a)
      
      from functools import reduce
      a = reduce(lambda x,y:y if x<y else x,[1,2,3,4])
      print(a)
   
      from functools import reduce
      a = reduce(lambda x,y:x*10+y,[3,4,5,6])
      print(a)

### 15.为什么不建议函数的默认参数传入可变的对象

      def test(L=[]):
         L.append('test')
         print(L)

### 16.__new__ 和 __init__ 的区别：
__new__ 是在创建实例之前就被调用，因为它的任务就是创建实例然后返回该实例对象，是个静态方法。

__init__是当实例对象创建完成后被调用，然后设置对象属性的一些初始值，通常在初始化的时候实用，是一个实例方法。

### 17.三元运算的规则：
      a ,b = 2,4
      h = a-b if a>b else b-a
### 18.生成随机数字
      import numpy as np
      a = np.random.randint(0,100,20)
      b = np.random.random()
### 19.zip的用法：
zip函数将可迭代的对象作为参数，然后将对象中对应的元素打包成一个元组，然后返回这个元组

      list1 = ['a', 'b', 'c', 'd']
      list2 = [2,3,4,5]
      tuppppple = list(zip(list1,list2))
      print(tuppppple)

### 20.range 和xrange的区别


