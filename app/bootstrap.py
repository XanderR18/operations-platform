import logging
from .models.machine import Machine, MachineRole

logging = logging.getLogger(__name__)

def bootstrap(machine_service):
    # Hard coding for testing. Not permanent
    workstation_machine = Machine("workstation-main", "workstation-main", "192.168.0.10", "E0-D5-5E-CF-DC-68", MachineRole.WORKSTATION)
    compute_machine = Machine("compute-main", "compute-main", "192.168.0.20", "70-54-D2-AB-1B-5D", MachineRole.COMPUTE)
    network_machine = Machine("network-main", "network-main", "192.168.0.30", "94-C6-91-A2-A4-61", MachineRole.NETWORK)
    storage_machine = Machine("storage-main", "storage-main", "192.168.0.40", "B4-2E-99-3B-4A-B3", MachineRole.STORAGE)

    machine_service.add_machine(workstation_machine)
    machine_service.add_machine(compute_machine)
    machine_service.add_machine(network_machine)
    machine_service.add_machine(storage_machine)

    logging.info(f"Bootstrapped {len(machine_service.get_all_machines())} machines")

    logging.info("Bootstrapping complete.")