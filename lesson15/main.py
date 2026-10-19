import csv
import json
from pathlib import Path

import xml.etree.ElementTree as ET
from xml.etree.ElementTree import ElementTree

work_dir = Path.cwd().parent
print(type(work_dir))
print(work_dir)

# dirs = [f.name for f in work_dir.iterdir() if f.is_dir()]
# for file in work_dir.iterdir():
#     print(file.name)
#
# print(dirs)

def get_py_modules(path: Path | str = None):
    # path = Path(FilePath)
    if path is None:
        path = Path.cwd()
    elif isinstance(path, str):
        path = Path(path)

    if not path.exists():
        raise ValueError(f'Dir with path {path} is not exist')

    py_modules = []
    for file in path.iterdir():
        if file.is_dir() and not file.name.startswith('.'):
            py_modules.extend(get_py_modules(file))
        # if file.name.endswith('.py'):
        if file.suffix == '.py':
            py_modules.append(file)

    return py_modules

py_modules = get_py_modules(work_dir)
print(get_py_modules())
print(py_modules)

# new_dir = Path(r'C:\Users\DzMS\PycharmProjects\Hillel082026\lesson15\new_dir1\sub_dir\sub_2')
new_dir = work_dir / 'new_dir'
new_dir.mkdir(parents=True, exist_ok=True)

file_with_modules = new_dir / 'modules.txt'
# file_with_modules.write_text('Hello World')

# try:
#     file_with_modules.open()
# finally:
#     file_with_modules.close()

with open(file_with_modules, mode='w+') as file:
    file.writelines([f'{m.name}\n' for m in py_modules])

with open(file_with_modules) as f:
    print(f.read())

# print([f for f in work_dir.glob('*/*.py')])

dict_modules = {f.name: str(f) for f in py_modules}
# print(dict_modules)
# json_modules = json.dumps(dict_modules, indent=4)
# print(type(json_modules))

person = {
    "name": "Vasiya",
    "age": 21,
    "pass": {
        "id": 333,
        "add": "Adress"
    }
}

with open(new_dir / 'modules.json', mode='w+') as file:
    # json.dump(dict_modules, file, indent=4)
    json.dump(person, file, indent=4)

with open(new_dir / 'modules.json') as file:
    # json.dump(dict_modules, file, indent=4)
    load = json.load(file)
    print(load)


csv_modules = [
    [f.name, str(f)] for f in py_modules
]
with open(new_dir / 'modules.csv', mode='w+', newline='') as file:
    csv_file = csv.writer(file)
    csv_file.writerow(['name', "path"])
    csv_file.writerows(csv_modules)

with open(new_dir / 'modules.csv', newline='') as file:
    csv_file = csv.reader(file)
    for row in csv_file:
        print(row)


root = ET.Element('person')
name = ET.SubElement(root, 'name')
name.text = 'Vasiya'
age = ET.SubElement(root, 'age')
age.text = '21'
pass_el = ET.SubElement(root, 'pass')
pass_id = ET.SubElement(pass_el, 'id')
pass_id.text = '333'
pass_add = ET.SubElement(pass_el, 'add')
pass_add.text = 'Adress'

xml_file = ElementTree(root)
xml_file.write(new_dir / 'person.xml')

# with open(new_dir / 'person.xml', mode='w+') as file:
#     file.write(ElementTree(root))

el_tree = ET.parse(new_dir / 'person.xml')
print(el_tree.getroot().iterfind('name'))