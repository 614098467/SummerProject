# 5-31 Linux命令篇

## cat的功能参数用法
    1.cat gezhou.txt      #查看文本内容
    2.cat -b gezhou.txt  #对非空行显示行号
    3.cat -n gezhou.txt  #对所有行显示行号
    4.cat -n -E gezhou.txt  #在每行结尾加上$符号
    5.cat -s gezhoiu.txt   #减少空行数量
## cat命令合并多个文件
    cat douyin.txt gushi.txt > ./抖音和古诗的文本内容.txt
## cat非交互式的命令：
    cat >> 要写入的文件.txt << EOF
## cat清空文件的用法：
1.直接清空文件,留下了一个空行

    echo > 要清空的文件.txt  
2.直接清空文件内容，不留空行
   
    > 要清空的文件.txt
3.利用cat读取一个黑洞文件，然后清空其他文本

    cat /dev/null > 要清空的文件.txt

## tac命令与cat命令结果相反
>从尾往前边读取

## 管道符
1.查看gushi中的内容，并且利用管道符进行过滤

    cat gushi.txt | grep "know me"
> grep:过滤文本中的内容

## more命令和less命令：
语法：more 文件名 # 分屏显示文件内容
> 1.按下enter是下一行
> 
> 2.空格是向下滚动一个屏幕
> 
> 3.=显示当前行号
> 
> 4.q退出

>less命令与more命令相同

## head 和 tail 命令
head命令用来查看文件开头的n行

    语法： head -n 文件名    # 查看文件前n行
          head    文件名    # 默认显示10行
          head -c 3 文件名    #查看文件中的3个字符

tail命令用来查看文件后n行

    语法： tail -n 文件名    # 查看文件后n行
          tail    文件名    # 默认显示10行
          tail -f 文件名    # 监测文件内容的实时更改
          tail -F 文件名    # 不断的打开文件
## cut命令的用法：
    cut  -c 4 文件名      # 根据第4个字符进行切割
    cut  -c 4-7 文件名    # 根据第4-7个字符进行切割
    cut  -c  4，6 文件名  # 去除第4个和第6个
    cut -c -7 文件名      # 从头到第7个字符
    cut -c 8- 文件名      # 从第8个字符到结尾
    cut -d ":" -f  区域范围 文件名 
    cut -d ":" -f  3 文件名    #利用：分割，找出第3个区域的内容
## Sort排序命令：
    1.针对数字进行排序
    sort -n sort.txt 
    
    2.从大到小排序
    sort -n -r sort.txt
    
    3.对排序结果去重 unique
    sort -u  sort.txt

    4.指定分割符号，指定区域进行排序
    sort -n -t "." -k 4 sort.txt
    #根据"."分割符，对第四个区域进行排序
    例子：
    10.0.0.1
    10.0.0.4
    10.0.0.23
    10.0.0.212  

## uniq命令：去重命令
    1.去除连续的重复行
    uniq sort.txt

    2.先进行排序，再进行去重
    sort -n sort.txt | uniq 
    
    3.统计每一行的重复次数 -c  count
    sort -n sort.txt | uniq -c

    4.只找出文件重复行，并统计次数 -d
    sort -n sort.txt | uniq -c -d
    
    5.找出文件中只出现一次的行 -u
    sort -n sort.txt | uniq -c -u

## wc命令：统计文件的行数，单词，字节数
    1.统计文件行数 -l
    wc -l wc.txt 
    
    2.统计单词的数量 -w
    echo "A,B,C,D,E,F" | wc -w 
    
    3.打印字符数 -m
    注意：因为每一行都有$符号，所以会比看到的多一个
    例如：
        echo "gezhou" | wc -m  
        7
    4.打印最长行的字符数 -L
    wc -L

## tr命令：从标准输入中替换、缩减或删除字符，将结果写入到标准输出
>用法：tr 字符1  字符2
    
    1.替换标准输入中的大小写
         echo "my name is a" | tr '[a-z]' '[A-Z]'
    2.使用-d 删除参数
        @ echo "my name is a 9999" | tr -d '[a-z]' 
        9999
        @ echo "my name is a 9999" | tr -d 'a'
        my nme is
        @ echo "my name is a 9999" | tr -d '0-9'
        my name is a 
    3.把文件中的内容进行替换,把小写a转换为大写A
        tr 'a' 'A' < alex.txt

## stat命令用于显示文件状态信息，比ls -l更为详细
>命令：stat（选项）（参数）
    
## find命令：
    1.根据名字进行全盘搜索txt文件
    find / -name "*.txt"

    2.限制查找的最大文件夹深度
    find /opt -maxdepth 2 -name "*.txt"

    3.找到特定的文件并且删除
    find . -type f -name "[0-9]*"   -delete
    #从当前盘中找到文件类型为f，命名为0-9开头的文件并且删除

    4.反向查找(!取反）
    find . -maxdepth 1 ! -type d

    5.通过文件大小查找
    find . -maxdepth 2 -type f -size +200M

## Xargs命令：
    1.多行变为单行

    2.拆分：
        ''' echo "alex,mjj,cunzhang,gezhou"|xargs -d ","'''

    3.-i 用{}代替文本
    将当前所有的txt文件，移动到alltemptxt目录中
        find . -name "*.txt"| xargs -i mv {} alltemptxt/

## 文件属性管理：
    ls -lhi
第一列"130053" :Inode号码 索引节点，身份证号码

第二列"-rw-r--r":文件的类型Linux权限

第三列"1":硬链接的数量，超市前后门，超市前后门的数量

第四列："root":属主

第五列：文件大小

第六列：文件修改时间

第七列：文件名



    

    
        
    








    

