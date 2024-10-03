class Service:
    def __init__(self, address, id):
        self.address = address
        self.id = id
        self.base_dict = {'address': self.address, "id": self.id}

    def arrival_time(self):
        return len(self.address)
    
    def get(self):
        return self.base_dict
    

class Ambulance(Service):
    def __init__(self, address, id, mode, severity):
        self.mode = mode
        self.severity = severity
        super().__init__(address, id)
        self.base_dict["mode"] = self.mode
        self.base_dict["severity"] = self.severity
    

class Firefighters(Service):
    def __init__(self, address, id, mode, victims):
        self.mode = mode
        self.victims = victims
        super().__init__(address, id)
        self.base_dict["mode"] = self.mode
        self.base_dict["victims"] = self.victims


class Police(Firefighters):
    def __init__(self, address, id, mode, victims, armament_required):
        self.armament_required = armament_required
        super().__init__(address, id, mode, victims)
        self.base_dict["armament_required"] = self.armament_required 

amb = Ambulance("Bolshaya Gruzinskaya str., 1", 2, 5, 0)
print(amb.get())
print(amb.arrival_time())