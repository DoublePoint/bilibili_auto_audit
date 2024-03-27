from jsonpath import jsonpath

data = {'key1':{'key2':{'key3':{'key4':{'key5':{'key6':{'key7':'python'}}}}}}}

# 原始json的获取方式
print(data['key1']['key2']['key3']['key4']['key5']['key6']['key7'])
# 用法1，jsonpath的返回结果是一个列表
print(jsonpath(data,'$.key1.key2.key3.key4.key5.key6.key7'))

print(jsonpath(data,'$..key6..key7'))