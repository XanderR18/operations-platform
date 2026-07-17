class Machine():
    def __init__(self, id, host_name, IP, MAC):
        self.id = id
        self.host_name = host_name
        self.ip = IP
        self.mac = MAC

    def __repr__(self):
        return f"Machine(id='{self.id}', name='{self.host_name}', ip='{self.ip}', mac='{self.mac}')"