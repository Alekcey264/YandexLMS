from zipfile import ZipFile


with ZipFile("1.zip") as myzip:
    names_list = [name.strip() for name in myzip.namelist()]
    for name in names_list:
        if name[-1] == "/":
            name = name[:-1]
        print("  " * name.count("/") + name[name.rfind("/") + 1:])
