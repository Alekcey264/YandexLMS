from zipfile import ZipFile
import os


def human_read_format(size: int):
    sizes = {1: "Б", 2: "КБ", 3: "МБ", 4: "ГБ"}
    def_size = 1
    while size > 1023:
        size /= 1024
        def_size += 1
    return str(round(size)) + sizes[def_size]


with ZipFile('1.zip') as myzip:
    data = myzip.infolist()
    for item in data:
        is_file = True
        name = item.orig_filename
        if name[-1] == "/":
            name = name[:-1]
            is_file = False
        if is_file:
            print("  " * name.count("/") + name[name.rfind("/") + 1:], human_read_format(item.file_size))
        else:
            print("  " * name.count("/") + name[name.rfind("/") + 1:])

        