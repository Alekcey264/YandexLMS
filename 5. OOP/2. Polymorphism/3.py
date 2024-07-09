from datetime import datetime


class ShoppingList:
    def __init__(self, *shop_list):
        self.shop_list = list(shop_list)

    def values(self):
        return self.shop_list

    def append(self, value):
        self.shop_list.append((value, False))

    def check(self, value):
        for i in range(len(self.shop_list)):
            if self.shop_list[i][0] == value:
                self.shop_list[i] = (self.shop_list[i][0], True)

    def checked_values(self):
        return [item for item in self.shop_list if item[1]]
    
    def rest_values(self):
        return [item for item in self.shop_list if not item[1]]


class TODOList:
    def __init__(self, *values):
        self.todo_list = list(values)

    def append(self, *value):
        self.todo_list.append((*value, False))
        self.todo_list.sort(key=lambda x: -x[1])

    def check(self, value):
        for i in range(len(self.todo_list)):
            if self.todo_list[i][0] == value:
                self.todo_list[i] = (*self.todo_list[i][:2], True)

    def values(self):
        self.todo_list.sort(key=lambda x: -x[1])
        return self.todo_list
    
    def checked_values(self):
        return [item for item in self.todo_list if item[2]]
    
    def rest_values(self):
        return [item for item in self.todo_list if not item[2]]


class Route:
    def __init__(self, *values):
        self.routes_list = list(values)

    def append(self, *value):
        if (len(self.routes_list) == 0 
                or datetime.strptime(value[1], '%H:%M') > datetime.strptime(self.routes_list[-1][1], '%H:%M')):
            self.routes_list.append((*value, False))

    def check(self, value):
        for i in range(len(self.routes_list)):
            if self.routes_list[i][0] == value:
                self.routes_list[i] = (*self.routes_list[i][:2], True)

    def values(self):
        return self.routes_list
    
    def checked_values(self):
        return [item for item in self.routes_list if item[2]]

    def rest_values(self):
        return [item for item in self.routes_list if not item[2]]
    


path = Route()
path.append("Kew Gardens", "11:53")
path.append("Willesden Junction", "11:59")
path.append("Acton Central", "12:01")
print(*path.values(), sep="\n")
print()
path.append("Richmond", "12:12")
path.check("Kew Gardens")
print(*[x[0] for x in path.rest_values()], sep="\n")
print()
print(*path.checked_values(), sep="\n")