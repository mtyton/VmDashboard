from adapters import VBoxManage
from api.routers.vms import VMBasicData


def parse_vm_list(vm_list, status_list):
    vm_list = vm_list.splitlines()
    parsed_list = []
    for idx, vm in enumerate(vm_list):
        vm_data = vm.split()
        name = vm_data[0].replace('"', '')
        uuid = vm_data[1]
        vm_basic = VMBasicData(name=name, uuid=uuid, state=status_list[idx])
        parsed_list.append(vm_basic)
    return parsed_list


vbox = VBoxManage()

vm_list = vbox.list_virtual_machines()
status_list = vbox.get_all_vm_status()
parsed_list = parse_vm_list(vm_list, status_list)

print(parsed_list)
