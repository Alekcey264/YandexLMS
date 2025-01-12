import os 


def human_read_format(size: int):
    sizes = {1: "Б", 2: "КБ", 3: "МБ", 4: "ГБ"}
    def_size = 1
    while size > 1023:
        size /= 1024
        def_size += 1
    return str(round(size)) + sizes[def_size]


def get_files_sizes():
    files = [file for file in os.listdir() if os.path.isfile(file)]
    return '\n'.join([' '.join([file, human_read_format(os.path.getsize(file))]) for file in files])


print(get_files_sizes())