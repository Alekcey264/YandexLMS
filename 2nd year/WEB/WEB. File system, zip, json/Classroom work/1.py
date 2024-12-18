def human_read_format(size: int):
    sizes = {1: "Б", 2: "КБ", 3: "МБ", 4: "ГБ"}
    def_size = 1
    while size > 1023:
        size /= 1024
        def_size += 1
    return str(round(size)) + sizes[def_size]

print(human_read_format(15000))