### numpy usage
1. 数组创建函数
  * array
  * asarry
  * arange
  * ones, ones_like
  * zeros, zeros_like
  * empty, empty_like
  * eye, identity
2. dtype,astype（astype无论如何都会创建出一个新的数组，是原始数组的一份拷贝）
3. numpy的数据类型
  * int8,unit8
  * int16, uint16
  * int32,uint32
  * int64,uint64
  * float16
  * float32
  * float64
  * float128
  * complex64,complex128
  * bool
  * object
  * string_
  * unicode_
 
4. 大小相等的数组之间的任何算是运算都会将运算应用到元素级
5. 不同大小的数组之间的运算叫广播
6. 基本的索引和切片
  * 数组切片是原始数组的视图，数据不会被复制，视图上的任何修改都会直接反映到源数组上
  * 布尔型索引
    * numpy.random生成一些正态分布的随机数据
  * 数组转置和轴对称
    * .T /.transpose(())/.swapaxes()
    *  np.dox计算矩阵內积
    * 返回数据源的视图，都不会进行任何复制操作
7. 通用函数：快速的元素块级组函数
  * 通用函数：ufunc
  * 许多ufunc都是简单的元素级变体
  * 一元函数：
    * sqrt,
    * exp
    * abs, fabs
    * square
    * log, log10,log2,log1p
    * sign
    * ceil
    * floor
    * rint：四舍五入
    * modf:将数组的小数和整数以两个独立的组的形式返回
    * isnan
    * isfinite,isinf
    * cos,cosh,sin,sinh,tan,tanh
    * arccos,arcsin,
    * logical_not
  * 二元：接收两个数组： add, maximum
    * np.add(x1,x2)
    * substract
    * multiply
    * divide,floor_divide
    * power
    * maximum,fmax
    * minimum,fmin
    * mod
    * sopysign
    * greater,
    * less
    * equal
    * logical_and, logical_or, logical_xor
8. 利用数组进行数据分析
9. 将条件逻辑表述为数组运算
  * numpy.where函数时三元表达式，x if condition else y的矢量化版本，可以用np.where简化，np.where(condtion,x,y).第二个和第三个参数不必是数组，可以是标量值。where通常用于根据另一个数组儿产生一个新的数组。
10. 数学和统计方法
  * sum, mean,std,var
  * min, max
  * argmin,argmax
  * cumsum:累积和，cumprod：累积积
  * 对于布尔型数组的方法:any()用于检测数组中是否含有一个或多个true,all()检查数组中所有值是否都为true
11. 排序
  * sort():多维数组可以再任何一个轴上牌勋，只需要把轴编号传给sort
  * 数组的集合运算：
    * unique(x)
    * intersect1d(x,y)
    * union1d(x,y)
    * in1d(x,y)
    * setdiff1d(x,y)
    * setxor1d(x,y)
12. 将数组以二进制格式保存到磁盘
  * np.save和np.load是读写磁盘数组数据的两个函数。数组是以未压缩的原始二进制格式保存在.npy的文件中。
