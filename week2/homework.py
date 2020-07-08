
#写一个读取和写入json数据的函数
import json

def write_json(data, file_path):
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

def read_json(file_path):
    with open(file_path, encoding='utf-8') as f:
        return json.load(f)
        
file_path = input('请输入json文件路径:')
data = read_json(file_path)
print(data)

write_path = input('请输入保存的json文件名称：')
write_json(data, write_path)
