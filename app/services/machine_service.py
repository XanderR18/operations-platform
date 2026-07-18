import logging
import subprocess
from datetime import datetime
from ..models.machine_health import MachineHealthStatus
from ..models.machine import Machine
 
logging = logging.getLogger(__name__)

class MachineService():
    def __init__(self, name):
        self.name = name
        self.machines = {}

    def start(self) -> None:
        logging.info("Machine service succesfully started.")
    
    def stop(self) -> None:
        logging.info("Machine service succesfully stopped.")
    
    def add_machine(self, machine: Machine) -> None:
        if machine.id in self.machines:
            raise DuplicateMachine(f"Machine with id: {machine.id} already exists.")

        self.machines[machine.id] = machine
        logging.info(f"Machine with id: {machine.id} has been registered.")

    def remove_machine(self, machine_id: int) -> None:
        if machine_id not in self.machines:
            raise MachineNotFound(f"Machine with id: {machine_id} not found.")
        
        del self.machines[machine_id]
        logging.info(f"Machine id: {machine_id} has been removed.")


    def update_machine_identity(self, machine: Machine) -> None:
        if machine.id not in self.machines:
            raise MachineNotFound(f"Machine with id: {machine.id} not found.")
        
        existing: Machine = self.machines.get(machine.id)

        existing.host_name = machine.host_name
        existing.ip = machine.ip
        existing.mac = machine.mac
        existing.role = machine.role
        
        logging.info(f"Machine with id: {machine.id} has been updated.")

    def get_machine(self, machine_id: str) -> Machine:
        if machine_id not in self.machines:
            raise MachineNotFound(f"Machine with id: {machine_id} not found.")

        return self.machines[machine_id]

    def get_all_machines(self) -> dict:
        return self.machines
    
    def refresh_health(self) -> None:
        for machine in self.machines.values():
            self._refresh_machine_health(machine)
        logging.info("Machine healths sucessfully refreshed.")
            
    def _refresh_machine_health(self, machine: Machine) -> None:
        alive = self._ping(machine.ip)

        status = MachineHealthStatus.ONLINE if alive else MachineHealthStatus.OFFLINE
        
        machine.health.update(status, datetime.now())
        logging.info(f"{machine.id} -> {status}")
    
    def _ping(self, ip: str) -> bool:
        result = subprocess.run(
            ["ping", "-n", "1", "-w", "1000", ip],
            # ["ping", "-c", "1", "-W", "1", ip] Linux for later if needed
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        return result.returncode == 0

    def __repr__(self) -> str:
        return f"Service({self.name})"
    
class MachineNotFound(Exception):
    pass

class DuplicateMachine(Exception):
    pass