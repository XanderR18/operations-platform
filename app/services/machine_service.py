import logging
from ..models.machine import Machine
 
logging = logging.getLogger(__name__)

class MachineService():
    def __init__(self):
        self.machines = {}

    def start(self):
        return
    
    def stop(self):
        return
    
    def add_machine(self, machine:Machine):
        machine_id = machine.id
        if machine_id in self.machines:
            machine_id += "(1)"

        self.machines[machine_id] = machine

    def remove_machine(self, machine_id):
        if machine_id not in self.machines:
            raise MachineNotFound(f"Machine with id: {machine_id} not found.")
        
        del self.machines[machine_id]

    def update_machine(self, machine:Machine):
        if machine.id not in self.machines:
            raise MachineNotFound(f"Machine with id: {machine.id} not found.")
        
        self.machines[machine.id] = machine

    def get_machine(self, machine_id):
        if machine_id not in self.machines:
            raise MachineNotFound(f"Machine with id: {machine_id} not found.")

        return self.machines[machine_id]

    def get_all_machines(self):
        if not self.machines:
            return 0

        return self.machines
    
class MachineNotFound(Exception):
    pass

# Hard coding for testing. Not permanent
Machine("cm1", "compute-main", "192.168.0.20", "70-54-D2-AB-1B-5D")
Machine("nm1", "network-main", "192.168.0.30", "94-C6-91-A2-A4-61")
Machine("sm1", "storage-main", "192.168.0.40", "B4-2E-99-3B-4A-B3")