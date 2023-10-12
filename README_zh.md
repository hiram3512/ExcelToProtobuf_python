## 如何使用
![](/Others/Q9RVLdhun7.png)
- 双击执行main.bat
- 选择目录
- 点击生成

> 第一次使用工具时:
> - 双击[setup.bat](setup.bat)自动唤起python安装程序(勾选Add Python 3.10 to PATH)
> - 双击[setup_dependence.bat](setup_dependence.bat)自动安装依赖库

## 配置规则
参照[Example](Example)文件夹下的示例
- proto说明: https://developers.google.com/protocol-buffers/docs/proto3
- excel说明:
    - 第一行是注释,第二行是字段名,第三行以后是数据
    - 支持一个Sheet
    - 使用,分隔数组

## 导出数据
![](/Others/FvCsQi9QOz.png)
- json (方便查看导出数据)
- bin (二进制数据)
- pb (描述文件)

## 导出语言
- cpp
- csharp
- java
- python

-----

## More:

### 类型转换
标准python类型: 
https://docs.python.org/3/library/stdtypes.html#

官方类型对照表: https://developers.google.com/protocol-buffers/docs/proto3
![](/Others/vbBuHG4DUC.png)

转换规则:
- int32,sint32,sfixed32转换为int

- double,float转换为float

- int64,uint32,uint64,sint64,fixed32,fixed64,sfixed64转换为int(不是long)

- bool转换为bool

- string转换为str

- bytes转换为bytes

为何int64等类型转换为int?在python 3.x版本只有一种内置的数值类型int:

>PEP 237: Essentially, long renamed to int. That is, there is only one built-in integral type, named int; but it behaves mostly like the old long type.https://docs.python.org/3/whatsnew/3.0.html#integers

### 日志
- 日志在logs文件夹中
- 可以通过查找error关键字查找导出错误


-----

## Develop

### python规范 
https://google.github.io/styleguide/pyguide.html

### 语言扩展

#### 官方支持语言
- 只导出常用的/不需要依赖库的语言
- go,dart等需要额外安装工具/库才能导出,可以根据需要安装后导出

#### 其他语言支持
- Lua
  - 有描述文件pb,有数据文件bin,有很多开源库解析这两个文件成lua tale(常规做法)
  - 有带数据格式的json文件,有很多开源库转换json成lua文件
  - Unreal Engine/Unity 

support: hiramtan@live.com