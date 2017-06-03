#### 机器学习中R语言使用的程序包
1. arm： 用于构建多水平，多层次回归模型的程序包
2. ggplot2 ：创建高质量图形的首选程序包
3. glmnet:广义线性模型的包
4. igraph:
5. lme4
6. lubricate
7. rcurl
8. reshape
9. tm
10. xml
11. RJSONIO

#### 寻求帮助文档
1. ？packagename :读取一个函数的帮助文档
2. ??base::packagename ：在所有base包的帮助文档中搜索包

#### 读取文件
1. read.delim(file, header = TRUE, sep = "\t", quote = "\"",
           dec = ".", fill = TRUE, comment.char = "", ...)
* 在处理不熟悉的数据的时候，stringAsFactors=false来防止其转换，如果数据没有表头的时候，还需要把表头参数设置为false，以防R默认把第一行当做表头。数据中有许多空元素，我们想把这些空元素设置为R中的特殊值、NA。显式的定义空字符串为na.string();

2. names(x) <- value:Functions to get or set the names of an object.
  * 既可以读取列名，又能写入列名。我们要根据数据文档创建一个与数据集的列名相应的字符串向量，然后把它作为names函数唯一的参数传入

#### 手工查看数据
1. 比较好用的是head和tail。打印数据框的前六条和后六条
