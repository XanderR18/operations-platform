from .services.machine_service import MachineService
from .models.machine import Machine

def bootstrap(machine_service):
    # Hard coding for testing. Not permanent
    compute_machine = Machine("cm1", "compute-main", "192.168.0.20", "70-54-D2-AB-1B-5D")
    network_machine = Machine("nm1", "network-main", "192.168.0.30", "94-C6-91-A2-A4-61")
    storage_machine = Machine("sm1", "storage-main", "192.168.0.40", "B4-2E-99-3B-4A-B3")

    machine_service.add_machine(compute_machine)
    machine_service.add_machine(network_machine)
    machine_service.add_machine(storage_machine)

    print(machine_service.get_all_machines())