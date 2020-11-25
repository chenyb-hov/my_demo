package main

import "fmt"

func main(){
	fmt.Println("Hello,World!")
}

运行go run 文件名
注 : "{"不能在单独行上
变量命名规范 只能由大小写字母 数字 下划线组成,不能以数字开头
字符串连接用 + 号
变量声明 var name type; 例如 var a int;一次声明多个用逗号隔开
变量声明同时初始化 var a,b int = 1,2
var a,b = 123,"abc" 声明多个变量时类型不一致后面不要加类型
变量声明时若无初始化则值为系统默认
fmt.Printf("%v %v %v %q\n",i,f,b,s) i,f,b,s为变量,输出4个变量
另一种变量声明方式 var a=1 根据值判断变量类型
第三种变量声明方式 var a int   a,b := 1,2  如果后面没有声明新的变量会报错
f := 3 这个是正确声明变量的方式,前提是要放在函数中
var (a int
       b string)声明全局变量
变量与内存空间的关系 变量指向内存空间 赋值操作时 将被赋值的内存空间复制一份,赋值的变量指向新复制的内存空间
通过&变量 获取内容空间
引用类型ref 赋值则是指向内存空间,不需要复制
a := 1 不允许在同一代码块内多次出现 而允许a = 1多次出现
局部变量声明却没有使用会报错.
交换两个变量的值用 a,b = b,a 前提是他们类型要一致
_是一个只写变量无法得到它的值
常量定义 const修饰
多个同类型的常量可以一起声明 例如 const a,b=1,2
常量用作枚举 const(\n a = 1 \n b = "2" \n c = 3)
常量 可以用len()长度 cap() unsafe.Sizeof()等内置函数计算表达式的值
iota 特殊的常量 可以被编译器修改的常量 初始为0每增加一行值增加1 例如 const(\n a = iota \n b =  iota \n c =  iota) a=0,b=1,c=2 相当于 const(\n a = iota \n b \n c) 不管中间有几行iota增加
const(\n i=1<<iota \n j=3<<iota \n k \n l) i=1<<0,j=3<<1,k=3<<2,l=3<<3
算术运算符
+,-,*,/,%,++,--
关系运算符
==,!=,>,<,>=,<=
逻辑运算符
&&,||,!
位运算符
&,|,^,<<,>>
赋值运算符
=,+=,-=,/=,%=,*=,<<=,>>=,|=,&=,^=
其他运算符
&,*指针变量
select{
	case num1: 
	case num2:
	default: 
} 
如果有 default 子句，就执行default
若没有,且有多个 case 都可以运行，Select 会随机公平地选出一个执行。其他不会执行。
循环for 和嵌套for
goto 跳过本次循环并回到LOOP处  LOOP : for a<10{ goto LOOP}
func 函数名(参数,参数 类型) 返回类型{
函数体
}
返回类型为多个时用(re1,re2)
闭包 func func1() func2() 返回类型{
	return func2() 返回类型{
		return 
	}
}
结构体定义 type name struct{
	属性 类型
}
func (对象名 结构体) 函数名() 返回类型{
	return 对象名.属性 
}
局部变量在函数内部 
全局变量在函数外部
数组声明
var 数组名 [长度] 类型
初始化 var 数组名 = [长度]类型{a,b,c,d,e}
           var 数组名 = []类型{a,b,c,d,e}
多维数组 var 数组名 [数组长度][数组长度]...[数组长度] 类型
二维数组初始化 例如 a = [3][2]int{{1,2},{3,4},{5,6}}
数组作为函数参数
void funcname(arrayname []int) 返回类型{
	
}多个数组参数时用(arrayname1 []int,arrayname2 []float)
定义指针变量 var 变量名 *类型
一般这样使用 var a int =1;  var ip *int;  ip = &a;  这时候打印ip就是&a,打印*IP就是1
打印空指针(即未初始化)为0
空指针判断 if(指针变量 == nil)  
指向指针的指针 var 变量名 **类型
例如 var a =1; var ptr *int = &a; var pptr **int = &ptr; 打印 **pptr 的值为1
结构体指针 var 变量名 *类型
结构体指针作为参数打印仍然是值
语言切片
定义 var name []type
或者 var name []type = make([]type,len,cap)简写 name := make([]type,len,cap)
len 长度 cap 测量切片最长可以达到多少
判断是否为空切片 if(切片变量==nil)
切片截起类似js substring 前闭后开
切片变量.append(切片变量,元素)向切片添加元素 添加空切片则元素为0 添加多个元素用逗号隔开
copy(切片1,切片2) 拷贝切片2到切片1
range
for _,num := range 数组{ num数组内变量} 和for in 类似
若需要获取索引 则把 _ 替换成别的
range 也可用在map上 
例 kvs := map[string]string{'a':'123','b':'234'}
for k,v := range kvs{}
集合map
创建 var name map[type]type = make(map[type]type)
向map插入键值对 name[key] = value
for keyname := range mapname{keyname 即 key mapname[keyname] 即value}
判断元素是否在集合内 capital, ok := 集合名[键名] if(ok)
删除集合中的元素 delete(集合,键名)
递归 函数调用自身
类型转换
类型(变量/表达式)
接口
定义 type name interface{
	call()
}
可定义接口类型变量
错误处理
内置错误接口的定义
type error interface{
	Error() string
}
实现接口 func (变量 类型) 接口() string{
}
应用
type DivideError struct{
	dividee int
	divider int
}
func (de *DivideError) Error() string{
	strFormat := 'Cannot proceed, the divider is zero
		     dividee: %d
	      	     divider:0'
}
func Divide(varDividee int, varDivider int) (result int, errorMsg string){
	if varDivider==0{
		dData := DivideError{
			dividee: varDividee,
			divider: varDivider,
		}
		errorMsg = dData.Error()
		return
	}else{
		return varDividee / varDivider,""
	}
}
func main(){
	if result, errorMsg := Divide(100,10); errorMsg == ""{
		fmt.Println("100/10 = ",result)
	}
	if _,errorMsg := Divide(100,0);errorMsg != ""{
		fmt.Println("errorMsg is: ",errorMsg)
	}
}
函数返回类型若有多个(type1,type2)
并发
线程
使用 go 函数名(参数)
通道 channel
ch <- v 把v发送到通道 ch
v := <- ch 从ch接收数据 并把值赋给v
通道声明 ch := make(chan int) chan关键字
ch := make(chan int,2) 缓冲区大小为2
go遍历通道与关闭通道
close()函数关闭通道

运行工具Eclipse
1.下载Eclipse
2.下载 goclipse 插件 https://github.com/GoClipse/goclipse/blob/latest/documentation/Installation.md#installation
3.下载 gocode https://github.com/nsf/gocode
在 Windows下要安装 git，通常用 msysgit。
再在 cmd 下安装：
go get -u github.com/nsf/gocode
4.下载 MinGW 并按要求装好
5.配置插件
Windows->Reference->Go
