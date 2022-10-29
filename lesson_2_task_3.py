import yaml

key_list = ['word1', 'word2', 'слово3']
key_integer = 4
key_dict = {
    '1§': "paragraph",
    '30€': '30 euros'
}
yaml_data = {
    'first_key': key_list,
    'second_key': key_integer,
    'third_key': key_dict
}
with open('file.yaml', 'w', encoding='utf-8') as yaml_file:
    yaml.dump(yaml_data, yaml_file, default_flow_style=False, allow_unicode=True)
with open('file.yaml', 'r', encoding='utf-8') as yaml_file:
    yaml_content = yaml.load(yaml_file, Loader=yaml.Loader)
print('Так выглядят исходные данные:')
print(yaml_data)
print('А так считаные с .yaml файла:')
print(yaml_content)

# print(d)
# print(type(d))
