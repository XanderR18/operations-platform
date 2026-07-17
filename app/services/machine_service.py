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
        self.machines[machine.id] = machine

    def remove_machine(self, machine_id):
        del self.machines[machine_id]

    def update_machine(self, machine:Machine):
        self.machines[machine.id] = machine

    def get_machine(self, machine_id):
        return self.machines[machine_id]

    def get_all_machines(self):
        return self.machines
    
    # Hard coding for testing. Not permanent
    Machine("compute-main", "192.168.0.20", "70-54-D2-AB-1B-5D")
    Machine("network-main", "192.168.0.30", "94-C6-91-A2-A4-61")
    Machine("storage-main", "192.168.0.40", "B4-2E-99-3B-4A-B3")