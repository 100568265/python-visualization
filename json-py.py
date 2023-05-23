import json
import pyecharts

data = [{"name":"老王","age":16},{"name":"张三","age":26},{"name":"李四","age":30}]

#通过json.dumps()方法把python数据转换成json数据
json_str = json.dumps(data,ensure_ascii=False)
print(json_str)
#通过json.loads()方法把json数据转换为python数据
#data = json.loads(data)