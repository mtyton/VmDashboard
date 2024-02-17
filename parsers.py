from adapters import VBoxManage
from api.routers.vms import VMBasicData, VMDetailedData


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


def parse_vm_info(vm_info):
    vm_info = vm_info.split()
    vm = VMDetailedData(
        uuid=vm_info[11],
        name=vm_info[1],
        state=vbox.check_if_running(str('"' + vm_info[1] +
                                        '" {' + vm_info[11] + '}')),
        cpu=vm_info[51],
        memory=vm_info[29][:-2],
        disk=20,
        network=100
    )
    return vm


vbox = VBoxManage()
vbox.start_vm('deb')
vm_list = vbox.list_virtual_machines()
status_list = vbox.get_all_vm_status()
parsed_list = parse_vm_list(vm_list, status_list)

info = vbox.get_vm_info('deb')
parsed_info = parse_vm_info(info)
print(parsed_info)
vbox.stop_vm('deb')
