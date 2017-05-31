# ExcelDataCollation

A tiny tools framework to collate data in excel files.

For example :
- IDCard
- Phone Number
- data duplication
- and so on.

## Usage:

app.py is a gui interface entrance.

# Excel数据整理工具

本工具是一个excel数据整理框架，可以为运营人员的常用操作提供便利。
快速整理excel中一些字段，如手机号、身份证号校验、去重；手机归属地查询等。

# 可用的过滤器有

- idcard
   - 要求字段：文本，大陆身份证号
   - 输出：1
- mobileLocation
   - 要求字段：文本，手机号
   - 输出：3
- repeat
   - 要求字段：文本，任意
   - 输出：1

# 使用方式

1. 预处理，将所要整理的列变为所需格式（如文本）
2. 编写处理配置文件如：
    


		{
			"name":"test",
			"output":"E",
			"filters":[
				{ "name":"repeat", "source":"A" },
				{ "name":"idcard", "source":"B" },
				{ "name":"mobileLocation", "source":"A","target":"C,D" }
			]
		}

其中output是标准输出列，每个过滤器至少有一个输出，source是过滤器来源列，target是过滤器特有输出列

3. 运行：
    1. gui界面
    2. dataCollation 命令行
