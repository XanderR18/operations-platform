import logging
from ..models.machine import Machine
 
logging = logging.getLogger(__name__)

class MachineService():
    def __init__(self, name):
        self.name = name
        self.machines = {}

    def start(self):
        logging.info("Machine service succesfully started.")
    
    def stop(self):
        logging.info("Machine service succesfully stopped.")
    
    def add_machine(self, machine:Machine):
        if machine.id in self.machines:
            raise DuplicateMachine(f"Machine with id: {machine.id} already exists.")

        self.machines[machine.id] = machine
        logging.info(f"Machine with id: {machine.id} has been registered.")

    def remove_machine(self, machine_id):
        if machine_id not in self.machines:
            raise MachineNotFound(f"Machine with id: {machine_id} not found.")
        
        del self.machines[machine_id]
        logging.info(f"Machine id: {machine_id} has been removed.")


    def update_machine(self, machine:Machine):
        if machine.id not in self.machines:
            raise MachineNotFound(f"Machine with id: {machine.id} not found.")
        
        self.machines[machine.id] = machine
        logging.info(f"Machine with id: {machine.id} has been updated.")

    def get_machine(self, machine_id):
        if machine_id not in self.machines:
            raise MachineNotFound(f"Machine with id: {machine_id} not found.")

        return self.machines[machine_id]

    def get_all_machines(self):
        return self.machines
    
    def __repr__(self):
        return f"Service({self.name})"
    
class MachineNotFound(Exception):
    pass

class DuplicateMachine(Exception):
    pass